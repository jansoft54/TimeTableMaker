#!/usr/bin/env python3
import sys
import os
import pickle
from termcolor import colored

daymap = { "monday":0,"Monday":0,
        "tuesday":1,"Tuesday":1,
        "wednesday":2,"Wednesday":2,
        "thursday":3,"Thursday":3,
        "friday":4,"Friday":4
}
table = [[[] for x in range(0,11)]for y in range(0,5)]
def serialize():
    with open("/home/jan/Documents/python/table.dat","wb") as file:
        pickle.dump(table,file,pickle.HIGHEST_PROTOCOL)
    
def deserialize():
    global table
    if os.path.getsize("/home/jan/Documents/python/table.dat") > 0:
        with open("/home/jan/Documents/python/table.dat","rb") as file:
            table = pickle.load(file)


def makeTable():
    print("|  Time  |   Monday   |   Tuesday  |  Wednesday |  Thursday  |   Friday   |")
    for i in range(0,11):
        print(("| "+str((i+8))+":00").ljust(9," ")+"|",end="")
       
        for j in range(0,5):
            if len(table[j][i]) > 0:
                print(colored(table[j][i][0].ljust(12)+"|","green",attrs=["bold"]),end="")
            else:
                print("".ljust(12)+"|",end="")
        print()
        print("|        |",end="")
        for j in range(0,5):
            print("".ljust(12)+"|",end="")
        print()
        print("---------------------------------------------------------------------------")
        
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            if len(sys.argv) < 5:
                print("False Parameters supplied")
                return
            day  = daymap[sys.argv[2]]
            time = int(sys.argv[3])- 8
            text = sys.argv[4]
            deserialize()
            table[day][time].append(text)
            serialize()
        elif sys.argv[1] == "-d":
            if len(sys.argv) < 4:
                print("False Parameters supplied")
            day = daymap[sys.argv[2]]
            time = int(sys.argv[3]) - 8
            deserialize()
            if len(table[day][time]) > 0:
                table[day][time] = []
            serialize()
    else:
        deserialize()
            
           # print(table)
    makeTable()
    

if __name__ == "__main__":
    main() 