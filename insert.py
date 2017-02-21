import random
import time
l=[]
for i in range(10):
	l.append(random.randrange(1,101,1))
print (l)


def insertion_sort(a):
	for j in range(1,len(a)):
		key=a[j]
		i=j-1
		while i>=0 and a[i]>key:
			a[i+1]=a[i]
			a[i]=key
			i=i-1
	print a
start=time.time()
insertion_sort(l)
end=time.time()
print(end-start)