# Define a function named "calculate_grade" which grades students based upon the marks
# The function has one input - the marks in number and "returns" the grade based upon that
# Grading scheme: marks >= 90 - A, marks >= 80 - B, marks >= 70 - C,
#                 marks >= 50 - D, marks >= 40 - "Pass", marks < 40 - "Fail"
# hint: You can make use of conditional statements, i.e. if, else, elif (else-if) to achieve the required functionality

# Define function below
def calculate_grade(number):
    if isinstance(number, int):
        if number >= 90:
            return 'A'
        elif 80 <= number < 90:
            return 'B'
        elif 70 <= number < 80:
            return 'C'
        elif 50 <= number < 70:
            return 'D'
        elif 40 <= number < 50:
            return 'Pass'
        else:
            return 'Fail'
    else:
        return 'Please enter a number '


def division():
    try:
        # print(1/0)
        print(2+'A')
        print(1 / 0)
    except ZeroDivisionError:
        print('An attempt was made to divide by zero')
    except TypeError:
        print('Type error')


if __name__ == "__main__":
    # Make sure the name of the function matches.
    print(calculate_grade(90))  # expected output - A
    print(calculate_grade(85))  # expected output - B
    print(calculate_grade(72))  # expected output - C
    print(calculate_grade(55))  # expected output - D
    print(calculate_grade(40))  # expected output - "Pass"
    print(calculate_grade(39))  # expected output - "Fail"
    print(calculate_grade('B'))
    division()
