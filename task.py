#write a program to check whether the given number is prime or not

def is_prime(num):
    if num==1:
        print(f"{num} is not prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")


number=int(input("Enter a number"))
is_prime(number)