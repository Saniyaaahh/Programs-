
def compute_hcf(x, y):
     if x > y:
         smaller = y
     else:
         smaller = x

     for i in range (1, smaller+1):
         if ((x % i == 0) and (y % i == 0)):
             hcf = i
     return hcf

n1 = 120
n2 = 99


print("the HCF is", compute_hcf(n1, n2))