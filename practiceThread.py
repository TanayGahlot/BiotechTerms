#oggpnosn
#hkhr

import threading 
from time import sleep,ctime 
message = []
def loop(nloop, nsec):
	message.append('Start loop '+str(nloop)+'at '+ctime())
	sleep(nsec)
	message.append('End loop'+str(nloop)+'at'+ctime())

	
loops = (4,2)
threads = []

for i in range(len(loops)):
	threads.append(threading.Thread(target=loop,args=(i,loops[i])))
	
for i in range(len(loops)):
	threads[i].start()

for i in range(len(loops)):
	threads[i].join()

print message
print 'all this end at', ctime()

def bar(text):
	print text


