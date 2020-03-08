### 栈和队列知识点梳理
#### 栈
栈是一种只能从表的一端存取数据且遵循 `"先进后出"` 原则的线性存储结构。
通常，栈的开口端被称为栈顶；相应地，封口端被称为栈底。因此，栈顶元素指的就是距离栈顶最近的元素
- 栈的具体实现有以下两种方式：
- - **顺序栈**：采用顺序存储结构可以模拟栈存储数据的特点，从而实现栈存储结构；
- - **链栈**：采用链式存储结构实现栈结构。
> 两种实现方式的区别，仅限于数据元素在实际物理空间上存放的相对位置，顺序栈底层采用的是`数组`，链栈底层采用的是`链表`。
- 应用
- - **浏览器 "回退" 功能**的实现，底层使用的就是栈存储结构；
- - 可以帮我们**检测代码中的括号匹配**问题。
- - 栈结构还可以**实现数值的进制转换**功能。例如，编写程序实现从十进制数自动转换成二进制数，就可以使用栈存储结构来实现。
#### 队列
队列是一种遵循 `"先进先出"` 的原则的线性存储结构。
- 队列存储结构的实现有以下两种方式：
- - **顺序队列**：在顺序表的基础上实现的队列结构；
- - **链队列**：在链表的基础上实现的队列结构；
> 两者的区别仅是顺序表和链表的区别，即在实际的物理空间中，数据集中存储的队列是顺序队列，分散存储的队列是链队列。
- 应用：实际生活中，队列的应用随处可见。比如排队买 XXX、医院的挂号系统等，采用的都是队列的结构。

### 常见Leetcode题型
- [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/description/)
- [用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/description/)
- [最小值栈](https://leetcode-cn.com/problems/min-stack/description/)
- [用栈实现括号匹配](https://leetcode-cn.com/problems/valid-parentheses/description/)
- [数组中元素比它下一个大的距离](https://leetcode-cn.com/problems/daily-temperatures/description/)
- [循环数组中比当前元素大的下一个元素](https://leetcode-cn.com/problems/next-greater-element-ii/description/)