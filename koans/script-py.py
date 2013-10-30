import threading

import os
p = os.popen('node -v',"r")
while 1:
    threading.Timer(5.0).start()
    line = p.readline()
    if not line: break
    print line



def printit():
  threading.Timer(5.0, printit).start()
  print "Hello, World!"


#printit()
