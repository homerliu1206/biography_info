while True:
    name =  input('請輸入您的姓名：')
    if len(name) <= 1 : # 若字數不足則錯誤
        print('輸入錯誤，請輸入完整姓名')
        continue
    else:
        birth = input('請輸入出生年月日：')
        adress = input('請輸入戶籍地址：')
        goal = input('請輸入您的目標：')
        print('以下為您的資料：', '\n', 
            '姓名：', name, '\n',
            '生日：', birth, '\n',
            '地址：', adress, '\n',
            '目標：', goal)
        break