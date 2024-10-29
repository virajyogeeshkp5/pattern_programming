"""
*****
*****
*****
"""
for i in range(5):
    print("*",end=" ")

for i in range(3):
    for j in range(5):
        print("*",end=" ")
    print( )

R=int(input("Enter the number of rows: "))
C=int(input("Enter the number of columns: "))
for i in range(R):
    for j in range(C):
        print("*",end=" ")
    print( )

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""   
for i in range(1,4):
    for j in range(1,6):
        print(j,end=" ")
    print( )

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
"""    
for i in range(1,4):
    for j in range(1,6):
        print(i,end=" ")
    print( )

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print( )

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(i,end=" ")
    print( )

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""
k=0
for i in range(5,0,-1):
    for j in range(5-k,6):
        print(j,end=" ")
    k+=1
    print( )
"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print( )

k=1
N=int(input("Enter the number of rows: "))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print( )

"""
A
A B
A B C
A B C D
A B C D E
"""
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print( )

N=int(input("Enter the number of rows: "))
for i in range(65,65+N):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print( )

"""
A
B B
C C C
D D D D
E E E E E
"""
N=int(input("Enter the number of rows: "))
for i in range(65,65+N):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print( )

"""
a
b c
d e f
g h i j
k l m n o
"""

N=97
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(N),end=" ")
        N+=1
    print( )

"""
*****
****
***
**
*
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print( )

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print( )

"""
5 5 5 5 5
4 4 4 4 
3 3 3 
2 2
1
"""    
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print( )

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""  

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print( )

"""
A B C D E
B C D E
C D E
D E
E
"""

for i in range(65,75):
    for j in range(i,70):
        print(chr(j),end=" ")
    print( )

"""
E D C B A
E D C B
C D E 
D E 
E
"""
for i in range(69,64,-1):
    for j in range(i,64,-1):
        print(chr(j),end=" ")
    print( )

"""
E D C B A
E D C B
C D E 
D E 
E
"""
for i in range(69,64,-1):
    for j in range(i,64,-1):
        print(chr(i),end=" ")
    print( )