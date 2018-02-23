#!/usr/bin/env python
import pygeoip
from scapy.all import *


def monitor(pkt):
    try:
        gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

        if pkt.haslayer(IP):

            ip_ = pkt.getlayer(IP).src
            try:
                rec = gi.record_by_addr(ip_)
                city = rec['city']
                country = rec['country_name']
                longe = rec['longitude']
                lat = rec['latitude']


                print('[+] From ' + str(ip_) + ' : ' + str(pkt.ttl) + ' || ' + str(country)+' / '+str(city)+' || '\
                    +'LAT: '+str(lat)+' LONGE: '+str(longe))
            except:
                print ip_
    except:
        pass


def main():
    sniff(prn=monitor, store=0)


if __name__ == '__main__':
    main()
