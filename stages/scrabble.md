# Scrabble

## 背景

在 Scrabble 游戏中，玩家用字母拼成单词，并根据每个字母的分值来计算单词的总分。

每个字母的分值如下：

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 3   | 3   | 2   | 1   | 4   | 2   | 4   | 1   | 8   | 5   | 1   | 3   | 1   | 1   | 3   | 10  | 1   | 1   | 1   | 1   | 4   | 4   | 8   | 4   | 10  |

例如，如果我们想计算单词 "CODE" 的分值：

- 'C' = 3 分
- 'O' = 1 分
- 'D' = 2 分
- 'E' = 1 分

总分 = 3 + 1 + 2 + 1 = 7 分

## 任务

实现一个程序 `scrabble.c`，用于判断两名 Scrabble 玩家中谁是赢家。

你的程序应该：

1. 提示用户输入玩家 1 的单词
2. 提示用户输入玩家 2 的单词
3. 根据每个单词中字母的 Scrabble 分值计算总分
4. 输出赢家，或者如果平局则输出 "Tie!"

## 规范

- 你的程序需要处理大小写字母（大小写字母的分值相同）
- 非字母字符应该忽略（不计分）
- 输出格式：
  - 如果玩家 1 获胜：输出 "Player 1 wins!"
  - 如果玩家 2 获胜：输出 "Player 2 wins!"
  - 如果平局：输出 "Tie!"

## 示例

```
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```
$ ./scrabble
Player 1: Oh,
Player 2: hai!
Player 2 wins!
```

```
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

## 提示

1. 你可以使用数组来存储每个字母的分值
2. 使用 `tolower()` 或 `toupper()` 函数来统一处理大小写
3. 使用 `isalpha()` 函数来判断字符是否为字母
4. 记得包含 `<ctype.h>` 头文件来使用这些函数

## 起始代码

```c
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    // TODO
}

int compute_score(string word)
{
    // TODO
}
```
