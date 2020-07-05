Week02学习笔记

这一周学习难度加大，感觉真的有点跟不上；并且和上周的作业有重叠和连贯性，因此周日看完视频后又回头开始看Scarpy的用法。
先回顾Scrapy的实现方式：
1.首先通过Scrapy startporoject spiders 创建:
New Scrapy project 'spiders', using template directory '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/scrapy/templates/project', created in:
    /Users/allen/pythontrain/spiders

You can start your first spider with:
    cd spiders
    scrapy genspider example example.com

2. 进入目录建立 scrapy genspider movies douban.com 创建movies 的爬虫。
Created spider 'movies' using template 'basic' in module:
  spiders.spiders.movies

3. 通过scrapy 将之前的Requests的爬虫更简洁的修改和实现，同时通过XPath进行实现跟着老师的视频实现。。


到这周的视频更加的深入，自己也是尝试理解和模拟；
1. 异常的捕获和处理，为提升程序的健壮性，通常使用Try...Except 语法来捕获异常，
   另外常用的的异常类型主要有：1 Lookuperror下的IndexError 和 KeyError；2 IOError;3 NameError;4 TypeError；5 AttributeError; 6 ZeroDivisionError。
  并且通过pretty_errors 将异常更清晰的显示。
  另外也告知了魔术方法的使用，其也是python的特色。

2. 通过PyMySQL 进行数据库操作
    先安装MySQL、然后安装PyMySql的连接器;
    将mysql的链接信心等都写入dbinfo中；
    开始-创建connection-获取cursor-CRUD-关闭cursor-关闭conn-结束。
3. 反爬虫：通过模拟浏览器的头部信息来规避，通过User-Agent、Referer Host;
          带Cookies，通过Post方式将用户名、密码验证信息模拟交给服务器。

4. 安装WebDriver,并安装相关驱动；通过Browser=webdriver.Chrome() 模拟浏览器行为。
   同时通过验证码进行灰度和不断识别得到，并传值进去。

5. 通过Proxyspider完成爬虫中间件的作用并，这一块需要加深理解。

注意：在git checkout 2e 的时候遇到文件change的问题，最后通过git reset --hard origin/master

因为前次作业没有实现猫眼电影的爬虫，因此这周难度加大也是没能力实现，只有先学到基本知识再继续学习。