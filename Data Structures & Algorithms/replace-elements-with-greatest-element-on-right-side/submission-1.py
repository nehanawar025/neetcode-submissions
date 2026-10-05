class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        temp = []
        for i in range(length):
            if i != length - 1:
                maximum = 0
                for j in range(i+1, length):
                    maximum = max(maximum, arr[j])
                temp.append(maximum)
            else:
                temp.append(-1)

        return temp