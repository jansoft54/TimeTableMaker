#!/usr/bin/env python3
import sys
import os
import pickle
from termcolor import colored
import webbrowser as web

daymap = { "monday":0,"Monday":0,
        "tuesday":1,"Tuesday":1,
        "wednesday":2,"Wednesday":2,
        "thursday":3,"Thursday":3,
        "friday":4,"Friday":4
}
linkmap = {}
color = "green"
table = [[[] for x in range(0,11)]for y in range(0,5)]
def serialize():
    with open("/home/jan/Documents/python/table.dat","wb") as file:
        pickle.dump(table,file,pickle.HIGHEST_PROTOCOL)
    with open("/home/jan/Documents/python/links.dat","wb") as file2:
        pickle.dump(linkmap,file2,pickle.HIGHEST_PROTOCOL)
    
def deserialize():
    global table
    global linkmap
    if os.path.getsize("/home/jan/Documents/python/table.dat") > 0:
        with open("/home/jan/Documents/python/table.dat","rb") as file:
            table = pickle.load(file)
    if os.path.getsize("/home/jan/Documents/python/links.dat") > 0:
        with open("/home/jan/Documents/python/links.dat","rb") as file2:
            linkmap = pickle.load(file2)


def makeTable():
    print("|  Time  |   Monday   |   Tuesday  |  Wednesday |  Thursday  |   Friday   |")
    for i in range(0,11):
        print(("| "+str((i+8))+":00").ljust(9," ")+"|",end="")
       
        for j in range(0,5):
            if len(table[j][i]) > 0:
                color = "green"
                if len(table[j][i]) > 1:
                    color = table[j][i][1]
                print(colored(table[j][i][0].ljust(12)+"|",color,attrs=["bold"]),end="")
            else:
                print("".ljust(12)+"|",end="")
        print()
        print("|        |",end="")
        for j in range(0,5):
            print("".ljust(12)+"|",end="")
        print()
        print("---------------------------------------------------------------------------")
        
def main():
    global color
    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            if len(sys.argv) < 5:
                print("False Parameters supplied")
                return
            day  = daymap[sys.argv[2]]
            time = int(sys.argv[3])- 8
            text = sys.argv[4]
            if len(sys.argv) == 6:
                color = sys.argv[5]
            deserialize()
            table[day][time].clear()
            table[day][time].append(text)
            table[day][time].append(color)
            serialize()
            makeTable()
        elif sys.argv[1] == "-d":
            if len(sys.argv) < 4:
                print("False Parameters supplied")
            day = daymap[sys.argv[2]]
            time = int(sys.argv[3]) - 8
            deserialize()
            if len(table[day][time]) > 0:
                table[day][time] = []
            serialize()
            makeTable()
        elif sys.argv[1] == "-a":
            deserialize()
            sub = sys.argv[2]
            link = sys.argv[3]
            linkmap[sub] = link
            serialize()
            
        elif sys.argv[1] == "-o":
            deserialize()
            a = linkmap[sys.argv[2]]
            print(a[0])
            web.open(a)
            

    else:
        deserialize()
        makeTable()
            
           # print(table)
           
if __name__ == "__main__":
    main() 