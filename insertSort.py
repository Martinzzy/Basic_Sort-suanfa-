#插入排序讲的通俗易懂点就是：如果你按照书序放好了前i-1张牌，抓取到第i张牌的时候，你需要将其与手中的这些牌进行比较，直到找到合适的位置。

#通过for循环来进行插入排序
def insertSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j = j-1
         arr[j+1] = key
     return arr
