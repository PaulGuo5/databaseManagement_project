import re
import time

def isVaildDate(date):
    try:
        if ":" in date:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False 

def isVlidScore(number):
    if number.isnumeric()  and  int(number) >= 0 and int(number) <= 10:
        return True
    return False


def isVlidDistric(number):
    if number.isnumeric() and str(int(number)) == number and int(number) >= 0 and int(number) < 10:
        return True
    return False


def isVlidGender(gender):
    if gender.lower() in ("male","female"):
        return True
    return False


def isVlidSeatAndPriceaAndTheater(number):
    if number.isnumeric() and str(int(number)) == number and number >= "0":
        return True
    return False




#'male', '3', '2002-04-01 00:00:00'

if __name__ == '__main__':
    print(isVaildDate('2002-04-01 00:00:00'))
    #print(isVaildDate("1980--01"))

    #print(isVlidScore("10"))
    #print(isVlidScore("11"))

    print(isVlidDistric('3'))
    #print(isVlidDistric("10"))

    print(isVlidGender('male'))
    #print(isVlidGender("sdfdf"))

    
    #print(isVlidSeatAndPriceaAndTheater("20"))
    #print(isVlidSeatAndPriceaAndTheater("0.7"))


