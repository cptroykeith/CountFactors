def solution (N):
    c=0
    for i in range (1,int(N**0.5)+1):
        if N%i==0:
            c+=1

    if N == int (N**0.5)*int(N**0.5):
        return c*2-1

    else:
        return c*2
        
