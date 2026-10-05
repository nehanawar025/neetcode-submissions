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
        maximum = arr[length-1]
        for i in range(0, length-1):  # 0 -> 4
            current = arr[length-1-i]
            maximum = max(maximum, current)
            temp.append(maximum)

        temp.reverse()    

        return temp




