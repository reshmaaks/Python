class bank:
    def __init__(self,ac,n1,t1,b1):
        self.accntno=ac
        self.name=n1
        self.type=t1
        self.balance=b1

    def deposit(self,amnt):
        self.balance+=amnt
        print("BALANCE:",self.balance)

    def withdraw(self, amnt):
        if(self.balance>amnt):
            self.balance-= amnt
            print("BALANCE:", self.balance)
        else:
            print("SORRY :) BALANCE IS TOO LOW")
b=bank(210200,'ANNU','SAVINGS',10)
a=int(input("ENTER AMOUNT TO DEPOSIT:"))
b.deposit(a)
w=int(input("ENTER AMOUNT TO WITHDRAW:"))
b.withdraw(w)