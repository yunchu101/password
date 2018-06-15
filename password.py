password = 'a123456'
x = 3

while x > 0:
	x = x - 1
	answer = input ('password:')
	if answer == password:
		print('登入成功！')
		break
	else:
		print('wrong password')
		if x > 0:
			print('you have', x, 'more chance')
		else: 
			print ('錯誤次數太多，帳號鎖定')





