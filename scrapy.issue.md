scrapy
===

安装
---
    sudo apt-get install gcc python-virutalenv python-dev libxml2-dev
    libxslt-dev

    pip install Scrapy

抓取
---
    scrapy crawl douban_book


selector
---
    样例
    <html>
         <head>
             <base href='http://example.com/' />
             <title>Example website</title>
         </head>
         <body>
             <div id='images'>
                 <a href='image1.html'>Name: My image 1 <br />
                    <img src='image1_thumb.jpg' /></a>
                 <a href='image2.html'>Name: My image 2 <br />
                    <img src='image2_thumb.jpg' /></a>
                 <a href='image3.html'>Name: My image 3 <br />
                    <img src='image3_thumb.jpg' /></a>
                 <a href='image4.html'>Name: My image 4 <br />
                    <img src='image4_thumb.jpg' /></a>
                 <a href='image5.html'>Name: My image 5 <br />
                    <img src='image5_thumb.jpg' /></a>
             </div>
         </body>
    </html>

    xpath
        选择属性使用@
        选择节点文字text()
        选择某节点href属性@href
    css
        选择属性使用::
        选择节点文字::text
        选择某节点href属性::attr(href)

    xpath

        sel.xpath('//title/text()') -- [<Selector (text) xpath=//title/text()>]
        sel.xpath('//title/text()').extract() -- [u'Example website']
        sel.xpath('//base/@href').extract() -- [u'http://example.com/']
        sel.xpath('//a[contains(@href, "image")]/@href').extract()
            [u'image1.html', u'image2.html', u'image3.html',
             u'image4.html', u'image5.html']
        sel.xpath('//a[contains(@href, "image")]/img/@src').extract()
            [u'image1_thumb.jpg', u'image2_thumb.jpg', u'image3_thumb.jpg',
             u'image4_thumb.jpg', u'image5_thumb.jpg']

    css

        sel.css('title::text').extract() -- [u'Example website']
        sel.css('base::attr(href)').extract() -- [u'http://example.com/']
        sel.css('a[href*=image]::attr(href)').extract()
        [u'image1.html', u'image2.html', u'image3.html', u'image4.html', u'image5.html']
        sel.css('a[href*=image] img::attr(src)').extract()
            [u'image1_thumb.jpg', u'image2_thumb.jpg', u'image3_thumb.jpg',
             u'image4_thumb.jpg', u'image5_thumb.jpg']
