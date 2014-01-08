oauth issue
====

认证和授权过程(来自维基百科)
----

    在认证和授权的过程中涉及的三方包括：
        1.服务提供方，用户使用服务提供方来存储受保护的资源，如照片，视频，联系人列表。
        2.用户 ，存放在服务提供方的受保护的资源的拥有者。
        3.客户端 ，要访问服务提供方资源的第三方应用。在认证过程之前，客户端要向服务提供者申请客户端标识。

    使用OAuth进行认证和授权的过程如下所示:
    1.用户访问客户端的网站，想操作自己存放在服务提供方的资源。
    2.客户端向服务提供方请求一个临时令牌。
    3.服务提供方验证客户端的身份后，授予一个临时令牌。
    4.客户端获得临时令牌后，将用户引导至服务提供方的授权页面请求用户授权。在这个过程中将临时令牌和客户端的回调连接发送给服务提供方。
    5.用户在服务提供方的网页上输入用户名和密码，然后授权该客户端访问所请求的资源。
    6.授权成功后，服务提供方引导用户返回客户端的网页。
    7.客户端根据临时令牌从服务提供方那里获取访问令牌 。
    8.服务提供方根据临时令牌和用户的授权情况授予客户端访问令牌。
    9.客户端使用获取的访问令牌访问存放在服务提供方上的受保护的资源。

python获得授权(以openmaster为例)
---
    文档
    http://dev.admaster.com.cn/doc/openmaster/v1/cn/oauth.html

    由于使用测试的地址，直接把id贴上了，没有什么用处。

    1.页面有一个链接让用户来点击登录,点击之后就会打开一个
    页面让用户登录，这里会是openmaster的页面，如果使用新浪微博
    则会打开新浪的登录页面，成功后会返回到redirect_uri指定的地址,
    并且在url中会带有code的信息。
    <a
    href="http://testopen.admasterapi.com/oauth/authorize?client_id=0839e9663d20068e44dd&response_type=code&redirect_uri=http://127.0.0.1:8000/oauth/authorize">
    oauth </a>

    2.后台取下code,将文档中需要添加的参数打包用urllib
    post到服务器上，这样会返回需要的access_token,有了access_token后就可以根据
    文档做一些事情了，例如取得用户的信息(get下数据即可)

    完整代码如下 (以django为例):

    def authorize(request):
        code = request.GET['code']
        req = urllib2.Request("http://testopen.admasterapi.com/oauth/access_token")
        param = {
                'client_id':'0839e9663d20068e44dd',
                'client_secret':'b446ddb809070a47236673cc8a54525c58aab9d4',
                'grant_type':'authorization_code',
                'code':code,
                'redirect_uri':'http://127.0.0.1:8000/',
               }.
        req.add_data(json.dumps(param))

        tokens = urllib2.urlopen(req).read()
        tokens = json.loads(tokens)
        access_token = tokens["access_token"]
        request.session["access_token"] = access_token

        get_url = "http://testopen.admasterapi.com/user?access_token={0}".format(access_token)
        user = urllib2.urlopen(get_url).read()
        user = json.loads(user)

        return render(request,'oauthapp/index.html',{"access_token":access_token,"user":user})

