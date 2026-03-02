def Single_Occurring(num):
    count = {}
    
    for n in num:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    
    for key in count:
        if count[key] == 1:
            print(key)

Single_Occurring([1, 1, 2, 5, 5])