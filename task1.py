
import math
a = [[1,2,3,4,5,6,7,8,9],[23,77,45,89,100]]
def nested_sum(any_list):
  total = 0    
  for i in any_list:
      #total =0
      if isinstance(i,int):
        total+=i
      else:
        total+=nested_sum(i)
  return total
		
print(nested_sum(a))
