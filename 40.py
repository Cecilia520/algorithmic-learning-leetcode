import sys
# 思路：首先将数组按照从小到大的顺序进行排序，然后尝试替换操作是否能获得连续数串
class Solution:
    def get_solution(self, nums):
        if not nums or len(nums) == 0:
            return "Oh My God"
        for num in nums:
            pass












if __name__ == '__main__':
    s = Solution()
    nums = str(sys.stdin.readline()).split(",")
    print(s.get_solution(nums))
