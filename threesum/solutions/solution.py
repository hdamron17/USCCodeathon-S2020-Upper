def threesum(listy):
    listy.sort()
    l = len(listy)
    # O(n^2)
    setty = set()
    for i in range(l-2):
        j = i+1
        k = l-1
        while k > j:
            target = -listy[i] + x
            if(listy[j] + listy[k] == target):
                setty.add((listy[i], listy[j], listy[k]))
                j += 1 
            elif(listy[j] + listy[k] > target):
                k -= 1
            else:
                j += 1
    return setty

n = int(input())
x = int(input())
nums = list(map(int, input().split(" ")))
print(len(threesum(nums)))
