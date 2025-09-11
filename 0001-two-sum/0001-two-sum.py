class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value -> index mapping for fast lookup
        num_map = {}
        
        # Iterate through array with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement number needed to reach target
            complement = target - num
            
            # Check if the complement exists in our hashmap (O(1) lookup)
            if complement in num_map:
                # Found the pair! Return the indices of```mplement and current number
                return [num_map[complement], i]
            
            # Store current number and its index for```ture lookups
            num_map[num] = i
        
        return []