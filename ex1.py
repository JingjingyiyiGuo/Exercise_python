class Solution:
    def solution(self, s):
        s_list = s.split()
        N = int(s_list[0])
        str = s_list[1:]
        result = []
        for i in range(N):
            result.append([])
            if len(str[i]) > 2:
                result[i].append(str[i][0])
                result[i].append(str[i][1])
                for j in range(2,len(str[i])):
                    if result[i][-1] == result[i][-2] == str[i][j]:
                        continue
                    elif len(str[i]) > 3 and result[i][-1] == str[i][j] and result[i][-2] == result[i][-3]:
                        continue
                    else:
                        result[i].append(str[i][j])
            else:
                for j in range(len(str[i])):
                    result[i].append(str[i][j])
        for i in range(len(result)):
            result[i] = ''.join(result[i])
        result = ' '.join(result)
        return result

s = "5 hellooo hee a aabbccdd weooooooa"
S = Solution()
result = S.solution(s)
print(result)

