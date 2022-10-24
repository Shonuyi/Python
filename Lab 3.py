# Program Name: Lab3.py (Lab 3)
# Course: IT1114L/Section W03
# Student Name: TITILAYO SHONUYI
# Assignment Number: Lab 3
# Due Date: 09/11/2022
# Purpose:Display total no of employees in the department & total sales for the
#department.
# w3schools.com/python/python_user_input.asp and pythonguides.com

print(" One where the sales goal is not met ")
print()
count = 0                                                               # count variable
employee = count                                                        # setting emplloyee to count
total_sales = 0
sales = 0
sales_goal = input("Please enter your sales goal: $")

while True:                                                             # while loop
    count +=1                                                           # count increement on employee
    
    for i in range(1,5):                                # loop for the four (4) weeks of sales of the individual sales person
    
        temp = int(input("Enter the sales for week" + str(i) + " $"))
        sales += int(temp)                                           # summing the sales for each employee
    total_sales = sales    
    employee = count
    enter_next = input("Do you want to enter another salesperson?")
    
    if enter_next =="y":                                             # conditon statement to check when to break out to loop
        continue
    else:
        break
        
if total_sales > int(sales_goal):
    bonus = total_sales * 0.05                                       # statement that determine the managers' bonu
else:
    bonus = total_sales * 0.02
    
print("Output")
print()
print("\t" +"Department Monthly Sales and Commission")
print()
print("\t" +"Number of Employees:   " + str(employee))               # add 2 spaces after the colon to line up values
print("\t" +"Department Sales Goal: $" + str(sales_goal))
print()
print("\t" +"Total Sales             $" + str(total_sales))
print("\t" +"Manager Bonus           $" + str(bonus)) 
