#check if number is prime or not
n= int(input("enter number : "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("this is not prime number")
            break
        else:
            print("this is prime number")
else:
    print("this is not a prime number")