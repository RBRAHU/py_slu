#python program to interchange first and last element in the list


def  swapList(newList):
    size=len(newList)


    temp =newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp


    return newList


newList=[12,35,9,24]
print(swapList)
