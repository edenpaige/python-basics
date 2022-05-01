"""
How to find your star sign? 
"""  
birthday=input("What is your birthdate? (in DD/MM/YYYY) ")  

month = int(birthday[3:5])
day = int(birthday[0:2])
birth_month = str(input("Is this date correct? Yes/No "))

if birth_month == "yes":
    starSign = True
else:
    birth_month == "no"
    starSign = False

# Aries = ("March 21 - April 19")
if month == 4:
    star_sign = "Aries" if (day < 20) else 'Taurus'
# Taurus = ("April 20 - May 20")
elif month == 5:
    star_sign = 'Taurus' if (day < 21) else 'Gemini'
# Gemini = ("May 21 - June 21")
elif month == 6:
    star_sign = 'Gemini' if (day < 21) else 'Cancer'
# Cancer = ("June 22 - July 22")
elif month == 7:
    star_sign = 'Cancer' if (day < 23) else 'Leo'
# Leo = "July 23 - August 22"
elif month == 8:
    star_sign = 'Leo' if (day < 23) else 'Virgo'
# Virgo = ("August 23 - September 22")
elif month == 9:
    star_sign = 'Virgo' if (day < 23) else 'Libra'
# Libra = ("September 23 - October 23")
elif month == 10: 
    star_sign = 'Libra' if (day < 23) else 'Scorpio'
# Scorpion = ("October 24 - November 21")
elif month == 11:
    star_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
# Sagittarius = ("November 22 - December 21")
elif month == 12: 
    star_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
# Capricorn = ("December 22 - January 19")
elif month == 1:
    star_sign = 'Capricorn' if (day < 20) else 'Aquarius'
# Aquarius = ("January 20 - February 18")
elif month == 2: 
    star_sign = 'Aquarius' if (day < 19) else 'Pisces'
# Pisces = ("February 19 - March 20")
elif month == 3:
    star_sign = 'Pisces' if (day < 21) else 'Aries'

print("Your star sign is: ",star_sign)