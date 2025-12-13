# Hello

## 背景

这是你的第一个 C 程序！你将学习如何获取用户输入并输出问候语。

## 任务

实现一个程序 `hello.c`，提示用户输入名字，然后打印 `hello, {name}`。

## 示例

```
$ ./hello
What is your name? Emma
hello, Emma
```

```
$ ./hello
What is your name? Rodrigo
hello, Rodrigo
```

## 规范

1. 程序必须命名为 `hello.c`
2. 使用 `get_string` 提示用户输入名字
3. 输出格式为 `hello, {name}\n`

## 提示

<details>
<summary>点击查看提示</summary>

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What is your name? ");
    printf("hello, %s\n", name);
}
```

</details>

## 参考资料

- [Lecture 1: C](https://cs50.harvard.edu/x/2024/weeks/1/)
- [get_string Manual](https://manual.cs50.io/3/get_string)
