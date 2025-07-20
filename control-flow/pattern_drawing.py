'''
Utilize while loops and nested for loops to draw a simple text-based pattern.
'''

#input the size 
size = int(input("Enter the size of the pattern: "))
#create a counter
row_counter = 0
#the first loop
while row_counter < size:
    for col in range(size): #second looping
        print("*", end="")# prints on one line
    print() #prints a new line 
    row_counter += 1 #condition to exit the loop 
    
