# Send UDP broadcast packets

MYPORT = 10000

import sys, time, socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
    data = repr(time.time()) + '\n'
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)