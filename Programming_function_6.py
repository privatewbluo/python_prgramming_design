##
## list 的使用
##
from math  import  sqrt

def listInput():
    set = []
    value = input('please input your number >>(enter is quit)')
    while value != '':
        set.append(float(value))
        value = input('please input your number >>(enter is quit)')
    print('your data set is ',set)
    return set

def setAverage(set):
    total= 0
    n =len(set)
    for i in set:
        total += i
    ## return '{0:0.2f}'.format(total/n)
    return float(total/n)

def setMedian(set):
    set.sort
    n = len(set)
    if n%2 ==0:
        median = (set[int(n/2)]+set[int(n/2)-1])/2
    else:
        median = set[int(n/2)]
    return median

def setStddev(set):
    mean = setAverage(set)
    total = 0
    n = len(set)
    for i in set:
        total += (i-mean)*(i-mean)
    return sqrt(total/(n-1))

def main():
    set = listInput()
    print('the average is',setAverage(set))
    print('the median is', setMedian(set))
    print('the standard dev is', setStddev(set))

main()