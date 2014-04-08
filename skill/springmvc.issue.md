spring mvc 相关


spring mvc json使用
---

###导入 参照一下连接注意，Jackson 需要用all的jar包，并且版本要在1.9.1以上

http://www.mkyong.com/spring-mvc/spring-3-mvc-and-json-example/

    @RequestMapping(value = "test/user/json", method = RequestMethod.GET)
    public @ResponseBody User getJson() {
        return new User("name", "password", "login");
    }

   1. Jackson library is existed in the project classpath

   2.The mvc:annotation-driven is enabled

   3. Return method annotated with @ResponseBody

spring mvc + freemarker中表单组件 
---

定义一个form.ftl宏，restful风格的uri中需要添加_method这个hidden input,内容分别为put（修改），delete（删除），post(新加)
如果用@s.formXXX Controller中必须有绑定的对象，在这个例子里必须有User 对象，可以new，可以传参。

    <#macro userform action method="post" button_content="注册新用户" >
    <form action=${action} method="post">
    <input type="hidden" name="_method" value="${method}">
    <#if method!='delete'>
        <#import "/spring.ftl" as s />   
        <@s.formHiddenInput "user.uuser_id"/>
        <@s.showErrors "<div>" />
        登录名:
        <@s.formInput "user.login_name" "class='loginText'"/>
        <@s.showErrors "<div>" />
         用户名:
        <@s.formInput "user.user_name" />
        <@s.showErrors "<div>" />
        密码：
        <@s.formPasswordInput "user.password"/>
        <@s.showErrors "<div>" />
      <button type="submit">${button_content}</button>
    <#else>
        <#nested>
    </#if>
    </form>
     </#macro> 

对应文件引用即可




    新增post
    <#import "form.ftl" as form/>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>
            form
        </title>
    </head>
    <body>
       <div>
                <@form.userform action="post" button_content="注册新用户"/>
       </div>
    </body>
</html>

    删除代码段
    <@form.userform action="${webRoot}/user/delete/${user.uuser_id}" method="delete" button_content="修改">
         <button  fx="confirm[msg=你确定删除?]" type="submit">删除</button>
     </@form.userform>

    修改代码段
    <@form.userform action="/user/put/${user.uuser_id}" method="put" button_content="修改"/>

spring mvc + junit单元测试 
---

###测试中导入spring中的配置文件，并且使用注解还是比较简单的，类上面加上两个注解即可，测试类内部就可以使用spring的IoC了。

    @RunWith(SpringJUnit4ClassRunner.class)
    @ContextConfiguration(locations = { "/springMVC.xml" })
    public class TestEhcache {
        @Resource(name = "cacheUserController")
        private UserController controller;
        @Test
        public void test(){   .....   }

        .....
        .....
    }

###spring 测试controller，测试页面再也不用启动tomcat了以及写一堆没用的页面了～

spring测试controller的时候使用的是Mock这个测试框架 ，Mock的request和response分别使用：MockHttpServletRequest request; MockHttpServletResponse response。注意测试的时候需要模拟真实的HTTP请求，即每次的request和response对象都是一个新new的。

    request.setRequestURI("/cacheTest/get/2");
    request.setMethod(HttpMethod.GET.name());
    new AnnotationMethodHandlerAdapter().handle(request, response,
                    controller);

直接上例子：

    /**
     * Project Name:justforfun
     * File Name:TestEhcache.java
     * Package Name:com.practice.ehcache
     * Copyright (c) 2013, Thirdtiger.com All Rights Reserved.
     *
     */
    package com.practice.ehcache;

    import javax.annotation.Resource;

    import org.junit.Assert;
    import org.junit.BeforeClass;
    import org.junit.Test;
    import org.junit.runner.RunWith;
    import org.springframework.http.HttpMethod;
    import org.springframework.mock.web.MockHttpServletRequest;
    import org.springframework.mock.web.MockHttpServletResponse;
    import org.springframework.test.context.ContextConfiguration;
    import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
    import org.springframework.ui.Model;
    import org.springframework.web.method.HandlerMethod;
    import org.springframework.web.servlet.ModelAndView;
    import org.springframework.web.servlet.mvc.annotation.AnnotationMethodHandlerAdapter;
    import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter;

    /**
     * com.practice.ehcache.TestEhcache TODO:
     * 
     * @author: 杨洋 Contributor：TODO
     * @since JDK 1.6 2013年11月1日 上午9:36:25
     */
    @RunWith(SpringJUnit4ClassRunner.class)
    @ContextConfiguration(locations = { "/springMVC.xml" })
    public class TestEhcache {
        @Resource(name = "cacheUserController")
        private UserController controller;
        @Resource
        public RequestMappingHandlerAdapter handlerAdapter;
        private static MockHttpServletRequest request;
        private static MockHttpServletResponse response;

        private void init() {
            request = new MockHttpServletRequest();
            request.setCharacterEncoding("UTF-8");
            response = new MockHttpServletResponse();
        }

        @Test
        public void testCache() throws Exception {
            init();
            request.setRequestURI("/cacheTest/get/2");
            request.setMethod(HttpMethod.GET.name());
            new AnnotationMethodHandlerAdapter().handle(request, response,
                    controller);
            init();
            request.setRequestURI("/cacheTest/get/2");
            request.setMethod(HttpMethod.GET.name());
            new AnnotationMethodHandlerAdapter().handle(request, response,
                    controller);
            // handlerAdapter.handle(request, response, new
            // HandlerMethod(controller,
            // "get", String.class, Model.class)); // 执行URI对应的action
            Assert.assertEquals(response.getStatus(), 200);
            // Assert logic
        }

        @Test
        public void testCache2() throws Exception {
            init();
            request.setRequestURI("/cacheTest/get/3");
            request.setMethod(HttpMethod.GET.name());
            new AnnotationMethodHandlerAdapter().handle(request, response,
                    controller);
            init();
            request.setRequestURI("/cacheTest/get/3");
            request.setMethod(HttpMethod.GET.name());
            new AnnotationMethodHandlerAdapter().handle(request, response,
                    controller);
            // handlerAdapter.handle(request, response, new
            // HandlerMethod(controller,
            // "get", String.class, Model.class)); // 执行URI对应的action
            Assert.assertEquals(response.getStatus(), 200);
            // Assert logic
        }
    }

