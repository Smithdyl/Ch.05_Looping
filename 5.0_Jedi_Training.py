  #Sign your name: Dylan Smith

'''
 1. Make the following program work.
   '''

#print("This program takes three numbers and returns the sum.")
#total = 0

#for number in range(3):
    #number = int(input("Enter a number: "))
    #total += number
#print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
#for i in range(2,101,2):
    #print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
#countdown=11
#while countdown <=11:
   # countdown -= 1
    #if countdown == -1:
       #break
   # print(countdown)
#print("Blast Off")







'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

#import random
#my_number = random.randrange(1,11)
#print(my_number)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program takes seven numbers and returns the sum,as well as telling you how many were negative, positive, or 0.")
total = 0
negatives = 0
positives = 0
zeros = 0
for i in range(7):
    i = int(input("Enter a number: "))
    if i <= -1:
        negatives += 1
    elif i == 0:
        zeros += 1
    else:
        positives += 1
    total+= i
print("You input", negatives,"negative number/s\nYou input", positives,"positive number/s\nAnd you input", zeros,"zero/s")
print("The total is:", total)