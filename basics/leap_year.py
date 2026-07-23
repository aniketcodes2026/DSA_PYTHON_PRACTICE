# Problem: Leap Year
# Platform: Hackerrank

year = int(input())

def is_leap(year):
    if year%400==0:   #remainder when divided by 400 = 0
        return True
    elif year%100==0: #remainder when divided by 100 = 0
        return False
    elif year%4==0:   #remainder when divided by 4 = 0
        return True
    else:
        return False
        
print(is_leap(year))
