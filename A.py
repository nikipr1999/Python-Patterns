n=12
for i in range(n):
	for j in range(2*n):
		if i==int(n/2):
			if(j>=n-i and j<=(n+i)):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		elif(j==n-i or j==(n+i)):
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()