def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
  
a = 56
b= 8
  
print ("The GCD of 56 and 8 is : ",end="") 
print (computeGCD(56,8)) 
