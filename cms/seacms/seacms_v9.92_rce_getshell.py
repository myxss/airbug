# coding=UTF-8
# Author:w8ay
# Name:测试DEMO
'''
name: seacms<=9.92前台getshell
referer: https://xz.aliyun.com/t/6191
author: Lucifer
description: https://xz.aliyun.com/t/6191
'''
import HackRequests

def poc(arg,**kwargs):
    header = '''
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    '''
    hack = HackRequests.hackRequests()
    payload = "/data/mysqli_error_trace.php"
    shell_url = arg + payload
    #print(shell_url)
    hh = hack.http(shell_url)
    #print(hh.status_code)
    if (hh.status_code == 200):
        result = {
        "name": "seacms<=9.92前台getshell",  # 插件名称
        "content": "seacms<=9.92前台getshell",  # 插件返回内容详情，会造成什么后果。
        "url": arg,  # 漏洞存在url
        #"log": req4.log,
        "tag": "rce"  # 漏洞标签
        }
        #print('ok')
        return result
        
if __name__ == "__main__":
    pass
