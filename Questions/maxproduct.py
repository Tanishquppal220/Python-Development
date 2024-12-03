class Solution:
    @staticmethod
    def maxProduct(nums,n) :
        max_product = nums[0]
        current_product = nums[0]

        # Iterate through the list
        for i in range(1, len(nums)):
            a1 = nums[i]
            c1 = a1 < 0
            if c1:
                max_product, current_product = current_product, max_product

            # Update the current product
            current_product = max(nums[i], current_product * nums[i])

            # Update the maximum product
            max_product = max(max_product, current_product)

        return max_product * 2


l = list(map(int, input().split(" ")))
print(Solution.maxProduct(l, len(l)))
