#-*- coding=utf-8 -*-

import requests
import re
import getpass

url = "http://ngw.bupt.edu.cn/login"
logout_url = "http://ngw.bupt.edu.cn/logout"
s = requests.Session()


# 获得网络登录状态
def get_gw_state():
    r = s.get(url)
    pattern = "logout"
    match = re.search(pattern, r.text, re.I)
    if not match:
        print "当前状态：您还未登陆网关"
        return False
    else:
        print "当前状态：您已经登陆网关"
        return True


# 登出
def logout():
    r= s.get(logout_url)
    get_gw_state()


# 登出
def login():
    option = raw_input("是否使用原账号登陆？[y/n]")
    if option == 'y' or option == 'Y':
        username = ''
        userpass = ''
        line = ''
    else:
        username = raw_input("请输入您的用户名")
        userpass = getpass.getpass("请输入您的密码")
        line = ''
        operator = raw_input("请输入运营商线路，默认为校园网，中国联通请输入1，中国移动请输入2，中国电信请输入3")
        if operator == 1:
            line = 'CUC-BRAS'
        elif operator == 2:
            line = 'CMCC-BRAS'
        elif operator == 3:
            line = 'CT-BRAS'
    payload = {'user': username, 'pass': userpass, 'line': line}
    r = s.post(url, data=payload)
    get_gw_state()


if __name__ == "__main__":
    if not get_gw_state():
        option = raw_input("是否登陆网关？[y/n]")
        if option == 'y' or option == 'Y':
            login()
        else:
            print "您并未选择登陆网关，当前处于断网状态"
    else:
        option = raw_input("是否登出网关？[y/n]")
        if option == 'y' or option == 'Y':
            logout()
        else:
            print "您并未选择登出网关，请继续使用网络"
