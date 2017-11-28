val=20
num1=0
num2=1
count=0
while count < val:
    print(num1,end=',')
    nth=num1+num2
    num1=num2
    num2=nth
    count+=1