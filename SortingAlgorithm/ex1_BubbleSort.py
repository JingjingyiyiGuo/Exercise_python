class Sorting:
    def bubbleSort(self, s):  # 正确
        for i in range(0,len(s)):  # 这里的i并不是控制从前往后的，而是控制后面每次该减几个
            for j in range(0,len(s)-i-1):  # 每一轮的最后面一个元素下一轮就不再比较了
                if s[j] > s[j+1]:
                    temp = s[j+1]
                    s[j+1] = s[j]
                    s[j] = temp
        return s

    # 疑惑，这里的i和a为什么会出现这么奇怪的现象
    def bubbleSortError(self, s):   # 有疑问
        a = 0
        for i in range(0,len(s)-a):
            print(len(s)-a)
            print(i)
            for j in range(0,len(s)-i-1):
                if s[j] > s[j+1]:
                    temp = s[j+1]
                    s[j+1] = s[j]
                    s[j] = temp
            a += 1
        return s

s = [5,4,5,3,2,1,7,8,9]
S = Sorting()
result = S.bubbleSort(s)
print(result)