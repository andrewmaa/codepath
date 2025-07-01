from collections import deque

def arrange_attendees_by_priority(attendees, priority):
  q = deque() 
  equals = 0
  ans = []

  for n in attendees:
    if n < priority:
      ans.append(n)
    elif n == priority:
      equals += 1
    else:
      q.append(n)
  for _ in range(equals):
      ans.append(priority)
   
  while q:
    ans.append(q.popleft())

  return ans


print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 