#### 链表的基本介绍
链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表指针次序实现的。
链表的每个结点包括两个部分：一个是**存储数据元素的数据域**，另一个是**存储下一个结点地址的指针域**。
#### 操作效率的比较（数组、有序数组、链表、有序链表、二叉树、平衡二叉树、哈希表等）
- **无序数组**直接插在末尾，时间复杂度为`1`
- **有序数组**使用二分查找，时间复杂度`logN`
- **无序链表**插入在表尾，时间复杂度`1`
- **有序链表**插入需要寻找插入位置，时间复杂度`N`
- 二叉树一般情况即为平衡二叉树，最坏情况为有序链表
- 平衡二叉树删除时需要从被删除节点的父节点开始调节平衡一直调节到根节点，时间复杂度`O(logN)`
具体表一览如下：
![img](https://github.com/Cecilia520/algorithmic-learning-leetcode/blob/cecilia-python/cecilia-python/linkedlist/%E6%95%88%E7%8E%87%E8%A1%A8.png)
#### 相关操作
##### 建立链表
- **头插法**: 将元素插入链表头的后面
- **尾插法**: 将元素顺序插入链表当中
##### 逆序一个链表
- 非递归。需要三个辅助**变量前驱（pre）**，**当前节点（p）**，**后继节点（next）**
- 递归。递归到最后返回的时候，`p->next->next = p`;实现单次逆序，然后回溯最终整个链表逆序成功
- 头插
#### LeetCode经典题型
- [链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/)
- [链表倒置](https://leetcode-cn.com/problems/reverse-linked-list/description/)
- [合并链表（求并集）](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)
- [从有序链表中删除重复结点](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/)
- [删除链表的倒数第n个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/)
- [交换链表的相邻节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/)
- [链表求和](https://leetcode-cn.com/problems/add-two-numbers-ii/description/)
- [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/description/)
- [分格链表](https://leetcode-cn.com/problems/split-linked-list-in-parts/description/)
- [链表元素按奇偶聚集](https://leetcode-cn.com/problems/odd-even-linked-list/description/)

> 链表是空节点，或者有一个值和一个指向下一个链表的指针，因此很多链表问题可以用**递归**来处理。