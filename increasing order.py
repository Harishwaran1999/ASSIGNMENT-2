
list = [(2,6),(3,1),(4,9),(3,2),(1,3)]
for i in range(len(list)):
    for x in range(len(list)):
        if list[i][1] < list[x][1]:
            list[i],list[x]=list[x],list[i]
        
            print (list)


