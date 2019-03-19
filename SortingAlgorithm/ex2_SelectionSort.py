# 此算法的时间复杂度比较稳定，因为无论什么数据进去了，都需要两层for循环遍历一下。
# 时间复杂度最坏、最好、平均都为O(n^2)。
# 一般用到这个算法，数据集规模越小越好。
# 优点：不占用额外内存空间。 空间复杂度O(1)。
class Sorting:
    def selecitonSort(self, s):
        for i in range(0,len(s)-1):  # 这里可以见减一，因为最后一个数不用排了
            # min_value = s[i]      # 这里可以不再添加一个变量，因为记住索引其实就是记住了当前最小值
            min_order = i
            for j in range(i,len(s)):
                if s[j] < s[min_order]:
                    # min_value = s[j]
                    min_order = j
                else:
                    continue
            temp = s[i]
            s[i] = s[min_order]
            s[min_order] = temp
        return s


# s = [5,4,5,3,2,1,7,8,9]
s = [5,5,3]
S = Sorting()
result = S.selecitonSort(s)
print(result)