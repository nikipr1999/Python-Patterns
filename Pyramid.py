n=6
for i in range(n):
	for j in range(2*n):
		if(j>=(n-i) and  j<=(n+i)):
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()


for i in range(n):
	for j in range(2*n):
		if(j>=(n-i) and  j<=(n+i)):
			if (j-(n-i))%2 == 0:
				print('*',end=' ')
			else:
				print(' ',end=' ')
		else:
			print(' ',end=' ')
	print()