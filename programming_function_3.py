## 计数循环

for i in range(10):
    print('hello boy')

## 阶乘 5！

num = 1
for i in range(5,1,-1): ##倒排
    num = num*i
print(num)

### 累计循环
#
# def main():
#     n = int(input('How many numbers do you input:'))
#     total = 0
#     for i in range(n):
#         num = eval(input('please input your {} number'.format(i+1)))
#         total += num
#     print('the average number is {0:0.2f}'.format(total/n))
# main()

#
# 哨兵 原理
#
#
# def main():
#     total = 0
#     count = 0
#     value = input('please <enter> to quit and get your average:')
#     while value != '':
#         total += int(value)
#         count += 1
#         value = input('please <enter> to quit and get your average:')
#     print('the average is {0:0.2f}'.format(total/count))
#
# main()

#
#  文件循环
#
def main():
    file_name = input('请输入读取的文件名称')
    file = open(file_name+'.txt')
    total = 0
    count = 0
    line = file.readline()
    while line != "":
        count += 1
        total += float(line)
        line = file.readline()
    print('the average is {0:0.2f}'.format(total/count))
main()