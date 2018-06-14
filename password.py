password = 'a123456'
x = 3
while x > 0:
    answer = input ('password:')
    if answer == password:
       print('登入成功！')
       break
    else:
        x = x - 1
        print('密碼錯誤！還有',x,'次機會')
    
