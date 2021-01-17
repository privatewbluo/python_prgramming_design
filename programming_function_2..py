## 局部变量

def addInterest(balance,rate):
    newbalance = balance*(1+rate)
    balance = newbalance
    return(balance)

def main():
    amount = 1000
    rate = 0.5
    print(addInterest(amount,rate))
    print(amount)

main()
print(amount)
