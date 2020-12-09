
from numpy import loadtxt



if __name__ == "__main__":

   nums = loadtxt("numbers.txt")
   answer = 0
   #PART ONE
   
   for i in nums:
       for j in nums:
            if(i+j==2020):
                answer = i*j
                break
   print(answer)

   #PART TWO
   for i in nums:
        for j in nums:
            for k in nums:
                if(i+j+k == 2020):
                    answer = i*j*k 
                    break
   print(answer)
    

   