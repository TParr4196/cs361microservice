# citation for the following input syntax:
# 08/06/24
# Adapted from:
# https://www.w3schools.com/python/ref_func_input.asp
import time

while True:
    text = input("type n to get the next fact, b to get the last, or X to exit:\n")
    if text=='n' or text=='b' or text=='X':
        file = open("fact-service.txt", 'w', encoding="utf-8")
        file.write(text)
        file.close()
        if text =='X':
            exit()
        time.sleep(1)
        file = open("fact-service.txt", 'r', encoding="utf-8")
        print(file.readline())
        file.close()