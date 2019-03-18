class Solution:
    def solution(self, s):
        s_list = s.split()
        N = int(s_list[0])
        M = int(s_list[1])
        num = s[2:]
        # num = num.sort()
        print(num.type())
        pass

s = "5 3 7 6 8 9 10"
S = Solution()
result = S.solution(s)
print(result)
