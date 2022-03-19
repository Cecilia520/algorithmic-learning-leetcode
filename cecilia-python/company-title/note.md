根据往年的算法笔试题和今年已经经历过的一些题目来看，考察最多的类型题目就是**动态规划、回溯法、分治法以及贪心算法**等类型的算法题目。因此，针对以上做了基本的小结：
#### 递归与分治法
直接或间接地调用自身的算法称为**递归算法**。 递归是算法设计与分析中经常使用的一种技术，描写叙述简单且易于理解。

**分治法**的设计思想是将一个规模为n难以解决的问题分解为k个规模较小的子问题，这些子问题**相互独立且与原问题同样**。
递归地解这些子问题，然后将各子问题的解合并得到原问题的解。

> 典型样例：**Fibonacci数列，阶乘，Hanoi塔；二分法搜索、高速排序、合并排序**。

#### 动态规划法
动态规划过程是：依据当前（阶段）状态，采取对应的决策，引起状态的转移。例如以下，一个决策序列就是在变化的状态中产生出来的，这样的多阶段最优化决策解决这个问题的过程就称为动态规划。

    初始状态→│决策１│→│决策２│→…→│决策ｎ│→结束状态

动态规划算法与分治法类似，其思想也是将待求解问题分解成若干个子问题（一般每一个问题相应一个阶段），按顺序求解子阶段，前一子问题的解，为后一子问题的求解提供了实用的信息。
在求解任一子问题时，列出各种可能的局部解，通过决策保留那些有可能达到最优的局部解，丢弃其它局部解。依次解决各子问题，最后一个子问题就是初始问题的解。
    因为**动态规划解决的问题多数有重叠子问题这个特点，为降低反复计算，对每个子问题仅仅解一次，将其不同阶段的不同状态保存在一个二维数组中**。

与分治法最大的区别是：**适合于用动态规划法求解的问题，经分解后得到的子问题往往不是互相独立的（即下一个子阶段的求解是建立在上一个子阶段的解的基础上，进行进一步的求解）。**

> 典型样例：**最长公共子序列； 最大连续子序列和（最大m子段和）**。

#### 贪心算法
贪心算法在策略的运行过程中，总是做出对当前看来是最好的选择。也就是说贪心算法并不从整理最优上进行考虑，它所做出的选择仅仅是在某种意义上的局部最优选择。

**贪心算法不能保证找到的解是最优解，但在某些情况下能够是最优解的近似解，甚至是最优解**。

> 典型样例：**哈夫曼编码；单源最短路径（Dijkstra算法）；最小生成树（Prim和Kruskal算法）**

#### 回溯法 （DFS搜索解空间）
回溯法是以**深度优先方式**搜索问题解的算法，它适用于组合数较大的问题，能系统地搜索到一个问题的全部解惑任一解。
回溯法解题通常包括3个步骤：①针对所给的问题，定义问题的解空间；  ②确定易于搜索的解空间的结构； ③ 以DFS搜索解空间，并在搜索过程中用剪枝函数（约束条件）避免无效搜索。

解空间树：
- ①**子集树**：当所给问题是从n个元素的结合S中找出满足某种性质的子集时，对应的解空间树称为子集树。比如n个物品的0-1背包问题。这类子集树通常有2^n个叶节点，其节点总个数为为2^(n+1)-1。遍历子集树的不论什么算法均需O(2^n)的计算时间
- ②**排列树**：当所给问题是确定n个元素满足某种性质的排列时，对应的解空间树成为排列树。比如旅行售货员问题。排列树通常有n！个叶节点，因此遍历排列树须要O(n!)的计算时间。

搜索实现能够递归，也能够用树的非递归深度优先遍历算法来实现（用到**栈Stack**）。

> 典型样例：**八皇后（找出全部的解），N 皇后**

#### 分支界限法（BFS搜索解空间）
分支界限法的求解目标是找出满足约束条件的一个解，或是在满足约束条件的解中找出使某一目标函数值达到极大或极小的解，即在某种意义下的最优解。（**分支界限法与回溯法求解目标不同，求解方式也不同（前者是DFS，后者是BFS）**）

分支界限法以**广度优先或以最小耗费（最大收益）优先**的方式搜索解空间。所谓“分支”就是在扩展节点处，先生成其全部儿子节点（分支），然后在从当前的活结点表中选择下一个扩展节点，继续搜索。过程中能够用约束条件，进行剪枝。
常见的扩展节点的常见方式：先进先出FIFO队列 和 优先队列分支界限法。

> 典型样例：**单源最短路径**