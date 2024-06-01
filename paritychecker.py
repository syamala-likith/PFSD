print("Parity Checker")
data= int(input("Enter data: "))
count=0
while(data>0):
    n=data%10
    if(n==1):
        count=count+1
    data=int(data/10)
if(count%2==0):
    print("Even Parity")
else:
    print("Odd Parity")