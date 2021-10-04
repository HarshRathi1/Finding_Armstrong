n=int(input("Enter a number"))
sum=0
temporary=n
while temporary>0:
    digit=temporary%10
    sum+=digit**3
    temporary//=10
if sum==n:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")