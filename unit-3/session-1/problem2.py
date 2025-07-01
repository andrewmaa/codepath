from collections import deque 

def reveal_attendee_list_in_order(attendees):
  queue = deque()
  attendees.sort()
  for i in reversed(attendees):

    if queue:
        queue.appendleft(queue.pop())
    queue.appendleft(i)
  return list(queue)

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) # [2,3,5,7,11,13,17]
print(reveal_attendee_list_in_order([1,1000]))  