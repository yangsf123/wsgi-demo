# 导入python内置的WSGI server
from wsgiref.simple_server import make_server

def application(env, start_response):
    response_body = [
            '%s: %s' % (key, value) for key, value in sorted(env.items())
    ]
    response_body = '\n'.join(response_body) # 由于下面将Content-Type设置为text/plain,所以'\n'在浏览器中会起到换行的作用

    status = '200 OK'
    response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

# 中间件
class Upperware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, env, start_response):
        for data in self.wrapped_app(env, start_response):
            yield data.upper()


wrapped_app = Upperware(application)

httpd = make_server('localhost', 8051, wrapped_app)

httpd.serve_forever()

print('end')
