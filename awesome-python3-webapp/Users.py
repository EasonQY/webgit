import asyncio,sys
import orm
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop=loop,port=3306,user='root',password='quyi0816',db='awesome')
    u = User(name='Test',email='test@example.com',passwd='1234567878',image='about:blank',id='110')
    await u.save()

# 把协程丢到EventLoop中执行
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()