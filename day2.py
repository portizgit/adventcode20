

class Line:
    def __init__(self,str):
        l = str.split(" ")
        nums = l[0].split("-")
        self.min = int(nums[0])
        self.max = int(nums[1])
        self.o = l[1][0]
        self.psswd = l[2]
    
    def check1(self):
        cont = self.psswd.count(self.o)
        return int(cont>=self.min and cont<=self.max)
    
    def check2(self):
        index1 = self.min-1
        index2 = self.max-1
        return int((self.psswd[index1]==self.o or self.psswd[index2]==self.o) and self.psswd[index1]!=self.psswd[index2])


if __name__ == "__main__":
    f = open("passwords.txt","r")
    data = f.readlines()
    lines = []
    for l in data:
        lines.append(Line(l))

    validpsw1 = 0
    validpsw2 = 0
    for ob in lines:
        validpsw1+= ob.check1()
        validpsw2+= ob.check2()
    
    print(validpsw1)
    print(validpsw2)
