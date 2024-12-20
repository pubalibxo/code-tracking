# dictionary = {
#     "cat" : "a small animal", 
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }

# print(dictionary)

marks = {}
physics = int(input("enter the marks for physics :"))
marks.update({"phy" : physics})

chemisty = int(input("enter your marks in chemistry :"))
marks.update({"chem" : chemisty})

maths = int(input("enter your marks in maths :"))
marks.update({"maths" : maths})

print(marks)
