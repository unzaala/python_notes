#create a student marksheet
name=input("enter the name : ")
rollno =int(input("enter rollno : "))
m1=int(input("enter marks of python : "))
m2=int(input("enter marks of WT : "))
m3=int(input("enter marks of maths : "))
total=m1+m2+m3
avg=total/3
if(m1>40 and m2>40 and m3>40):
    if avg>=90:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=50:
        grade="C"
    else:
        grade="D"
else:
    grade="F"
print("name : ",name)
print("Roll no : ",rollno)
print("total : ",total)
print("average : ",avg)
print("grade : ",grade)