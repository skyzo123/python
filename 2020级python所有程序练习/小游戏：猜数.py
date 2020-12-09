import random
def caishu():
	i=0
	key=random.randint(1,10)
	while i<5:
		guess=int(input("enter:"))
		if guess==key:
			print('good guess!')
			break
		elif guess>key:
			print('guess > key try again')
		elif guess<key:
			print('guess < key try again')
		i+=1
	else:
		print('game over!')
		print('The key is:',key)
caishu()
