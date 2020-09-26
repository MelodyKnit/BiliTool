
from threading import Timer
from pynput.keyboard import Listener
from blivedm.textToSpeed import file_rw
FILENAME = 'liveID'


def save():
    uid = input('请输入您的直播间id\n> ')
    file_rw(FILENAME, 'w', uid)
    return uid


def login():
    try:
        return file_rw(FILENAME, 'r')
    except FileNotFoundError:
        return save()


