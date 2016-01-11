#open path

import os
from glob import iglob
#import shutil


dirpath = '/Users/admin/Desktop/VR Training Logs'

dirList = os.listdir(dirpath)

for fname in dirList:

	print(fname)
	path = dirpath +'/'+fname 
	if os.path.isdir(path):
		#path = r'/Users/admin/Desktop/VR Training Logs/Kotaro'
		with open(os.path.join(dirpath,fname+'.txt'), 'w') as destination:
		#with open('/Users/admin/Desktop/VR Training Logs'+'/'+fname+'.txt', 'wb') as destination:
			print(os.path.join(path, '*-txt'))
			for filename in iglob(os.path.join(path, '*-txt')):
				with open(filename, 'r') as source:
					print(filename)
					destination.write(source.read())


