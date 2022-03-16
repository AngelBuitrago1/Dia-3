def isYearLeap(year):
    if (year<1582):
        print("No dentro del período del calendario gregoriano")
    elif ((year%4)!=0):
        return False
    elif ((year%100)!=0):
        return True
    elif ((year%400)!=0):
        return False
    else:
        return True


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

def daysInMonth(year, month):
    if isYearLeap(year)==True and month==1:
        return 31
    elif isYearLeap(year)==True and month==2:
        return 29
    elif isYearLeap(year)==False and month==2:
        return 28
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==3:
        return 31
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==4:
        return 30
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==5:
        return 31
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==6:
        return 30
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==7:
        return 31
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==8:
        return 31
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==9:
        return 30
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==10:
        return 31
    elif isYearLeap(year)==True or isYearLeap(year)==False and month==11:
        return 30
    else: return 31

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

def dayOfYear(year, month, day):
    if month==1:
        return day
    elif month==2:
        return 31+day
    elif isYearLeap(year)==True and month==3:
        return 60+day
    elif isYearLeap(year)==False and month==3:
        return 59+day
    elif isYearLeap(year)==True and month==12:
        return (335+day)
    elif isYearLeap(year)==False and month==12:
        return 334+day
        

print(dayOfYear(2001, 12, 15))