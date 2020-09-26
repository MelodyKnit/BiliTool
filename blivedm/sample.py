# -*- coding: utf-8 -*-

import asyncio
from blivedm.MyBLiveClient import MyBLiveClient


async def main(uid):
    # 参数1是直播间ID
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(uid, ssl=True)
    future = client.start()
    try:
        # 5秒后停止，测试用
        # await asyncio.sleep(5)
        # future = client.stop()
        # 或者
        # future.cancel()

        await future
    finally:
        await client.close()


def run(uid):
    asyncio.get_event_loop().run_until_complete(main(uid))
