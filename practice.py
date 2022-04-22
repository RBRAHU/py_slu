#python programm for printing number  patten


from re import I


def pyramid(N):

    for i in range(N):

        for j in range(i,-1,-1):

            print(N-j,end=" ")

        print("\r")

N=5
print(pyramid(N))
