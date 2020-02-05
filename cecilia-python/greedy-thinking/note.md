#### 认识贪心算法
贪心算法没有固定的算法框架，设计的关键在于贪心策略的选择。贪心策略使用的前提是局部最优能导致全局最优。需要注意的是，贪心算法不是对所有问题都能得到整体最优解，选择的贪心策略必须具备**无后效性**，即某个状态以后的过程不会影响以前的状态，只与当前状态有关。所以对所采用的贪心策略一定要仔细分析其是否满足无后效性。
#### 注意点
- 利用贪心算法解决问题时需要解决以下两个问题：

- - （1）该问题是否适合贪心策略求解。

- - （2）如何选择贪心标准，以得到问题的最优/较优解。

- 贪心算法存在如下问题：

- - （1）不能保证解释最佳的。因为贪心算法总是从局部出发，并没有从整体考虑。

- - （2）贪心算法一般用来解决求最大或最小解。

- - （3）贪心算法只能确定某些问题的可行性范围。

#### 贪心算法思想
贪心算法的基本思路就是从问题的一个最初的解出发一步一步地进行，根据某个优化测度，每一步都要确保能获得局部最优解。每一步只考虑一个数据，他的选取应该满足局部优化的条件。若下一个数据和部分最优解连在一起不再是可行解时，就不把该数据添加到部分解中，直到把所有数据枚举完，或者不能再添加算法停止。
##### 过程
- 建立数学模型来描述问题；
- 把求解的问题分成若干个子问题；
- 对每一子问题求解，得到子问题的局部最优解；
- 把子问题的解局部最优解合成原来解问题的一个解。
#### 实际应用
- 求最小生成树的Prim算法和Kruskal算法都是漂亮的贪心算法。
- 贪心算法和很多的智能算法一起结合使用，比单纯的贪心算法更靠近了最优解。例如遗传算法，模拟退火算法。
#### 题型
- [分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)
- [无重叠空间](https://leetcode-cn.com/problems/non-overlapping-intervals/description/)
- [用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)
- [根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/)
- [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/)
- [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
- [种花问题](https://leetcode-cn.com/problems/can-place-flowers/description/)
- [判断是否是子序列](https://leetcode-cn.com/problems/is-subsequence/description/)
- [修改一个数成为非递减数组](https://leetcode-cn.com/problems/non-decreasing-array/description/)
- [子数组最大的和](https://leetcode-cn.com/problems/maximum-subarray/description/)
- [分隔字符串使同种字符出现在一起](https://leetcode-cn.com/problems/partition-labels/description/)
