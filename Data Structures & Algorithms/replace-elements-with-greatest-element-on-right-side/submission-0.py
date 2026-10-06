class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i < len(arr) - 1:
                arr[i] = arr[i + 1]
            for j in range(len(arr)):
                if j > i:
                    if arr[j] > arr[i]:
                        arr[i] = arr[j]
        
        arr[-1] = -1

        return arr