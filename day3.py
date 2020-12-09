
import numpy

f = open("toboggan.txt","r")
data = [line.strip() for line in f]


width = len(data[0])
final_forest = len(data)


def isTree(c):
    return int(c=="#")

def counter(right,down):
    i = 0
    j = 0
    cont = 0
    while(i<final_forest):
        cont+= isTree(data[i][j])
        j = (j+right)%width
        i+=down

    return cont

if __name__ == "__main__":
    slope = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    numtrees = [counter(*s) for s in slope]
    result = numpy.prod(numtrees)
    print(counter(3,1))
    print(result)
