Week03学习笔记

1. Scrapy 并发参数优化原理
    Scrapy 和requests 区别在于多任务 异步和同步的区别
    Scrapy 默认16个并发请求数量，可以CONCURRENT_REQUESTS = 32;但并不是越大越好；
    还可设置通过下载延迟，可以通过DOWNLOAD_DELAY = 3设置，防止爬取过快导致被封
    同时还有更细致的设置，可以通过PER_DOWMAIN和PER_IP设置限制，控制底层工作。

   Scrapy 是使用的Twisted 模型， 其实异步编程框架，任务之间互相独立、用于大量I/O密集操作。
   Twisted 内部形成事件的循环，Reactor Loop内部实现循环

2. 多进程：进程的创建
    多进程、多线程、协程的目的都是希望尽可能的多处理任务；
    产生新进程可以用：os.fork() multiprocessing.Process()
    多进程程序调用，引入多进程解决性能问题，要注意调试技巧

3. 多进程：使用队列实现进程间的通信
    为什么不能使用变量作为进程间共享数据 主要共享方式：队列 管道 共享内存
    其中队列的共享方式应用最高
     Put  Get（Blocked TimeOut）
    进程安全：同时写的时候，可以进行资源抢占：加锁机制
    
    管道、共享内存 方式，比队列更原始 pipe
    多进程，锁机制解决资源抢占 multiprocessing 的lock（）函数

4. 多进程的进程池
    Pool类表示一个工作进程池，如果要启动大量的子进程，可以用进程池方式批量创建子进程。multiprocessing.pool
    要注意Join函数放置的位置，不要造成死锁
    可以灵活的使用with描述符、Map的方式来更灵活使用。