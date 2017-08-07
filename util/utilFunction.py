# -*- coding: utf-8 -*-
import requests
from lxml import etree
from util.LogHandler import LogHandler
from util.WebRequest import WebRequest

logger = LogHandler(__name__)

def robustCrawl(func):
    def decorate(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            logger.info(u"sorry,主区出错。原因:")
            logger.info(e)

    return decorate

def verifyProxyFormat(proxy):
    import re
    verify_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}'
    return True if re.findall(verify_regex,proxy) else False

def getHtmlTree(url,**kwargs):
    header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    wr = WebRequest()
    html = wr.get(url=url,header=header).content
    return etree.HTML(html)

def validUsefulProxy(proxy):
    proxies = {"https": "https://{proxy}".format(proxy=proxy)}
    try:
        r = requests.get('https://www.baidu.com', proxies=proxies, timeout=40, verify=False)
        if r.status_code == 200:
            logger.debug('%s is ok' % proxy)
            return True
    except Exception as e:
        logger.info(e)
        return False

