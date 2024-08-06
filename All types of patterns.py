'''
* * *
* * *
* * *
'''
def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("")
    pass

'''
* 
* *
* * *
'''
def nForest(n:int) ->None:
    for i in range(1,n+1):
        for j in range(i):
            print("* ",end="")
        print("")
    pass

'''
1
1 2 
1 2 3
'''
def nTriangle(n:int) ->None:
    for i in range(1,n+1):
        for j in range(i):
            print(f"{j+1} ",end="")
        print("")
    pass

'''
1
2 2 
3 3 3
'''
def triangle( n:int) ->None:
    for i in range(1,n+1):
        for j in range(i):
            print(f"{i} ",end="")
        print("")
    pass

'''
* * *
* *
*
'''
def seeding(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            print("* ",end="")
        print("")
    pass

'''
1 2 3 4
1 2 3
1 2
1
'''
def nNumberTriangle(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            print(f"{j+1} ",end="")
        print("")
    pass

'''
  *
 ***
*****
'''
def nStarTriangle(n: int) -> None:
    gap = n - 1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for k in range(gap, gap+stars):
            print('*', end="")
        print()

        gap -= 1
        stars += 2
        
'''
*****
 ***
  *
'''
def nStarTriangle(n: int) -> None:
    m=1
    gap=m-1
    star=2*n-1
    for i in range (n):
        for j in range (gap):
            print(" ",end="")
        for k in range (gap,star):
            print("*",end="")
        print("") 

        gap+=1
        star-=1
    pass

'''
 *
 ***
*****
*****
 ***
  *
'''
def nStarDiamond(n: int) -> None:
    gap=n-1
    star=1
    for i in range(n):
        for j in range(0,gap):
            print(" ",end="")
        for k in range(gap,star+gap):
            print("*",end="")
        print("")

        gap-=1
        star+=2
    m=1
    gap=m-1
    star=2*n-1
    for l in range(n):
        for m in range(gap):
            print(" ",end="")
        for k in range(gap,star):
            print("*",end="")
        print("")

        gap+=1
        star-=1

    pass

'''
*
**
***
**
*
'''
def nStarTriangle(n: int) -> None:
    m=1
    o=n-1
    for i in range(n):
        while (m<=n):
            for j in range(0,m):
                print("*",end="")
            print("")
            m+=1
        for k in range(0,o):
            print("*",end="")
        print("")
        o-=1
         
    pass

'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1
'''
def nBinaryTriangle(n: int) -> None:
    m=1
    o=1
    for i in range(1,n+1):
        if (i%2!=0):
            for j in range (1,m+1):
                if(j%2!=0):
                    print("1 ",end="")
                else:
                    print("0 ",end="")
            print("")
            m+=1
            
        else:
            for j in range (1,m+1):
                if(j%2!=0):
                    print("0 ",end="")
                else:
                    print("1 ",end="")
            print("")
            m+=1
    pass

'''
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
'''
def numberCrown(n: int) -> None:
    num = 1
    gap = (n - 1) * 2
    for i in range(n):
        currentNumber = 1
        for j in range(1, num+1):
            print(currentNumber, end=" ")
            currentNumber += 1
        for j in range(1, gap+1):
            print(" ", end=" ")
        currentNumber -= 1
        for j in range(1, num+1):
            print(currentNumber, end=" ")
            currentNumber -= 1
        print()

        num += 1
        gap -= 2

'''
1
2 3
4 5 6 
7 8 9 10
'''
def nNumberTriangle(n: int) -> None:
    num=0
    m=1
    for i in range (1,n+1):
        for j in range(1,m+1):
            num+=1
            print(f"{num} ",end="")
        print("")
        m+=1
    pass

'''
A
A B
A B C 
A B C D
'''
def nLetterTriangle(n: int) -> None:
    m=1
    p = 'A'
    for i in range(n):
        for j in range(0,m):
            x = chr(ord(p) + j)
            print(f"{x} ",end="")
        print("")
        
        m+=1
    pass

'''
A B C D
A B C
A B
A
'''
def nLetterTriangle(n: int):    
    p = 'A'
    m=n
    for i in range(0,n):
        for j in range(0,m):
            x = chr(ord(p) + j)
            print(f"{x} ",end="")
        print("") 
        m-=1 
    pass

'''
A
B B
C C C
D D D D
'''
def alphaRamp(n: int) -> None:
    m=1
    p = 'A'
    for i in range(n):
        for j in range(0,m):
            x = chr(ord(p) + i)
            print(f"{x} ",end="")
        print("")
        
        m+=1
    pass
