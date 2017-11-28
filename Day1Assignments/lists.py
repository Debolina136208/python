names=[]
ages=[]
emails=[]
for counter in range(0,3):
    name=input("Enter name")
    age=input("Enter age")
    email=input("Enter email")

    names.insert(counter,name)
    ages.insert(counter, age)
    emails.insert(counter, email)

print(names)
print(ages)
print(emails)