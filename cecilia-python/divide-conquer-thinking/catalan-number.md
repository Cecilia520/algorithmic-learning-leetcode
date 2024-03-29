### 起源介绍

根据百度百科介绍，卡特兰数又称卡塔兰数，英文名Catalan number，是组合数学中一个常出现在各种计数问题中出现的数列。
以比利时的数学家欧仁·查理·卡塔兰 (1814–1894)的名字来命名，其前几项为（从第零项开始） :
'''
1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650,
1289904147324, 4861946401452, ...
'''

### 原理

$$
设h(n)为catalan数的第n+1项，令h(0)=1,h(1)=1，catalan数满足递推式：\\

h(n)= h(0)*h(n-1)+h(1)*h(n-2) + \cdot\cdot\cdot + h(n-1)*h(0) (n>=2)\\

例如：

h(2)=h(0)*h(1)+h(1)*h(0)=1*1+1*1=2\\

h(3)=h(0)*h(2)+h(1)*h(1)+h(2)*h(0)=1*2+1*1+2*1=5
$$



另类递推式：
$$
h(n)=h(n-1)*(4n-2)(n+1)
$$
递推关系的解为：
$$
h(n)=\frac{C_{2n}^{n}}{n+1}
= C_{2n}^{n}-C_{2n}^{n-1}\\
.s.t (n=0,1,2,...)
$$

### 应用案例

##### 求**括号化**的数量

> 矩阵连乘： P=a1×a2×a3×……×an，依据乘法结合律，不改变其顺序，只用括号表示成对的乘积，试问有几种括号化的方案？(h(n)种)

##### **计算出栈次序**

> 一个栈(无穷大)的[进栈](https://baike.baidu.com/item/%E8%BF%9B%E6%A0%88)序列为1，2，3，…，n，有多少个不同的[出栈](https://baike.baidu.com/item/%E5%87%BA%E6%A0%88)序列?

##### 买票找零

> 有2n个人排成一行进入剧场。入场费5元。其中只有n个人有一张5元钞票，另外n人只有10元钞票，剧院无其它钞票，问有多少种方法使得只要有10元的人买票，售票处就有5元的钞票找零？(将持5元者到达视作将5元入栈，持10元者到达视作使栈中某5元出栈)

##### **凸多边形三角划分**

> 在一个[凸多边形](https://baike.baidu.com/item/%E5%87%B8%E5%A4%9A%E8%BE%B9%E5%BD%A2)中，通过若干条互不相交的对角线，把这个多边形划分成了若干个三角形。任务是键盘上输入凸多边形的边数n，求不同划分的方案数f（n）。比如当n=6时，f（6）=14。
>
> 分析：
>
> 因为凸多边形的任意一条边必定属于某一个三角形，所以我们以某一条边为基准，以这条边的两个顶点为起点P1和终点Pn（P即Point），将该凸多边形的顶点依序标记为P1、P2、……、Pn，再在该凸多边形中找任意一个不属于这两个点的顶点Pk（2<=k<=n-1），来构成一个三角形，用这个三角形把一个凸多边形划分成两个凸多边形，其中一个凸多边形，是由P1，P2，……，Pk构成的凸k边形（顶点数即是边数），另一个凸多边形，是由Pk，Pk+1，……，Pn构成的凸n-k+1边形。
>
> 此时，我们若把Pk视为确定一点，那么根据[乘法原理](https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E5%8E%9F%E7%90%86)，f（n）的问题就等价于——凸k多边形的划分方案数乘以凸n-k+1多边形的划分方案数，即选择Pk这个顶点的f（n）=f（k）×f（n-k+1）。而k可以选2到n-1，所以再根据加法原理，将k取不同值的划分方案相加，得到的总方案数为：f（n）=f（2）f（n-2+1）+f（3）f（n-3+1）+……+f（n-1）f（2）。看到此处，再看看卡特兰数的递推式，答案不言而喻，即为f（n）=h（n-2） （n=2，3，4，……）。

##### **给定节点组成二叉搜索树**

> 给定N个[节点](https://baike.baidu.com/item/%E8%8A%82%E7%82%B9)，能构成多少种不同的[二叉搜索树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91)？
>
> （能构成h（N）个）
>
> （这个公式的下标是从h(0)=1开始的）

##### **n对括号正确匹配数目**

> 给定n对括号，求括号正确配对的字符串数，例如：
>
> 0对括号：[空序列] 1种可能
>
> 1对括号：() 1种可能
>
> 2对括号：()() (()) 2种可能
>
> 3对括号：((())) ()(()) ()()() (())() (()()) 5种可能
>
> 那么问题来了，n对括号有多少种正确配对的可能呢？
>
> 分析：
>
> 考虑n对括号时的任意一种配对方案，最后一个右括号有唯一的与之匹配的左括号，于是有唯一的表示A(B)，其中A和B也是合法的括号匹配序列
>
> 假设S(n)为n对括号的正确配对数目，那么有递推关系S(n)=S(0)S(n-1)+S(1)S(n-2) +...+S(n-1)S(0)，显然S(n)是卡特兰数。