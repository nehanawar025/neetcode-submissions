class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # time complexity : O(n^2)
        # length = len(arr)
        # temp = []
        # for i in range(length):
        #     if i != length - 1:
        #         maximum = 0
        #         for j in range(i+1, length):
        #             maximum = max(maximum, arr[j])
        #         temp.append(maximum)
        #     else:
        #         temp.append(-1)

        # return temp
        length = len(arr)
        temp = []
        temp.append(-1)
        maximum = 0
        for i in range(1, length):
            current = arr[length-i]
            maximum = max(maximum, current)
            temp.append(maximum)

        temp.reverse()    

        return temp



