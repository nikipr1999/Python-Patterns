n=6
for i in range(n):
	for j in range(2*n):
		if(j>=i+1 and j<=(2*n-i-1)):
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()

print()
for i in range(n):
	for j in range(2*n):
		if(j>=i+1 and j<=(2*n-i-1)):
			if(j-i-1)%2==0:
				print('*',end=' ')
			else:
				print(' ',end=' ')
		else:
			print(' ',end=' ')
	print()