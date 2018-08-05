import logging; logging.basicConfig(level = logging.INFO)
# 日志输出，可以设置输出日志的等级，日志保存路径、文件回滚等，相比print有以下优点：
# 1.可以通过设置不同的日志等级，在release版本中输出重要信息，而不必显示大量的调试信息
# 2.可以由开发者决定将信息输出到什么地方，以及怎么输出
import asyncio, os, json, time
#asyncio主要用于服务器端，实现单线程并发IO操作，实现了TCP,UDP,SSL等协议
from datetime import datetime
from aiohttp import web
# aiohttp是基于asyncio实现的HTTP框架

def index(request):
	return web.Response(body = b'<h1>Awesome</h1>')

@asyncio.coroutine
# 装饰器，实现协程工作，把一个generator标记为coroutine类型，然后在内部用yield from调用另一个coroutine实现异步操作
def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()