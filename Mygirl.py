import requests
import itchat  # 这是一个用于微信回复的库
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'  # 这个key可以直接拿来用


# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

# 注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By机器人13']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply


# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=True)
itchat.run()