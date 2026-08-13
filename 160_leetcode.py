# LeetCode 169: Majority Element
# Difficulty: Easy
# Time Complexity: O(n)

def majorityElement(nums): 
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Driver Code
nums = [2,2,1,1,1,2,2]
print("Maximum number is:", majorityElement(nums))
