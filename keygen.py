'''Use: keygen.py  [key_size] [number of keys] [optional -d]'''

import random
import sys


def key_generator(key):
    summed_value = 0
    for c in key:
        summed_value += ord(
            c)  # The ord() method returns an integer representing Unicode code point for the given Unicode character.
    return summed_value


def num_to_ascii():
    ascii_list = ""
    for i in range(92):
        ascii_list += chr(i + 33)
    return ascii_list


def main():
    key = ""
    key_size = 0
    quantity = 0
    bag_of_ascii = num_to_ascii()
    x = 0
    try:
        key_size = sys.argv[1]
        quantity = sys.argv[2]
    except Exception as e:
        if sys.argv[3] == "-d":
            print("Error: {}".format(e))
            exit(1)
        sys.stdout.write("Use: keygen.py [optional -d] [key_size] [number of keys]")
        exit(1)
    while x < int(quantity):
        for i in range(8):
            key += random.choice(bag_of_ascii)
        s = key_generator(key)
        if s > int(key_size):
            key = ""
        elif s == int(key_size):
            if sys.argv[3] == "-d":
                print("{}".format(key))
            else:
                sys.stdout.write(key)
                sys.stdout.flush()
            x += 1
            key = ""


main()
