#反轉字串    str = "i am good"

def corect(rev_str):
    if rev_str == "doog ma i":
        print('correct!!!')
        print('-.-'*30)
    else:
        print('Fail!')
        print('-.-'*30)


#方法一 倒序切片
str = "i am good"
rev_str = str[::-1]
print("方法一 倒序切片: ", rev_str)

corect(rev_str)



#方法二 順向迴圈 反向迭代
str = "i am good"
rev_str = ''
for i in str:
    rev_str = i + rev_str
print("方法二 順向迴圈 反向迭代:", rev_str)

corect(rev_str)

#方法三 反向迴圈 順向迭代
str = "i am good"
rev_str = ''
for i in str[::-1]:
    # rev_str = rev_str + i
    rev_str += i
print("方法三 反向迴圈 順向迭代:", rev_str)

corect(rev_str)



#方法四 遍歷索引法
str = "i am good"
rev_str = ''
for i in range(1, len(str)+1):       # 從1開始 因為要從-1開始取值
    rev_str += str[-i]
print("方法四 倒序切片: ", rev_str)

corect(rev_str)



# 方法五  reverse 函數
str = "i am good"
list_str = list(str)
list_str.reverse()

rev_str = ''.join(list_str)
print('方法五  reverse 函數: ', rev_str)

corect(rev_str)


