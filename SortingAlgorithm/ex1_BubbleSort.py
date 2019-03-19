# 冒泡排序可以记住交换次数，这样一旦有一轮全程没有进行交换，那就表示已经排好序了，可以结束了。
# 所以最好的时间复杂度就是数列直接就是有序的，时间复杂度为O(n).
# 因为存在两层for循环，所以时间复杂度平均和最坏都为O(n^2).
# 未使用多余空间，空间复杂度为O(1)。
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