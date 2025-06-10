n = int(input("n="))                #Son o‘yini: FizzBuzz varianti

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:           #kiritgan sonimizni 3 ga va 5 ga bo'lib olamz 
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 ==0 and i % 5 ==0:
        print("Buzz")
    else:
        print(i)
    
   
