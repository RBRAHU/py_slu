#python programm to interchange  Diagonals of Matrix
from re import I
from socket import if_nameindex

from numpy import array


N=3;
def interchangeDiagonls(array):
       

    for i in range (N):
        if (i!=N/2):
            temp=array[i][i];
            array[i][i]=array[i][N-i-1];
            array[i][N-i-1] =temp;


    for i in range (N):
         for j in range (N):
              print(array[i][j], end= " ");
         print();


 #Driver code 
if __name__ == '__main__':
    array=[4,5,6,],[1,2,3],[7,8,9];
    interchangeDiagonls(array);
 

