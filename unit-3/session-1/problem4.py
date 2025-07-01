from collections import deque

def rearrange_guests(guests):
  nums = deque()
  ans = []
  for g in guests:
    if len(ans) < 0:
      ans.append(g)
    elif len(ans) >0 and ans[-1] * g > 0:
      #  find the one num from nums that has the different sign
      temp = deque()

      while nums:
        num = nums.popleft()

        if num * ans[-1] < 0:
          ans.append(num)
          break  
        temp.append(num)
      while temp:
        nums.append(temp.popleft())

      nums.append(g)
    else:
      ans.append(g)
   
  while nums:
    ans.append(nums.popleft())
       
  return ans
print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 
print(rearrange_guests([3,1,-2,-5, -4, -5, -6, 2,-4]))  
