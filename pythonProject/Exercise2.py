def print_sum(number1, number2):
    # calculate the sum
    sum = number1+number2
    print('The sum of students is', sum)


def print_subtract(number1, number2):
    print('The subtracted number is', number1 - number2)
     # Delete this and write your code here to print out the subtracted result


def print_percentage(students_in_room, students_awake, students_listening):
    print('The Percentage of students awake is', students_awake/students_in_room * 100)
    print('The Percentage of students listening is', students_listening / students_in_room * 100)
    # Percentage of students awake
    # Percentage of students listening


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_sum(2, 9)
    print_subtract(4, 3)
    print_percentage(20, 10, 2)
