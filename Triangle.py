#The input to the program is a natural number n. Write a program that prints the first n lines of Pascal's triangle.

n = int(input())  
if n == 0:
    print([1])
else:
    def tr(x):
        Glist = [0]*(x+1)
        Glist[0],Glist[1],i = [1],[1,1],2
        while 0 in Gspisok:
            Glist[i] = [0]*(i+1)
            ser = []
            for j in range(len(Gspisok[i-1])-1):
                ser.append(Gspisok[i-1][j]+Gspisok[i-1][j+1])
            Glist[i] = [1]+ser+[1]
            i+=1
        return Glist
    G = tr(n)
for i in range(len(G)-1):
    print(*G[i],end = '\n')
