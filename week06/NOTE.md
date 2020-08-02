Week06学习笔记
Django 特点
1.采⽤MTV框架
    Model）模型
    （Template）模板
    （Views）视图
2.强调快速开发和代码复⽤DRY (Do Not Repeat Yourself)
3. 组件丰富：
    ORM (对象关系映射) 映射类 构建数据模型
    URL 支持正则表达式
    模板可继承
    内置用户认证，提供用户认证和权限功能
    admin 管理系统
    内置表单模型、Cache 缓存系统、国际化系统等

Django 最新版本3.0  这次安装了2.2.13（LTS） 
安装方法
$ pip install --upgrade django==2.2.13
通过python3 检验版本
    >>> import django
    >>> django.__version__

创建Django 应用程序
$ python manage.py help 查看具体功能
$ django-admin startproject MyDjango 创建项目
$ python manage.py startapp index    创建应用程序
$ python manage.py runserver         本地启动Django

$ python manage.py runserver 0.0.0.0:80  提供外部访问的启动模式
$ CONTROL-C   完成调试后停止应用方法

Django 的配置文件包括：
    项目路径
    密钥
    域名访问权限
    App 列表
    静态资源
    模板文件
    数据库配置
    缓存
    中间件

URL调度器 url.py 
   urls.py 文件中写入urlpatterns 列表：
    从URL 路由到视图(views) 的映射功能
    过程中使用Python 模块：**URLconf**(URL configuration)，也叫URLconf

    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('index.urls')),
        ]

view 视图
    HTTP 状态码200，请求已成功被服务器接收
    HTTP 状态码302，重定向Admin 站点的URL
    HTTP 状态码301，永久重定向Admin 站点URL
    HTTP 状态码400，访问的页面不存在或者请求错误
    HTTP 状态码404，页面不存在或者网页的URL 失效
    HTTP 状态码403，没有访问权限
    HTTP 状态码405，不允许使用该请求方式
    HTTP 状态码500，服务器内容错误
