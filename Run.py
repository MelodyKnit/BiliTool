# -*- coding: utf-8 -*-

try:
    from blivedm.sample import run
    from config.edit import login
    if __name__ == '__main__':
        run(login())
        # 输入直播间id号

except ModuleNotFoundError as error:
    print(f'安装"{error.name}"库')
    try:
        from os import system
        system(f'pip install {error.name}')
        system(f'python {__file__}')
    except Exception as error:
        print(f'\033[0;31m{error} \033[0m!')
