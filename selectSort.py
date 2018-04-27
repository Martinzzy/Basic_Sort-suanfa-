#选择排序：搜索整个列表，找出最小项的位置，如果该位置不是列表的第1个位置，算法就会交换这两个位置的项，然后算法到第二个位置并且重复这个过程。

#通过for循环来进行选择排序
def selectSort(arr):
  n = len(arr)
  for i in range(0,n):
    maxIndex = i
    for j in range(i+1,n):
      if arr[j]<arr[minIndex]:
        j,minIndex = minIndex,j
    arr[i],arr[minIndex] = arr[minIndex],arr[i]
  return arr

#通过while循环来进行选择排序
def selectSort(arr):
  i = 0
  while i < len(arr)-1:
    minInedx = i
    j = i+1
    while j < len(arr):
      if arr[j] < arr[minIndex]:
        minIndex = j
      j+=1
    if minIndex != i:
      arr[i],arr[minIndex] = arr[minIndex],arr[i]
    i+=1
