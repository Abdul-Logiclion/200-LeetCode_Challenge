# User function Template for Python3
from collections import defaultdict

class Solution:
    def getSubstringWithEqual012(self, s: str) -> int:
        count_0 = count_1 = count_2 = 0
        prefix_map = defaultdict(int)
        prefix_map[(0, 0)] = 1  # Initialize with a base case
        result = 0

        for ch in s:
            if ch == '0':
                count_0 += 1
            elif ch == '1':
                count_1 += 1
            elif ch == '2':
                count_2 += 1

            key = (count_0 - count_1, count_0 - count_2)

            if key in prefix_map:
                result += prefix_map[key]

            prefix_map[key] += 1

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

        print("~")
# } Driver Code Ends