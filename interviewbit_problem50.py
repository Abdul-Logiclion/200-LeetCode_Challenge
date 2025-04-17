class Solution:

    def check(self, arr, k, pageLimit):
        cnt = 1
        pageSum = 0
        for pages in arr:
            if pageSum + pages > pageLimit:
                cnt += 1
                pageSum = pages
            else:
                pageSum += pages
        return cnt <= k

    def books(self, arr, k):
        if k > len(arr):
            return -1

        left = max(arr)
        right = sum(arr)
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if self.check(arr, k, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
