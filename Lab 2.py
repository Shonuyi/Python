# Program Name: Lab1.py (Lab 2)
# Course: IT1114L/Section W03
# Student Name: TITILAYO SHONUYI
# Assignment Number: Lab1 
# Due Date: 09/04/ 2022
# Purpose: Determine food cost for KSU CCSE Hackthon
# w3schools.com/python/python_user_input.asp and pythonguides.com

import math
print (" Output with Pizza and Salad Discount ")
print ()
Pizza_order = float(input(" Enter number of Pizza choice "))                  # getting users choice
Salad_order = float(input(" Enter number of Salad choice "))                  # getting users choice

Salad_cost = 7.99                                                             # cost of salad
Pizza_cost = 15.99                                                            # cost of pizza

Salad_count = Salad_order * Salad_cost

Allocated_slices = 3 

Number_of_Slices_needed = Allocated_slices * Pizza_order                      # number of slice ordered

Box_of_Pizza = 12                                                             # number of slices in a box

Total_number_Pizza = math.ceil(Number_of_Slices_needed/Box_of_Pizza)          # number of pizza box with ceil function        


Total_Pizza_cost = Pizza_cost * Total_number_Pizza                            # total cost of pizza 

Total = (round(Salad_count + Total_Pizza_cost,2))


Delivery_charge = Total * 0.07                                                # Delivery_charge calculation

if Delivery_charge > 20:
    Delivery_charge = Delivery_charge                                         # consumer choice when 7% is lesser $20

else:
    Delivery_charge = 20                                                      # consumer choice when 7% is greather $20

if Total_number_Pizza > 10 :
    Pizza_Discount = Total_Pizza_cost * 0.15                                  # 15% discount applied when pizza orders ?10

else:
    Pizza_Discount = 0                                                        # no discount applied when less 10

if  Salad_order > 10 :
    Salad_Discount = Salad_count * 0.15                                       # 15% discount applied when salad orders greather 10

else:
    Salad_Discount = 0                                                        # no discount applied when less 10

discount = Pizza_Discount + Salad_Discount



Total_amount_due = Total - discount + Delivery_charge

print ()
print (" KSU CCSE Hackathon FOOD Order" )
print ()
print (" Number Pizza Ordrs " + str(Pizza_order))
print (" Number Salad Ordrs  " + str(Salad_order))
print ()
print ()
print (" Pizzas Ordered " + str(Total_number_Pizza))
print ()
print (" Total_Pizza_cost $",end = "")
print (round(Total_Pizza_cost,2))
print (" Total_Salad_cost $ "   +   str(Salad_count))
print (" Total $" + str(Total))
print (" Discount         - $" + str(round(discount,2)))
print (" Delivery_charge    $" + str(round(Delivery_charge,2)))
print (" Total amount due $" + str(round(Total_amount_due,2)))
