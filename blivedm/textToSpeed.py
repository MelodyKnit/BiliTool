from requests import Session
from playsound import playsound


class Speech:
    def __init__(self, **kwargs):
        self.error = True
        self.session = Session()
        self.main_url = 'https://www.zaixianai.cn/'
        self.url = 'https://www.zaixianai.cn/Api_getVoice'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.params = dict({
            'content': str(),
            'volume': 20,           # 音量
            'speech_rate': -100,    # 语速
            'voice': 'Aixia',       # 声音
            '_token': str()
        }, **kwargs)
        self.reset()

    def reset(self):
        self.session.get(self.main_url, headers=self.headers)

    def get(self, text):
        self.params['content'] = text
        obj = self.session.get(self.url, headers=self.headers, params=self.params).json()
        obj['data']['file_url'] = f'https://www.zaixianai.cn/voice/{obj["data"]["file_name"]}'
        return obj

    def play(self, text):
        try:
            self.error = True
            playsound(self.get(text)["data"]['file_url'])
        except :
            if self.error:
                self.reset()
                self.play(text)
            self.error = False


def file_rw(path, mode, val=None):
    with open(path, mode=mode) as file:
        if val and mode == 'w':
            file.write(str(val))
        else:
            return file.read()


