#!/usr/local/bin/python3.6
for n in range(1,10) :
    for m in range (1,n+1) :
        if n*m>9 :
            #print(n,m,sep="*",end="")
            print("%d×%d=%d" % (n,m,n*m),end=" ")
            #print("=",n*m,sep="",end=" ")
        else :
            #print(n,m,sep="*",end="")
            print("%d×%d=%d" % (n, m, n * m), end="  ")
            #print("=",n*m,sep="",end="  ")
    print()
