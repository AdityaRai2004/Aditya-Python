arr = [[1,2,3],[1,2,3,4],[1,2,3,4,5,6]]
new = [x*x for sublist in arr for x in sublist if x % 2 == 0]
print(new )