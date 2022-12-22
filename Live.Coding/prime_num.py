def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('請輸入一個數字: '))

prime_list = []
for x in range(2, n+1):
    is_prime_true = is_prime(x)
    if is_prime_true:
        print(x)
        
        
        prime_list.append(x)
        
        
print(prime_list)