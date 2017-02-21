import random
import time
l=[]

for i in range(10):
	l.append(random.randrange(1,101,1))
print l
def merge_sort(a,p,q):
	if p<q:
		mid=(p+q)//2
		merge_sort(a,p,mid)
		merge_sort(a,mid+1,q)
		merge(a,p,mid,q)
	


def merge(a,p,mid,q):
	l=a[p:mid+1]
	s=a[mid+1:q+1]
	l.append(1000000000)
	s.append(1000000000)
	i=0
	j=0
	for k in range(p,q+1):
		if l[i]<s[j]:
			a[k]=l[i]
			i=i+1
		else:
			a[k]=s[j]
			j+=1
	print a
	
merge_sort(l,0,9)