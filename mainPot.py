#!/usr/bin/python
import socket
import time
import pygeoip
import threading
import os
import queue

q = queue.Queue()
num_of_threads = 5
jobs_to_do = [1, 2, 3, 4, 5, 6, 7]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def geo_locate(tgt):
    try:
        gi = pygeoip.GeoIP('opt/GeoIP/Geo.dat')
        try:
            rec = gi.record_by_addr(tgt)
            print '[+] {}'.format(tgt)
        except:
            print '[-] couldnt identify the target'
        try:
            city = rec['city']
            print '[+] {}'.format(city)
        except:
            print '[-] Couldnt identify the city'
        try:
            country = rec['country_name']
            print '[+] {}'.format(country)
        except:
            print '[-] Couldnt identify the country'
        try:
            longe = rec['longitude']
            lat = rec['latitude']
            print 'LON: {} / LAT: {}'.format(longe, lat)
        except:
            print '[-] Couldnt geo locate the target'
    except:
        pass


def http_pot(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 80))
    print '[*] HTTP pot LISTENING....'
    while True:
        s.listen(6)

        soc, addr = s.accept()
        if len(str(geo_locate(tgt=addr[0]))) != 0 and str(geo_locate(addr[0])) != None:
            print 'HTTP HoneyPot Victim: ', addr[0], geo_locate(addr[0]), '\n'
        time.sleep(1)

        soc.close()


def ssh_pot(host):
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 22))
    print '[*] SSH pot LISTENING.....\n'
    while True:
        s.listen(6)
        soc, addr = s.accept()
        print '[+] SSH pot victim: ', addr[0], '\n'
        soc.close()


def ftp_pot(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 21))
    print '[*] FTP pot is LISTENING...\n'
    while True:
        s.listen(5)
        sock, addr = s.accept()
        print '[+] FTP pot victim : ', addr[0], '\n'
        sock.close()


def postgresql_pot(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 5432))
    print '[*] POSTGRESQL pot is LISTENING...\n'
    while True:
        s.listen(5)
        sock, addr = s.accept()
        print '[+] POSTGRESQL pot victim : ', addr[0], '\n'


def mysql_pot(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 3306))
    print '[*] MYSQL pot is LISTENING....\n'
    while True:
        s.listen(5)
        sock, addr = s.accept()
        print '[+] MYSQL pot victim : ', addr[0]
        sock.close()


def create_worker():
    for threads in range(num_of_threads):
        t = threading.Thread(target=work, args=())
        t.daemon = True
        t.start()


host = '127.0.0.1'


def Ishell():
    while True:
        x = os.getlogin() + '@' + os.uname()[1] + ':~# '
        l = raw_input(str(x))
        if l == 'clear':
            os.system('clear')
        if l == 'quit':
            exit(0)


def work():
    x = q.get()
    if x == 1:
        http_pot(host)
    if x == 2:
        ftp_pot(host)
    if x == 3:
        ssh_pot(host)
    if x == 4:
        postgresql_pot(host)
    if x == 5:
        mysql_pot(host)
    if x == 6:
        Ishell()

    q.task_done()


def create_jobs():
    for job in jobs_to_do:
        q.put(job)
    q.join()


def main():
    create_worker()
    create_jobs()


if __name__ == '__main__':
    main()
