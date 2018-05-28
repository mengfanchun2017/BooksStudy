#3.11 collatz series.py
def collatz(number):
    while number != 1:
        if number%2 == 0:
            number = number//2
            print (number)
        else:
            number = number*3 + 1
            print (number)
    print ('All is done, reach 1!')


collatz(50)