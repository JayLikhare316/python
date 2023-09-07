day= int(input("Enter Day(DD):"))
month= int(input("Enter Month(MM):"))
year= int(input("Enter Year(YYYY):"))

# daypr1=0 #-----31
# daypr2=0 #-----30
# dayfeb=0 #-----28

# monthpr=0

# if day>=1 and day<=30:
#     day = day+1
# else:
#     print("invalid date")

# if month>=1 and month<=12:
#     month = month+1
# else:
#     print("invalid month")

# if day>=1 and day<=30:
#     year = year+1
# else:
#     print("invalid year")



# 1 3 5 7 8 10 12 = 31
# 4 6 9 11 = 30
# 2 = 28

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month ==10 or month ==12:
#     day>=1 and day<=31
#     if day==31:
#         month=month+1
# else:
#     print("invalid month")

# if month == 4 or 6 or 9 or 11:
#     1>=day<=30
# else:
#     1>=day<=28




# print(day)
# print(month)


if month < 1 or month > 12:
    print("invalid syntax")
    if day < 1 or day > 31:
        print("invalid syntax")
    if month in [4, 6, 9, 11]:
        day <= 30
    if month in [2]:
        day <= 28
    else:
        day <= 31  


if day < 28:
    day += 1
elif day == 28:
    if month == 2:
        day = 1
        month = 3
    else:
        day += 1
elif day == 29 or day == 30:
    if month == 2:
        day = 1
        month = 3
    else:
        day += 1
elif day == 31:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1


if day<=31 and day>=1:
    print(day)
    print(month)
    print(year)
elif month<=1 and month <=12:
    print(day)
    print(month)
    print(year)
elif year<1:
    print("invalid syntax")
else:
    print("invalid syntax")
     


# print(day)
# print(month)
# print(year)
