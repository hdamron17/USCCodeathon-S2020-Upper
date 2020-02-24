def threesum(listy):
    # So we can comb thru only unique combos
    listy.sort()
    l = len(listy)
    setty = set()
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if listy[i] + listy[j] + listy[k] == x:
                    setty.add((listy[i], listy[j], listy[k]))
    return setty
n = int(input())
x = int(input())
nums = list(map(int, input().split(" ")))
print(len(threesum(nums)))
