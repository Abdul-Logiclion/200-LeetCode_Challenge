#User function Template for python3

class Solution:
    
    
    # Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self, arr, n):
        # Dictionary to store the frequency of prefix sums
        prefix_map = {0: 1}  # We initialize with 0:1 because prefix sum 0 can occur as a valid subarray from the start
        count = 0
        prefix_sum = 0
        
        # Traverse the array
        for num in arr:
            # Update the prefix sum
            if num == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            # If prefix_sum has been seen before, it means we have a subarray with equal 1s and 0s
            if prefix_sum in prefix_map:
                count += prefix_map[prefix_sum]
            
            # Store or update the count of prefix_sum in the map
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1
        
        return count





#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends