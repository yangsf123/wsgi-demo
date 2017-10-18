# WSGI(Web Server Gateway Interface)

WSGI:是一个python标准(协议)，由PEP 3333描述。
用来规定Web Server如何与python应用程序通信。

如果一个Python应用程序(或框架，如Django,Flask)符合WSGI标准，那么它可以在任何符合WSGI标准的Server上运行(比如Apache)

这是一个规范，描述了web server如何与web application交互，web application如何处理请求。WSGI既要实现web server，也要实现web application

WSGI server所做的工作仅仅是将从客户端收到的请求传递给WSGI application，然后将WSGI application的返回值作为相应传给客户端。
