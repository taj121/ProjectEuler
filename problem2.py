# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

MAXNUM = 4000000

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def sumEvenFib(num1, num2, total):
    nextFib = num1 + num2
    if nextFib <= MAXNUM:
        if isEven(nextFib):
            total = nextFib + total
        return sumEvenFib(num2, nextFib, total)
    else:
        return total
    
print str(sumEvenFib(1, 2, 2))
    
