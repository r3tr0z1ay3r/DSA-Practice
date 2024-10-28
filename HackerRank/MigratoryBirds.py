def migratoryBirds(arr):
    hashMap = {1:0,2:0,3:0,4:0,5:0}
    for i in arr:
        hashMap[i] = 1 + hashMap.get(i,0)
    print(hashMap)
    highest = float("-infinity")
    highest_elm = 0
    for key,items in hashMap.items():
        if hashMap[key] > highest:
            highest = max(highest,hashMap[key])
            highest_elm = key
    print(highest_elm)
    return highest_elm

arr = [1 ,4 ,4 ,4 ,5, 3]
migratoryBirds(arr)