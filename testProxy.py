import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5000/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5000/delete/?proxy={}".format(proxy))


def spider():
    proxy = get_proxy()
    header = {}
    header["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
    r = requests.get('http://www.zhihu.com/people/tian-yuan-dong/followers', headers=header,proxies={"http": "http://{}".format(proxy)})
    if r.status_code == 200:
        print r.content
        return True
    else:
        print "error"
        print r.content
        delete_proxy(proxy)

spider()
