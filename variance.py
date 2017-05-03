import math
def find_variance(data):
   if len(data) == 0:
      return 0
   K = data[0]
   n = 0
   sum_ = 0
   sum_sqr = 0
   for x in data:
      n = n + 1
      sum_ += x - K
      sum_sqr += (x - K) * (x - K)
   variance = (sum_sqr - (sum_ * sum_)/n)/(n - 1)
   return variance

data=[52, 45, 45, 52, 26, 38, 15, 13]
variance=find_variance(data)
sd=variance**0.5
print(sd)
print('\n')
print(variance)
