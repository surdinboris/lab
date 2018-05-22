import os, sys
import socket
import random
from struct import pack, unpack
from datetime import datetime as dt

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import Integer, IpAddress, OctetString

ip='10.148.38.183'
community='public'
nval='1.3.6.1.4.1.6050.1.2.26.1.8.1'
nlists=[int(x) for x in nval.split(".")]
value=tuple(nlists)
generator = cmdgen.CommandGenerator()
comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
transport = cmdgen.UdpTransportTarget((ip, 161))

real_fun = getattr(generator, 'nextCmd')

res = (errorIndication, errorStatus, errorIndex, varBinds)\
    = real_fun(comm_data, transport, value)
print(res)

if not errorIndication is None  or errorStatus is True:
       print("Error: %s %s %s %s" % res)
else:
       print("%s" % varBinds)
