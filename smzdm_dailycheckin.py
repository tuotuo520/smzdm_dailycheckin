#coding=utf-8

import json
import sys
import requests


username = '' #邮箱
password = ''#密码



class SMZDMDaliyException(Exception):
    def __init__(self, req):
        self.req = req


    def __str__(self):
        return str(self.req)

class SMZDMDailycheckin(object):
    BASE_URL = 'https://zhiyou.smzdm.com/'
    LOGIN_URL = BASE_URL + 'user/login/ajax_check'
    CHECKIN_URL = BASE_URL + 'user/checkin/jsonp_checkin'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()



    def checkin(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'host' : 'zhiyou.smzdm.com',
        'referer' : 'https://www.smzdm.com/',
        }
        params = {
            'username': self.username,
            'password': self.password,
        }

        r = self.session.get(self.BASE_URL, headers=headers)
        r = self.session.post(self.LOGIN_URL, data=params, headers=headers)
        r = self.session.get(self.CHECKIN_URL, headers=headers)

        if r.status_code != 200:
            raise SMZDMDaliyException(r)#显示引发异常，后面不执行

        data = r.text
        jdata = json.loads(data)


        return jdata

    if __name__ == '__main__':
        if username is '' or password is '':
            print('username or password is required')
            sys.exit()


try:
    smzdm = SMZDMDailycheckin(username, password)
    result = smzdm.checkin()
except SMZDMDaliyException as e:
    print('fail', e)
except Exception as e:
    print('fail', e)
else:
    print('success', result)
