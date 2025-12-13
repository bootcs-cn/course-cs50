# Cash

## 背景

当你在商店购物时，收银员需要找零。如何用最少的硬币找零呢？这就是贪心算法的经典应用！

美国常用硬币面值：

- 25 分 (quarter)
- 10 分 (dime)
- 5 分 (nickel)
- 1 分 (penny)

## 任务

实现一个程序 `cash.c`，计算找零所需的最少硬币数量。

## 示例

```
$ ./cash
Change owed: 41
4
```

（41 分 = 25 + 10 + 5 + 1 = 4 枚硬币）

```
$ ./cash
Change owed: 1
1
```

```
$ ./cash
Change owed: 15
2
```

（15 分 = 10 + 5 = 2 枚硬币）

## 规范

1. 程序必须命名为 `cash.c`
2. 提示用户输入找零金额（正整数，单位为分）
3. 如果用户输入负数，程序应重新提示
4. 输出最少硬币数量

## 贪心算法

始终优先使用最大面值的硬币：

1. 尽可能多用 25 分硬币
2. 剩余金额尽可能多用 10 分硬币
3. 剩余金额尽可能多用 5 分硬币
4. 剩余金额用 1 分硬币

## 提示

<details>
<summary>点击查看提示</summary>

```c
int coins = 0;

// 25 分硬币
coins += cents / 25;
cents %= 25;

// 10 分硬币
coins += cents / 10;
cents %= 10;

// 以此类推...
```

</details>

## 参考资料

- [Lecture 1: C](https://cs50.harvard.edu/x/2024/weeks/1/)
- [Greedy Algorithms](https://cs50.harvard.edu/x/2024/shorts/greedy_algorithms/)
