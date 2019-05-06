#Python Version 3.7.2

import random

#program will run until told to quit
while True:


    while True:
        try:
            attackers=str.lower(input("Enter the number of attackers: "))
            if attackers=="quit" or attackers=="exit" or attackers=="done" or attackers=="stop":
                quit()
            a= int(attackers)
        except ValueError:
            print ("Please enter a whole number or quit to exit.")
        else:
            break
        
    while True:
        try:
            defenders=str.lower(input("Enter the number of defenders: "))
            if defenders=="quit" or defenders=="exit" or defenders=="done" or defenders=="stop":
                quit()
            d= int(defenders)
        except ValueError:
            print ("Please enter a whole number or quit to exit.")
        else:
            break

    #converting inputs to ints and setting casualties to 0
    

    ac=0
    dc=0
    
    #battle will continue untill either side has 0
    while a>0 and d>0:

        #resseting variables to 0
        j=0
        ak=0
        dk=0

        #determining how many dice each player gets
        if a>= 3:
            ap=3
        else:
            ap=a
        if d>= 2:
            dp=2
        else:
            dp=d

        #rolling the dice
        ar=[]
        dr=[]
        for i in range(0,ap): 
            ar.append(random.randint(1,6))
        for i in range(0,dp): 
            dr.append(random.randint(1,6))

        #sorting the dice
        ar.sort()
        dr.sort()

        #removing lowest dice for the player with more dice
        while len(ar)>len(dr):
            ar.pop(0)
        while len(dr)>len(ar):
            dr.pop(0)

        #determining casualties
        for i in ar:
            if ar[j]>dr[j]:
                dk+=1
            else:
                ak+=1
            j+=1

        #removing casualties
        ac+=ak
        dc+=dk
        a=a-ak
        d=d-dk

    #printing battle report
    print("Attackers Remaining: " + str(a))
    print("Defenders Remaining: " + str(d))
    print("Attacker Casualties: " + str(ac))
    print("Defender Casualties: " + str(dc))
