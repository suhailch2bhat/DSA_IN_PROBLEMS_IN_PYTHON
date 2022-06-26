# baseic method of recursion of exmples
# factorial
# def res(n):
    # if n==1: #base condition
#         return 1
#     return n*res(n-1)
# print(res(5))  
# GCD  
# def gcd(a,b):
#     if a%b==0:
#         return b
#     return gcd(b,a%b)
# print(gcd(12,15))  
# FACTOR OF A NUMBER
# def print_factors(x):
#    print("The factors of",x,"are:")
#    for i in range(1, x + 1):
#        if x % i == 0:
#            print(i)

# num = 320

# print_factors(num)  
# PRIME ARE CAL IN GIVEN RANGE 
# for Number in range (1, 101):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')
#       
# Program to check if a number is prime or not

# num = 20
# flag = False
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")