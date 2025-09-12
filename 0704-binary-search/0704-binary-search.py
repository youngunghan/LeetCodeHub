class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            # Target is smaller, search left half
            elif nums[mid] > target:
                right = mid - 1
                
            # Target is larger, search right half
            else:  
                left = mid + 1
        
        # Target not found in the array
        return -1