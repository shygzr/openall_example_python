#!/usr/bin/evn python
# coding=utf-8

from bottle import default_app, get, run
from beaker.middleware import SessionMiddleware


# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

@get('/')
def callback():
    return '济南大学智慧校园开放平台-----python应用Demo-----bottle框架'

# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='0.0.0.0', port=8080, debug=True, reloader=True)