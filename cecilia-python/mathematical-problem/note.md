### 数学和算法
数学研究的对象是数量和空间的关系，而算法，就是一种解决问题的方法。
### 常见应用案例
#### 素数分解
`素数`定义：如果一个数如果只能被 1 和它本身整除，那么这个数就是素数。
- [统计素数](https://leetcode.com/problems/count-primes/description/)
#### 整除
令 `x = 2m0 * 3m1 * 5m2 * 7m3 * 11m4 * …`
令 `y = 2n0 * 3n1 * 5n2 * 7n3 * 11n4 * …`
如果 `x` 整除 `y（y mod x == 0）`，则对于所有 `i，mi <= ni`。
#### 最大公约数和最小公倍数
- 求解最大公约数
```python
def gcb(a, b):
    if b == 0:
        returnvalue = a
    else:
        returnvalue = gcb(b, a % b)
    return returnvalue
```
- 求解最小公倍数。最小公倍数为两数的乘积除以最大公约数
```python
def gcb(a, b):
    if b == 0:
        returnvalue = a
    else:
        returnvalue = gcb(b, a % b)
    return returnvalue
            
def lcm(a, b):
    returnvalue = gcb(a,b)
    return a * b / returnvalue
```
- 使用位操作和减法求解最大公约数

对于 a 和 b 的最大公约数 f(a, b)，有：

- - 1.如果 a 和 b 均为偶数，f(a, b) = 2*f(a/2, b/2);
- - 2.如果 a 是偶数 b 是奇数，f(a, b) = f(a/2, b);
- - 3.如果 b 是偶数 a 是奇数，f(a, b) = f(a, b/2);
- - 4.如果 a 和 b 均为奇数，f(a, b) = f(b, a-b);
> 乘 2 和除 2 都可以转换为移位操作。
#### 进制转换
- [七进制转换](https://leetcode.com/problems/base-7/description/)
- [16进制转换](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/)
- [26进制转换](https://leetcode.com/problems/excel-sheet-column-title/description/)
#### 阶乘
- [统计阶乘尾部有多少个 0](https://leetcode.com/problems/factorial-trailing-zeroes/description/)
#### 字符串加减法
- [二进制加法](https://leetcode.com/problems/add-binary/description/)
- [字符串加法](https://leetcode.com/problems/add-strings/description/)
#### 相遇问题
- [改变数组元素使得所有数组元素都相等II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-i/description/)
- [改变数组元素使得所有数组元素都相等II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)
#### 多数投票问题
- [数组中出现次数多于 n / 2 的元素](https://leetcode.com/problems/majority-element/description/)
#### 其他
- [平方数](https://leetcode.com/problems/valid-perfect-square/description/)
- [3的n次方](https://leetcode.com/problems/power-of-three/description/)
- [乘积数组](https://leetcode.com/problems/product-of-array-except-self/description/)
- [找出数组中乘积最大的三个数](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)