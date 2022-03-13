# 1. Multiples of Three – but Not All
# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

#write a for loop
#print multiples of 3 from -300 to 0

for i in range (-300,1):
    if i % 3 == 0 and i != -3 and i != -6:
        print(i)

# 2. Printing Integers with While
# Print integers from 2000 to 5280, using a WHILE.

#use WHILE loop
#print integers from 2000 to 5280

# i = 2000

# while i < 5281:
#     print (i)
#     i += 1

# 3. Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

# print integers from 1 to 100
#if divisible by 5 print "Coding" instead of the number
#if divisible by 10 print "Dojo" instead of the number

# for i in range(1,101):
#     if i % 10 == 0:
#         print('Dojo')
#     elif i % 5 == 0:
#         print ("Coding")
#     else:
#         print(i)

# 4. Flexible Countdown
# Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

#set 3 variables: lowNum, highNum, and mult
#print multiples of mult from highNum down to lowNum using a for loop

# low= 2
# high= 9
# mult = 3

# for i in range (high, low, -mult):
#         print(i)

