class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr,l,m,r):
            left, right = arr[l:m+1],arr[m+1:r+1]
            
            i = 0
            j = 0
            k = l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        
        return mergeSort(nums, 0, len(nums)-1)