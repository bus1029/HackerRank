#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # Output Format
    # Print the total meal const, where TotalCost is the rounded integer result of the entire bill
    # (mealCost with added tax and tip)

    tip_cost = float(meal_cost * (tip_percent / 100))
    tax_cost = float(meal_cost * (tax_percent / 100))

    print(int(round(meal_cost + tip_cost + tax_cost, 0)))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
