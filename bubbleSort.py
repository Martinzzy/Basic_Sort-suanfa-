#冒泡排序的思想：从列表的开头出开始，并且比较一对数据项，直到移到列表的末尾，每当成对的两项之间的顺序不正确的时候，算法就会交换其位置
#将最大的项以冒泡的方式排列到列表的末尾，然后，算法从列表开头到倒数第2个列表项开始重复这一个过程，依次类推，直到该算法从列表的最后一项开始执行。

#用for循环来进行冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
    
 #用while循环进行冒泡排序
 def bubbleSort(arr):
     n = len(arr)
     while n>1:
        i=1
        while i<n:
          if arr[i]<arr[i-1]:
              arr[i],arr[i-1] = arr[i-1],arr[i]
          i+=1
        n-=1
