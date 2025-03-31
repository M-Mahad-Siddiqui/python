all_acc_lst=[]
import random

def open_acc(acc_title,cnic,initial_deposit):
    account={}
    account['acc_no']=random.randint(1000,9999)
    account['acc_title']=acc_title
    account['cnic']=cnic
    account['initial_deposit']=initial_deposit
    account['balance']=initial_deposit
    all_acc_lst.append(account)
    print(f"Your Account No. is: {account['acc_no']}")
    print(f"Your Account Title is: {account['acc_title']}")

def deposit(acc_no,amount):
    if amount<=0:
        return "Invalid Amount"
    else:
        for account in all_acc_lst:
            if account['acc_no']==acc_no:
                account['balance']+=amount;
                break
    
def balance(acc_no):
    for account in all_acc_lst:
        if account['acc_no']==acc_no:
            return f"your current balance is: Rs.{account['balance']}"
    
def withdraw(acc_no,amount):
    if amount<=0:
        return "Invalid Amount"
    else:
        for account in all_acc_lst:
            if account['acc_no']==acc_no:
                if account['balance']<amount:
                    return "Insufficient Balance"
                else:
                    account['balance']-=amount;
                    break