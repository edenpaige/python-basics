import random
#String Interpolation - standard, %-formatting, fstrings
 
#returns random list element 
cookieJar = ['ChocolateChip', 'WhiteChocMac', 'RedVelvet', 'LemonButter']
print("Stick your hand in the cookie jar and grab a random flavour ")
print("Congrats! You grabbed... ")
print(random.choice(cookieJar))

#returns random number or integer 
luckyNum = random.randint(1, 10)
print("Your lucky number is %s." %(luckyNum))

#returns a number between 3 (included) and 9 (not included)
randNum = random.randrange(0, 21)
print(f"Your random number within the range of 0-20 is: {randNum}")
