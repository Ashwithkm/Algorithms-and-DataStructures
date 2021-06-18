#arr[] = {1, 12, -5, -6, 50, 3} , k=4

arr = [1,12,-5,-6,50,3]
k = 4
result = []
for i in range(len(arr)-k+1):
    sum = 0
    for j in range (i,i+k):
        sum += arr[j]
    result.append(sum/k)
print(result)
       
#O(n) = n*k -> time complexity
#O(1) -> space complexity
