# encoding: utf-8

import time, datetime
import requests
import json
import werobot


def log(*args, **kwargs):
    print(args, kwargs)


start_time = datetime.datetime(2019, 12, 21, 11, 40, 0)
print('Program not starting yet...')
while datetime.datetime.now() < start_time:
    time.sleep(1)
    print(datetime.datetime.now())
print('Program now starts on %s' % start_time)
print('Executing...')


robot = werobot.WeRoBot(token='nicoleacademy')
robot.config['APP_SECRET'] = '84c67ca9b0df9b5ab6d21b89b4b4f2af'
robot.config['APP_ID'] = 'wx4727d668a1c1b9dd'
client = robot.client

openid_dic = client.get_followers()              # 拉取 openid
openid_list = openid_dic['data']['openid']
log('openid_list', openid_list)

access_token = client.get_access_token()
log('access token', access_token)

for e in openid_list:
    user_info = client.get_user_info(e)
    log('user_info', user_info)


def post_data(openid, course, stu_name, ass_token):
    data = {
        "touser": openid,
        "template_id": "Ym6QUQkqlWyeAtVNcUIAk7TPjD35WtNN4dMVHOeX_9Y",  # 模板ID
        "data": {
            "first": {
                "value": "你好，以下课程将在半小时后开始",
                "color": "#173177"
            },
            "keyword1": {
                "value": course,
                "color": "#173177"
            },
            "keyword2": {
                "value": stu_name,
                "color": "#173177"
            },
            "remark": {
                "value": "若因故无法参加，请及时联系老师。",
                "color": "#173177"
            },
        }
    }
    json_template = json.dumps(data)
    # access_token = self.get_token()
    # print("access_token--", access_token)
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + ass_token
    try:
        response = requests.post(url, data=json_template, timeout=50)
        # 拿到返回值
        errcode = response.json().get("errcode")
        log("test--", response.json())
        if (errcode == 0):
            log("模板消息发送成功")
        else:
            log("模板消息发送失败")
    except Exception as e:
        log("test++", e)


post_data('oLGmWwkDtrc82LpDYWp3q8y7v6d0', '编程', 'Rocky', access_token)
post_data('oLGmWwt6e_QtMcZfQR4l9xN1SdN4', '英文进阶', 'server test', access_token)
post_data('oLGmWwjOKkGVYY1dCJfTnrFvi8RA', '衔接班', 'server test', access_token)
