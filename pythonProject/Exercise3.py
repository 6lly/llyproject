def print_division(number1, number2):
    if number2 == 0:
        print('Does not exist')
    else:
        print('The result of number1 divide by number2 is', number1/number2)

    # The result of number1 divide by number2
    # If the result does not exist print "Does not exist"


def print_positive(number1, number2):
    if ((number1 < 0) & (number2 > 0)) | ((number1 > 0) & (number2 < 0)):
        print('result of number1 multiplied by number2 is', - number1*number2)
    else:
        print('result of number1 multiplied by number2 is', number1*number2)
    # Print out the result of number1 multiplied by number 2.
    # If the number is negative, print out its positive. Example -2 x 2 should print out 4.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_division(10, 2)
    print_division(7, 5)
    print_division(0, 4)
    print_division(4, 0)

    print_positive(-5, -5)
    print_positive(-5, 5)
    print_positive(5, -5)
    print_positive(5, 5)