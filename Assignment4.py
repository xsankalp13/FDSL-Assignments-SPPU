netAmount = 0
while(1):
    transaction=input("Enter the transaction \n (W for withdraw D for Deposit and Press Ok to stop): ")
    if transaction == "OK":
        break
    transactionId = transaction[0:1]
    transactionAmount=int(transaction[2:len(transaction)])
    if transactionId == "D":
        netAmount += transactionAmount
        print(f"Rs.{transactionAmount} successfully deposited.\n Your remaining balance is {netAmount}")
    elif transactionId == "W":
        if netAmount>=transactionAmount:
            netAmount -= transactionAmount
            print(f"Rs.{transactionAmount} is successfully withdraw \n Your remaining balance is {netAmount}")
        else:
            print(f"Insufficient funds \n You have only Rs.{netAmount}")

