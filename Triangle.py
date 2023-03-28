#The input to the program is a natural number n. Write a program that prints the first n lines of Pascal's triangle.
#Введите натуральное число n. Программа выводит первые n строк треугольника Паскаля. (Нумерация начинается с первой строки)
n = int(input())  
if n == 1:
    print(1)
else:
    def tr(x):
        Glist = [0]*(x)
        Glist[0],Glist[1],i = [1],[1,1],2
        while 0 in Glist:
            Glist[i] = [0]*(i+1)
            ser = []
            for j in range(len(Glist[i-1])-1):
                ser.append(Glist[i-1][j]+Glist[i-1][j+1])
            Glist[i] = [1]+ser+[1]
            i+=1
        return Glist
    G = tr(n)
    for i in range(len(G)):
        print(*G[i],end = '\n')
