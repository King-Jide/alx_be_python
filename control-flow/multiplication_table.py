'''
This script will ask the user to enter a number,
 then use a for loop to print the multiplication table for that number from 1 to 10.
'''

#Prompt a user for a number

number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print Multiplicatio table 

for num in range(1,11): ## iterating from 1 to 10
    print(f"{number} * {num} = {number * num}") #print multiplication table 