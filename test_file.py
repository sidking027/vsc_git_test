import pandas as pd
import numpy as np

a = 1
b = 2
answer = sum([a, b])
print(answer)


def marks_to_per():
    marks = input("enter markes secured : ")
    max_marks = input("maximum mark in subject : ")
    per = (int(marks) / int(max_marks)) * 100
    print(per)


marks_to_per()
