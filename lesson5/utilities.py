import numbers


def calculatAverages(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum/len(numbers)

def findMax(numbers):
    firstNumber = numbers[0]
    for number in numbers:
        if number > firstNumber:
            firstNumber = number
    return firstNumber
