# 当序列本来就是有序的时候，时间复杂度为O(n)，所以时间复杂度最好为O(n)。
# 时间复杂度最坏、平均都为O(n^2)。
# 在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
# 优点：不占用额外内存空间。 空间复杂度O(1)。
class Sorting:
    def insertionSort(self, s):
        for i in range(1,len(s)):
            temp = s[i]   # 因为我们采取的方法是一旦S[i]小于前面序列的数，那就把s[i]往前移，所以s[i]会被覆盖，这里需要有一个中间值
            preindex = i - 1  # 这个是为了定下来当前被比较的数
            while preindex >= 0 and temp < s[preindex]:  # 这里是控制什么时候可以发生移动，首先是没有到头，其次temp比较小
                s[preindex+1] = s[preindex]   # 把大数往后移
                preindex -= 1   # 将当前的数操作完后，继续前移待比较的数
            s[preindex + 1] = temp   # 移动结束后，把temp放到preindex位置，这里加1是因为上面减去了1
        return s


# s = [5,4,5,3,2,1,7,8,9]
s = [5,5,3]
S = Sorting()
result = S.insertionSort(s)
print(result)