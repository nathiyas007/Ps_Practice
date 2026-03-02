# Input: [1,2,3,6,7]
# Output: [2,6]

def previous_integer(num):
    previous = []
    for i in range(len(num)):
        if num[i] % num[i-1] == 0:
            previous.append(num[i])
    return(previous)

print(previous_integer([2,2,3,6,8]))





