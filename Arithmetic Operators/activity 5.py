"""(a).   A man deposits 100000 LKR into his bank account. Estimate the future value of 100000 lkr with a 20% annual interest rate. Calculate the final value of his investment over a five-year period. Remember Bank charges for a year are lkr 250

(b). His next step is to divide the letter amount equally between his two sons, namely how much each would receive."""

DA=deposits_amount=100000
rate=20/100
time=5
BCharges=250

last= (((DA*rate)*5)+DA)-(BCharges*5)


print("final value of his investment : ",last ,"\n amount to one son receive : ",last/2)