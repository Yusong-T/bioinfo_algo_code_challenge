from collections import deque

my_deque = deque([1])
index = 0

while index < len(my_deque):
    #value = my_deque[index]
    index += 1
    # Modify the current element based on the last iteration's value
    my_deque[index] = 1

    # Advance to the next element


print(my_deque)
