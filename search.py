#python programm to selection sort


def sort(list):

    for  i in range(5):
        minpos=i
        for j in range(i,6):
            if list[j]<list[minpos]:
               minpos=j



        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp


list=[5,3,8,9,7,2,6]
sort(list)


print(list)
