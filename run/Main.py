
import sys
from multiprocessing import Process

sys.path.append('../')

from api.ProxyApi import run as ProxyApiRun
from schedule.ProxyValidSchedule import run as ValidRun
from schedule.ProxyRefreshSchedule import run as RefreshRun


def run():
    p_list = list()
    p1 = Process(target=ProxyApiRun, name='ProxyApiRun')
    p_list.append(p1)
    p2 = Process(target=ValidRun, name='ValidRun')
    p_list.append(p2)
    p3 = Process(target=RefreshRun, name='RefreshRun')
    p_list.append(p3)
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

if __name__ == '__main__':
    run()