spring mvc ehcache缓存
---

spring mvc使用ehcache

需要用到的jar包

    ehcache-2.7.5.jar(主程序)
    ehcache-spring-annotations-1.2.0.jar(注解)
    guava-r09.jar(依赖)
    slf4j-api-1.6.6.jar(依赖)
    
spring配置文件中需要添加如下内容

    头部
    xmlns:cache="http://www.springframework.org/schema/cache"
    xsi:schemaLocation
    http://www.springframework.org/schema/cache  
    http://www.springframework.org/schema/cache/spring-cache-3.2.xsd  
    
    <!-- 缓存配置 -->
    <!-- 启用缓存注解功能(请将其配置在Spring主配置文件中) -->
    <cache:annotation-driven cache-manager="cacheManager" />

    <!-- Spring自己的基于java.util.concurrent.ConcurrentHashMap实现的缓存管理器(该功能是从Spring3.1开始提供的) -->
    <!-- <bean id="cacheManager" class="org.springframework.cache.support.SimpleCacheManager"> 
        <property name="caches"> <set> <bean name="myCache" class="org.springframework.cache.concurrent.ConcurrentMapCacheFactoryBean"/> 
        </set> </property> </bean> -->

    <!-- 若只想使用Spring自身提供的缓存器,则注释掉下面的两个关于Ehcache配置的bean,并启用上面的SimpleCacheManager即可 -->
    <!-- Spring提供的基于的Ehcache实现的缓存管理器 -->
    <bean id="cacheManagerFactory"
        class="org.springframework.cache.ehcache.EhCacheManagerFactoryBean">
        <property name="configLocation" value="classpath:ehcache.xml" />
    </bean>
    <bean id="cacheManager" class="org.springframework.cache.ehcache.EhCacheCacheManager">
        <property name="cacheManager" ref="cacheManagerFactory" />
    </bean>
    
