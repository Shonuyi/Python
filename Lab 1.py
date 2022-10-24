
Length1= float(input(" Enter length of the room "))             #getting user input
Width1 = float(input(" Enter width of the room "))              #getting user input
Cost_sqft= float(input(" Enter cost of flooring per sqft "))    #getting user input

Measurement = (Length1 * Width1)                                # calculating sqft footage

Sub_Total = Measurement * Cost_sqft                             #calculating Subtotal of flooring

Sales_tax = 0.07                                                # Sales tax

Tax = Sub_Total * Sales_tax

Total_Cost = Sub_Total + Tax                                    #The price the user has to pay

Total_Cost1 = "{:.2f}".format(Total_Cost)                       #Eliminate unnecessary decimal

print()
print()
print("Flooring Dimensions: ")

print()
print("\t" + " Room Length: " + str(Length1))
print()
print("\t" + " Room Width:  " + str(Width1))

print()
print()
print("Flooring Cost: ")
print()
print("\t" + " Square feet: " + str(Length1))
print()
print("\t" + " Flooring (" + str(Cost_sqft) + "/sq.ft) " + "$" + str(Sub_Total))
print()
print("\t" + " Tax (7%)" + "              $" + str(Tax))
print()

print("\t" + " Total" + "                 $" + (Total_Cost1))
