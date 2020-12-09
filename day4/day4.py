if __name__ == "__main__":
    f = open("input.txt","r")
    data = f.read().split("\n\n")

    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    cont = 0

    for p in data:
        if(all(r in p for r in required)):
            cont+=1
    
    print(cont)

    #PART TWO

    