cache一般用在和数据库交互的地方service

    示例
    /**
     * Project Name:justforfun
     * File Name:NoticeService.java
     * Package Name:com.aft.site.yey.service
     * Copyright (c) 2013, Thirdtiger.com All Rights Reserved.
     *
     */
    package com.aft.site.yey.service;

    import java.util.Date;
    import java.util.HashMap;
    import java.util.LinkedHashMap;
    import java.util.List;
    import java.util.Map;

    import javax.annotation.Resource;

    import org.apache.commons.logging.Log;
    import org.apache.commons.logging.LogFactory;
    import org.springframework.cache.annotation.CacheEvict;
    import org.springframework.cache.annotation.CachePut;
    import org.springframework.cache.annotation.Cacheable;
    import org.springframework.stereotype.Service;

    import com.aft.site.yey.dao.NoticeDao;
    import com.aft.site.yey.entity.Notice;
    import com.app.jdbc.core.ToolUtil;

    /**
     * com.aft.site.yey.service.NoticeService TODO:
     * 
     * @author: yangyang 2013年10月21日 Contributor：TODO
     * @since JDK 1.6
     */
    @Service("yeyNoticeService")
    public class NoticeService {
        private static Log logger = LogFactory.getLog(NoticeService.class);
        @Resource(name = "yeyNoticeDao")
        private NoticeDao dao;

        /**
         * status = 0 指未删除
         * */
        @Cacheable(value = "cacheTest",key="'noticelist'")
        public List<Notice> topN(int begin, int end) {
            LinkedHashMap<String, String> orderby = new LinkedHashMap<String, String>();
            orderby.put("publish_time", "desc");
            Map<String, String> where = new HashMap<String, String>();
            where.put(dao.STATUS + " = ? ", dao.NORMAL_CODE.toString());
            //TODO:delete
            System.out.println("list:");
            logger.info("[list ]");
            return dao.find(where, orderby, begin, end);
        }

        @CacheEvict(value = "cacheTest",key="'noticelist'")
        public void delete(String id) {
            //TODO:delete
            System.out.println("delete:");
            logger.info("delete ");
            dao.delete(id, false);
        }

        @CacheEvict(value = "cacheTest", allEntries = true)
        public void save(Notice notice) {
            notice.setRowid(ToolUtil.getUUID());
            notice.setStatus(dao.NORMAL_CODE);
            notice.setPublish_time(new Date());
            // TODO:yeyid的获得方式
            notice.setYey_id("123");
            dao.insert(notice);
            //TODO:delete
            System.out.println("save:");
            logger.info("save ");
        }

        public Notice get(String id) {
            return dao.findById(id);
        }

        //@CachePut(value = "cacheTest",key="#notice.getRowid()")
        public void update(Notice notice) {
            Map<String, String> set = new HashMap<String, String>();
            LinkedHashMap<String, String> where = new LinkedHashMap<String, String>();
            set.put("title", notice.getTitle());
            set.put("author", notice.getAuthor());
            set.put("content", notice.getContent());
            where.put(dao.getIdColumnName() + "=?", notice.getRowid());
            dao.update(set, where);
            System.out.println("update:");
            logger.info("update ");
        }

    }

###非常详细的spring mvc和cache的使用博客
http://www.ibm.com/developerworks/cn/opensource/os-cn-spring-cache/

###官网文档
http://docs.spring.io/spring/docs/3.1.0.M1/spring-framework-reference/html/cache.html

###ehcache介绍
http://my.oschina.net/coolfire368/blog/123377

###spring mvc整合 ehcache
http://blog.csdn.net/jadyer/article/details/12257865

###简单讲解

cache主要*注解*使用：*@Cacheable，@CacheEvict，@CachePut*

缓存是这样的，取值时在方法(A)*调用前*查一下缓存中是否有目标值，缓存存在的话直接从缓存中拿出**不再去执行方法(A)**,这也是最基本的*@Cacheable*的概念;

缓存中有值需要更新怎么办？使用@CacheEvict来更新，这个注解的意思是删除掉缓存里面的某个值，从而达到更新缓存的效果。关于缓存更新，例如，取topN个对象，第一次取的时候比如是前1～10个，缓存中存这1～10的**一个集合对象**，第二次取的时候直接从缓存中拿，这没问题，现在是这样的，假设数据库中删除了1～10个元素中的任意一个值，这样**数据库中的topN与缓存中的topN**就不同步了，下次你在前台取topN的时候，因为缓存里面有这个对象，根据之前的介绍（取值时在方法(A)*调用前*查一下缓存中是否有目标值，缓存存在的话直接从缓存中拿出**不再去执行方法(A)**），方法A被略过，查的值不是真正的topN了，因此需要在add或者delete之后删除掉原来的缓存，保持数据一致。其他情景请自行考虑。

根据缓存的特性，如何做到既要保证方法被调用，又希望结果被缓存呢？直接使用*@CachePut*，他与@Cacheable的区别就在与方法是会被执行的。

注解里面属性解释,@Cacheable 与@CachePut一样， @CacheEvict还有和删除有关的两个属性：

1. value：缓存的名称，在spring配置文件中定义，必须指定至少一个 
    * 例如：@Cacheable(value=”mycache”) 或者
@Cacheable(value={”cache1”,”cache2”} 

2. key：缓存的key，(缓存是键值对儿)可以为空，如果指定要按照 SpEL 表达式编写，如果不指定，则缺省按照方法的所有参数进行组合 
    * 例如：
@Cacheable(value=”testcache”,key=”#userName”)
    * 使用字符串"'sss'"
    * 调用对象getName方法key=”#userName.getName()”

3. condition：缓存的条件，可以为空，使用SpEL 编写，返回 true 或者 false，只有为 true 才进行缓存
    * 例如：
@Cacheable(value=”testcache”,condition=”#userName.length()>2”) 

4. allEntries:是否清空所有缓存内容，缺省为 false，如果指定为 true，则方法调用后将立即清空**所有**缓存 
    * 例如：
@CachEvict(value=”testcache”,allEntries=true)
5. beforeInvocation:是否在方法执行前就清空，缺省为 false，如果指定为 true，则在**方法还没有执行的时候就清空缓存*，缺省情况下为false，这样如果方法执行抛出异常，则不会清空缓存
    * 例如：
@CachEvict(value=”testcache”，beforeInvocation=true) 
