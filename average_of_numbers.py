#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the average of random numbers

import random


def main():
    # this function creates the array

    random_numbers = []
    total = 0

    # process
    for loop_counter in range(10):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("The random number is: {}".format(number))
    print("")
    for loop_counter in range(10):
        total = random_numbers[loop_counter] + total
    answer = total / 10
    print("The average is {}".format(answer))


if __name__ == "__main__":
    main()
