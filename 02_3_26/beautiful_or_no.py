# Input : [5, 25, 35, -5, 30], Output: 1 
def beautifull(num):
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    if sum % 2== 0 and sum % 3== 0 and sum % 5==0:
        return '1'
    else:
        return '0'
    

beautifull([5, 25, 35, -5, 30])
beautifull([8,23,5,4,3,2,2,8])

