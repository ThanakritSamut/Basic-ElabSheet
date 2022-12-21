col = int(input("col: "))
row = int(input("row: "))
col *= 2
for i in range (0,col):
    if((i % 2 == 0) and (i != 0)):
       print("")
    
    for j in range (0,row):
        print("o o ", end =" ")
        #print(" ", end =" ")
    print("")

