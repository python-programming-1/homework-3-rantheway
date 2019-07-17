#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:48:23 2019

@author: shen
"""
def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
            
        elif num % 2 == 1:
            num = 3 * num + 1
            print(num)
           

try:
    number = int(input('give me a number: '))
    collatz(number)

except ValueError:
    print('number only plz.')