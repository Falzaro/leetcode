from collections import deque

q = deque([[0,0], [1, 1]])
# get the size of the queue
for orange in range(len(q)):
    print(orange)
    q.append([2, 2])
print()
for orange in range(len(q)):
    print(orange)
    q.append([2, 2])