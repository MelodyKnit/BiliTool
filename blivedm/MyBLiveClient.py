# -*- coding: utf-8 -*-

from blivedm import blivedm
from blivedm.textToSpeed import Speech
from blivedm.blivedm import SuperChatDeleteMessage
video = Speech(volume=100)
print('程序启动成功，欢迎使用本程序')
video.play('程序启动成功，欢迎使用本程序')


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)
    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        video.play(f"感谢现在还在观看的{popularity}位亲爱的观众老爷")

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        video.play(f"亲爱的{danmaku.uname}说：{danmaku.msg}")
        # print(f'{danmaku.uname}：{danmaku.msg}')

    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        print(gift.coin_type, gift.total_coin)
        video.play(f"感谢{gift.uname}赠送的{gift.num}个{gift.gift_name}")
        # print(f'{gift.uname} 赠送{gift.gift_name}x{gift.num} （{gift.coin_type}币x{gift.total_coin}）')

    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')

