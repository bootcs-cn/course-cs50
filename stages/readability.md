# Readability

## 背景

根据 Scholastic，E.B. White 的《夏洛特的网》适合 2-4 年级的阅读水平，而 Lois Lowry 的《记忆传授人》适合 8-12 年级的阅读水平。但是，是什么让一本书比另一本书的阅读水平更高呢？

很多"可读性测试"已经被开发出来，用于定义文本阅读水平的公式。其中一个这样的可读性测试是 **Coleman-Liau 指数**。Coleman-Liau 指数用于计算理解某段文本需要达到的（美国）年级水平。

公式如下：

$$
\text{index} = 0.0588 \times L - 0.296 \times S - 15.8
$$

其中：

- $L$ 是文本中每 100 个单词的平均字母数
- $S$ 是文本中每 100 个单词的平均句子数

## 任务

实现一个程序 `readability.c`，用于计算一段文本的 Coleman-Liau 指数。

## 规范

- 你的程序应该提示用户输入一段文本
- 你的程序应该计算该文本的 Coleman-Liau 指数
- 输出格式：
  - 如果指数小于 1，输出 "Before Grade 1"
  - 如果指数大于等于 16，输出 "Grade 16+"
  - 否则，输出 "Grade X"，其中 X 是计算出的年级（四舍五入到最近的整数）

### 定义

- **字母**：任何小写字符 a-z 或大写字符 A-Z
- **单词**：由空格分隔的任何字符序列（假设句子中不会有连续两个空格）
- **句子**：任何以句号（.）、感叹号（!）或问号（?）结尾的字符序列

## 示例

```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

```
$ ./readability
Text: One fish. Two fish. Red fish. Blue fish.
Before Grade 1
```

```
$ ./readability
Text: A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.
Grade 16+
```

## 提示

1. 使用 `get_string` 获取用户输入
2. 使用 `strlen` 计算字符串长度
3. 使用 `isalpha` 检查字符是否为字母
4. 使用 `round` 函数进行四舍五入（需要包含 `<math.h>`）
5. 编译时需要链接数学库：`clang -o readability readability.c -lcs50 -lm`

## 起始代码

```c
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    // TODO

    // Print the grade level
    // TODO
}

int count_letters(string text)
{
    // TODO
    return 0;
}

int count_words(string text)
{
    // TODO
    return 0;
}

int count_sentences(string text)
{
    // TODO
    return 0;
}
```
