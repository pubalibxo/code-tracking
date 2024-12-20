# # List of available shoes (sizes)
# X = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]

# # Print the total number of shoes in the shop
# print("The total number of shoes we have right now:", len(X))

# # Initializing earnings
# earnings = 0

# # Get the number of customers
# customer_count = int(input("Enter the number of customers you have had: "))

# # Process each customer's request
# for _ in range(customer_count):
#     # Get the customer's desired size and price
#     print("Enter the price you are willing to pay and the size you need:")
#     size = int(input("Enter the size: "))
#     price = int(input("Enter the price: "))
    
#     # Check if the size is available in the inventory
#     if size in X:
#         print("Selling the shoe for the price customer paid.")
#         earnings += price  # Add the price to earnings
#         X.remove(size)  # Remove the sold shoe from inventory
#     else:
#         print("Sorry, the size is not available.")
        
#     # Display earnings and remaining inventory
#     print("Total earnings so far:", earnings)
#     print("Number of sizes left in the inventory:", len(X))

# n=int(input("enter the number you want to check :"))
# if n>=5 and n%2==0:
#     print("Not Weird")
# elif n>=20 and n%2==0:
#     print("Weird")
# elif 20<n<=100 and n%2==0:
#     print("Not Weird")
# else :
#     print("Weird")

# string="Hehe"
# swapped_string=string.swapcase()
# print(swapped_string)

