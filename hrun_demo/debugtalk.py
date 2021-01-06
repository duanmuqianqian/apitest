import time
import random
import requests

import os

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def hook_up(request=None):
    # print("输出request:{}".format(request))
    print("前置操作：setup!")

def hook_down(response=None):
    print("后置操作：teardown!")

def get_user():
    return [
        {"username": "13817441237"}
    ]

# #用于在读取文件中的 cookies
# COOKIES_PATH = r'xxx/xxx/cookies'
#
# def generate_cookies():
#     if (not os.path.exists(COOKIES_PATH)):
#         # cookies 文件不存在 或 最后修改时间超过 3600 秒 (1小时) 则重新登录刷新 cookies
#         runner = HttpRunner()
#         runner.run(r'hrun_demo/har/login.yml')
#     with open(COOKIES_PATH, 'r') as f:
#         cookies: str = f.read()
#     return cookies
#  #用于在 login.yaml 中保存 cookies 内容到文件
# def teardown_saveCookies(response: requests.Response):
#     """保存 cookies 到文件给其他 api 调用"""
#     cookies: dict = response.cookies
#     foo: list = []
#     # 遍历 cookies 拆分 dict 并拼接为特定格式的 str
#     # 如: server=xxxxx; sid=xxxxxx; track=xxxxx;
#     for k, v in cookies.items():
#         foo.append(k + '=' + v + '; ')
#     bar: str = "".join(foo)
#     with open(COOKIES_PATH, 'w') as f:
#         f.write(bar)


#定义发私信内容
def get_content():
    num=str(random.randint(1,999999))
    print('哈哈'+num)
    return ('哈哈'+num)

#定义用户名、密码
def get_userinfo():
    #嵌套字典的列表
    user_info = [
        {"title": "正常登录", "username": "13817441237", "password": "65618383e140db353d238a14a1fdb2f5",
         "isLogin": 1, "status_code": 200, "content": "body.result", "contain_msg": "token",},
        {"title": "密码错误", "username": "13817441237", "password": "1234567",
         "isLogin": 0, "status_code": 200, "content": "body.error.text", "contain_msg": "密码格式错误"},
        {"title": "账号错误", "username": "keyou111", "password": "65618383e140db353d238a14a1fdb2f5",
         "isLogin": 0, "status_code": 200, "content": "body.error.text", "contain_msg": "帐号不存在"},
        {"title": "用户名为空", "username": "", "password": "65618383e140db353d238a14a1fdb2f5",
         "isLogin": 0, "status_code": 200, "content": "body.error.text", "contain_msg": "接口传入参数不完整或有误"},
        {"title": "密码为空", "username": "13817441237", "password": "",
         "isLogin": 0, "status_code": 200, "content": "body.error.text", "contain_msg": "接口传入参数不完整或有误"}

    ]
    return user_info

#getTimeline
def get_timeline():
    time_line=[
        {"title": "正常获取第一页数据","page": 1, "puid": "52498468",
         "type": "FOLLOW_TIMELINE", "lastCommentTime": "0", "status": 200, "msg": "success"},
        {"title": "正常获取第二页数据", "page": 2, "puid": "52498468",
         "type": "FOLLOW_TIMELINE", "lastCommentTime": "1606017759782", "status": 200, "msg": "success"},
        {"title": "不传页码", "page":"", "puid": "52498468",
         "type": "FOLLOW_TIMELINE", "lastCommentTime": "0", "status": 200, "msg": "success"},
        {"title": "不传puid", "page": 1, "puid": "",
         "type": "FOLLOW_TIMELINE", "lastCommentTime": "0", "status": 200, "msg": "success"},
        {"title": "不传type", "page": 1, "puid": "52498468",
         "type": "", "lastCommentTime": "0", "status": 500, "msg": "未知异常"},
    ]
    return time_line

#获取改头像的数据
def get_headerinfo():
    header_info =[
        {"title": "正常传递头像数据", "headerPath": "user/182/35138216940182/35138216940182-1609247671.png",
         "status": 200, "msg": "为了您和他人的安全与隐私，头像（昵称）审核中，预计最迟将会在1工作日内完成审核"},
        {"title": "不传递头像数据", "headerPath": "",
         "status": 500, "msg": "接口传入参数不完整或有误"}

    ]
    return header_info

#更改性别
def get_gender():
    gender=random.randint(0, 2)
    # print(gender)
    return gender


if __name__ == '__main__':
    hook_up()
    hook_down()
    get_user()
    # get_last_content()
    get_content()
    get_userinfo()
    # #获取cookie
    # generate_cookies()
    # #保存cookie
    # teardown_saveCookies()
    get_timeline()
    get_headerinfo()
    get_gender()



