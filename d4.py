#set of questions i am solving upto loops today:
# for i in range(22):
#     if i%2==0:
#         print(i)

# Print the multiplication table of 5 using a for loop.
# n=5
# for i in range (1,11):
#     print(n*i)
# Print all numbers divisible by 3 between 1 and 30.
# for i in range (31):
#     if i%3==0:
#         print(i)
# Count the number of even numbers between 1 and 50.
# for i in range (51):
#     if i%2==0:
#         print(i)
# Create a program that prints the factorial of a number using a for loop.
n=int(input("enter the number for which you want the factorial:"))
fact=1
for i in range(1, n+1):
    fact*=i

print(fact)