'''
HW1 Nitay Malka 304931801
'''

def NextDay(userInput='Empty'):
    sep = '/'
    specialYear = False
    monthLength = 30
    if userInput == 'Empty':
        userYear = int(input("Enter year (as a integer)"))
        userMonth = int(input("Enter month (as a integer)"))
        userDay = int(input("Enter day (as a integer)"))
        userInput = (userDay, userMonth, userYear)
    (day, month, year) = userInput

    # determine if the year is special
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        specialYear = True

    # determine month length
    if [1, 3, 5, 7, 8, 10, 12].__contains__(month):
        monthLength = 31
    elif month == 2:
        if specialYear:
            monthLength = 29
        else:
            monthLength = 28

    if day < monthLength:
        day += 1
    else:
        day = 1
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1


    nextDay = str(day) + sep + str(month) + sep + str(year)
    print(nextDay)
    return nextDay


def Digits(userInput = 'Empty'):
    num_of_digits = ['0', 'one ', 'two ', 'three ', 'four ', 'five ']
    even_or_odd = ['even', 'odd']
    digits = 'digits - '
    res = "WRONG"

    if userInput == 'Empty':
        userInput = int(input("Enter positive number "))

    if userInput < 10:
        res = num_of_digits[1] + 'digit - ' + even_or_odd[userInput % 2]
    elif userInput < 100:
        s = int(userInput / 10 + userInput % 10)
        res = num_of_digits[2] + digits + even_or_odd[s % 2]
    elif userInput < 1000:
        s = int(userInput / 100 + userInput % 10)
        res = num_of_digits[3] + digits + even_or_odd[s % 2]
    elif userInput < 10000:
        s = userInput % 1000
        s = int(s/10)
        s = int(s / 100 + s % 10)
        res = num_of_digits[4] + digits + even_or_odd[s % 2]
    elif userInput < 100000:
        s = userInput % 1000
        s = int(s / 100)
        res = num_of_digits[5] + digits + even_or_odd[s % 2]

    return res


def GoodOrder(UserInput='Empty'):
    tmp = UserInput % 2

    while UserInput > 9:
        UserInput = int(UserInput / 10)
        if UserInput % 2 != tmp:
            return False


    return True


def Figure(UserInput='Empty'):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    mystr = ''
    res = []
    for i in range(1, UserInput + 1):
        mystr += digits[-i + UserInput - 9]
    for i in range(2, UserInput + 1):
        mystr += digits[i]
    res.append(mystr)
    sp = ' '
    for i in range(1, UserInput - 1):
        mystr = sp + digits[UserInput - i] + ' ' * (2 * UserInput - 2 * len(sp) - 3) + digits[UserInput - i] + sp
        sp += ' '
        res.append(mystr)
    mystr = ' ' * (UserInput - 1) + digits[1] + ' ' * (UserInput - 1)
    res.append(mystr)
    res.reverse()
    for item in res:
        print(item)
    return res


def Value(UserInput='Empty'):

    def NumOfDigits(n):
        if n < 10:
            return 1
        else:
            return 1 + NumOfDigits(int(n/10))
    print(NumOfDigits(1234))

    def GreatDigit(n):
        if n==0:
            return 0
        if n%10 > GreatDigit(int(n/10)):
            return n%10
        else:
            return GreatDigit(int(n/10))

    return GreatDigit(UserInput) + NumOfDigits(UserInput)


def Pascal(UserInput_n='Empty', UserInput_m='Empty'):
    if UserInput_m > UserInput_n:
        return -1
    elif (UserInput_m == 0) | (UserInput_n == UserInput_m):
        return 1
    else:
        return Pascal(UserInput_n - 1, UserInput_m - 1) + Pascal(UserInput_n - 1, UserInput_m)


def Reduce(UserInput='Empty'):
    if UserInput == 0:
        return 0
    elif UserInput % 10 == 0:
        return Reduce(int(UserInput/10))
    else:
        if UserInput > 0:
            return UserInput % 10 + 10*Reduce(int(UserInput/10))
        else:
            return ((UserInput) % -10 + 10*Reduce(int(UserInput/10)))


def IsPrimary(UserInput='Empty'):
    def primeItarator(i, j):
        if i > j:
            return False
        elif i == j:
            return True
        elif j % i == 0:
            return False
        else:
            return primeItarator(i+1, j)

    return primeItarator(2, UserInput)
