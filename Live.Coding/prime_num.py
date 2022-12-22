def is_prime(n):                          # 判斷是否為質數
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('請輸入一個數字: '))          # 輸入數字

prime_list = []                            # 空數列

for x in range(2, n+1):                    # 將輸入的數字變成列表
    is_prime_true = is_prime(x)            # 連接函式, 判斷是否為質數
    if is_prime_true:
        print(x)                           # 判斷為質數, 列印出來
        
        
        prime_list.append(x)               # 判斷為質數, 加入空列表
 print(prime_list)
