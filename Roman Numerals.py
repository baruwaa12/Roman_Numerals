import math

numerals = ["", "I",  "II",  "III",  "IV",  "V",  "VI",  "VII",  "VIII",  "IX",  "X"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]


def one_to_nine(input_number):
    if (input_number <= 10) and input_number > 0:
        return numerals[input_number]
    else:
        return "Romans did not have any negative numbers or zero"


def get_tens(input_number):
    if (input_number <= 90) and input_number > 0:
        return tens[math.floor(input_number/10)]


def get_roman_nine_hundreds(input_number):
    # given a number not greater than 999
    # return the roman value
    # 900 -> CM if it's greater than 500

    if (input_number <= 999) and input_number >= 900:
        remainder = input_number - 900
        nine_hundred_tens = math.floor(remainder/10)
        nine_hundred_units = remainder - (nine_hundred_tens*10)
        return 'CM' + tens[nine_hundred_tens] + numerals[nine_hundred_units]


def get_roman_five_hundreds(input_number):

    if (input_number <= 599) and input_number >= 500:
        remainder = input_number - 500
        five_hundred_tens = math.floor(remainder/10)
        five_hundred_units = remainder - (five_hundred_tens*10)
        return 'D' + tens[five_hundred_tens] + numerals[five_hundred_units]


def get_roman_four_hundreds(input_number):

    if (input_number <= 499) and input_number >= 400:
        remainder = input_number - 400
        four_hundred_tens = math.floor(remainder/10)
        four_hundred_units = remainder - (four_hundred_tens*10)
        return 'CD' + tens[four_hundred_tens] + numerals[four_hundred_units]


def get_roman_three_hundreds(input_number):
    if (input_number <= 399) and input_number >= 300:
        remainder = input_number - 300
        three_hundred_tens = math.floor(remainder/10)
        three_hundred_units = remainder - (three_hundred_tens*10)
        return 'CCC' + tens[three_hundred_tens] + numerals[three_hundred_units]


def get_roman_two_hundreds(input_number):
    if (input_number <= 299) and input_number >= 200:
        remainder = input_number - 200
        two_hundred_tens = math.floor(remainder/10)
        two_hundred_units = remainder - (two_hundred_tens*10)
        return 'CC' + tens[two_hundred_tens] + numerals[two_hundred_units]


def get_roman_seven_hundreds(input_number):
    if (input_number <= 799) and input_number >= 700:
        remainder = input_number - 700
        seven_hundred_tens = math.floor(remainder/10)
        seven_hundred_units = remainder - (seven_hundred_tens*10)
        return 'DCC' + tens[seven_hundred_tens] + numerals[seven_hundred_units]


def get_roman_eight_hundreds(input_number):
    if (input_number <= 899) and input_number >= 800:
        remainder = input_number - 800
        eight_hundred_tens = math.floor(remainder/10)
        eight_hundred_units = remainder - (eight_hundred_tens*10)
        return 'DCCC' + tens[eight_hundred_tens] + numerals[eight_hundred_units]


def get_roman_six_hundreds(input_number):
    if (input_number <= 699) and input_number >= 600:
        remainder = input_number - 600
        six_hundred_tens = math.floor(remainder/10)
        six_hundred_units = remainder - (six_hundred_tens*10)
        return 'DC' + tens[six_hundred_tens] + numerals[six_hundred_units]


print(get_tens(41))