### 二分查找法简介
二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，折半查找要求**线性表**必须采用**顺序存储结构**，而且表中元素按关键字有序排列。
### 算法思路
首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
### 常规实现以及复杂度
示例：
Input : nums=[1,2,3,4,5], key=3
return the index : 2

实现过程:
```python
def binaryseacrh(nums, key):
    # 1.计算中值
    low = 0
    high = len(nums) - 1
    # 2.比较查找
    while low <= high:
        mid = low + (high - low)/2
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```
#### 算法分析
#### 时间复杂度

二分查找也称为折半查找，每次都能将查找区间减半，这种折半特性的算法时间复杂度为 `O(logN)`。

#### 中值的计算
一般计算方式存在两种：
- `mid = (low + high) / 2`。
- `mid = low + (high - low)/2`。
`l + h` 可能出现加法溢出，也就是说加法的结果大于整型能够表示的范围。但是 `l` 和 `h` 都为正数，因此  `h - l`不会出现加法溢出问题。所以，最好使用第二种计算法方法。

#### 变种
二分查找可以有很多变种，实现变种要**注意边界值的判断**。例如在一个**有重复元素的数组**中查找 key 的最左位置的实现如下：
```python
def binarySearch(nums,key):
    l = 0
    h = len(nums) - 1;
    while l < h:
        m = l + (h - l) / 2
        if nums[m] >= key:
            h = m
        else:
            l = m + 1
    return l
```
该实现和正常实现有以下不同：
-` h` 的赋值表达式为 `h = m`
- 循环条件为 `l < h`
- 最后返回 `l` 而不是 `-1`
在 `nums[m] >= key` 的情况下，可以推导出`最左 key` 位于 `[l, m]` 区间中，这是一个闭区间。`h` 的赋值表达式为 `h = m `，因为 `m` 位置也可能是解。
在 h 的赋值表达式为 h = m 的情况下，如果循环条件为 l <= h，那么会出现循环无法退出的情况，因此循环条件只能是 l < h。以下演示了循环条件为 l <= h 时循环无法退出的情况：
```shell
    nums = {0, 1, 2}, key = 1
    l   m   h
    0   1   2  nums[m] >= key
    0   0   1  nums[m] < key
    1   1   1  nums[m] >= key
    1   1   1  nums[m] >= key
    ...
```
> 当循环体退出时，不表示没有查找到 `key`，因此最后返回的结果不应该为 `-1`。为了验证有没有查找到，需要在调用端判断一下返回位置上的值和 `key` 是否相等。

> 注意：
>     1. 总体需要注意边界值的选择;
>     2. 返回值的选择；
>     3. 比较的逻辑。
### 实际应用
- 1.[求开方](https://leetcode.com/problems/sqrtx/description/)
> 一个数 `x `的开方 `sqrt `一定在` 0 ~ x `之间，并且满足 `sqrt == x / sqrt`。可以利用二分查找在 `0 ~ x `之间查找 `sqrt`。
- 2.[大于给定元素的最小元素](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)
- 3.[有序数组的 Single Element](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)
- 4.[第一个错误的版本](https://leetcode.com/problems/first-bad-version/description/)
- 5.[旋转数组的最小数字](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
- 6.[查找区间](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

### 小结
经过几道题型可以分析总结到，使用二分法去解决问题时，时间复杂度均为O(logN).
也许注意以下几点：
- 区间大小以及中间值的计算方式（计算值必须是整型！）。
- 循环的条件，何时可以等于，何时不可以等于（在提供的题型中，也就`求开方`和`寻找大于给定元素的最小元素`题型循环条件可以`l<=h`, 判断边界的最好办法根据小案例就是自行演算下）。
- 比较的过程中，何时可以搜索右区间，何时搜索左区间以及边界值。
- 返回值(考虑返回l还是h还是其他，实际问题实际分析)。