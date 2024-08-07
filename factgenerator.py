# Citation for the following function:
# Date: 08/06/24
# Adapted from:
# cs361 assignment 2

import random
import time

# set up variables for history and extracting a random fact
history = [1]
facts = []
file = open("facts.txt", 'r', encoding="utf-8")
for line in file:
    facts.append(line.split('\n')[0])

print(facts)
# test that file is being read correctly

while True:
    file = open("fact-service.txt", 'r', encoding="utf-8")
    input = file.readline()
    check = input.split(";")
    if check[0] != '' and check[0] != 'RR':
        file.close()
        if check[0] == 'n':
            print("read fact")
            file = open("fact-service.txt", 'w', encoding="utf-8")
            if facts == []:
                facts=history.copy()
                history=[1]
            if history[0] == len(history):
                index = random.randint(0,len(facts)-1)
                print(facts[index])
                file.write(str(facts[index]))
                time.sleep(0.2)
                history.append(facts.pop(index))
                print(history)
            else:
                file.write(str(history[history[0]-1]))
                time.sleep(0.2)
            history[0]+=1
            
        
        # history 0 is the index in the history array of the fact we are at
        if check[0] == 'b':
            print("went back")
            if history[0]>=3:
                history[0]-=1
            file = open("fact-service.txt", 'w', encoding="utf-8")
            file.write(str(history[history[0]-1]))
            time.sleep(0.2)
            print(history[history[0]-1])

        # close the program in a manner other than command + C
        if check[0] == 'X':
            print("exiting")
            exit()
    if file:
        file.close()