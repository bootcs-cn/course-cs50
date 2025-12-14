# Me

## 目标

实现一个程序，提示用户输入名字，然后输出 `hello, [name]`，其中 `[name]` 是用户输入的名字。

## 规范

- 程序文件名必须是 `hello.c`
- 程序应提示用户输入名字
- 输出格式必须是 `hello, [name]`，后跟换行符
- `hello` 的 `h` 可以是大写或小写

## 示例

```
$ ./hello
What is your name? Mario
hello, Mario
```

```
$ ./hello
What is your name? Peach
hello, Peach
```

## 提示

1. 使用 `get_string` 函数获取用户输入
2. 使用 `printf` 和 `%s` 格式化字符串输出

## 如何测试

```bash
bootcs check cs50/me
```
