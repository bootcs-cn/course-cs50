# Songs

## 背景

假设你在 Spotify 工作，需要分析 2018 年最热门的 100 首歌曲数据。你有一个 SQLite 数据库 `songs.db`，其中包含这些歌曲的信息。

## 数据库结构

数据库包含两个表：

### songs 表

| 列名         | 类型    | 描述                 |
| ------------ | ------- | -------------------- |
| id           | INTEGER | 歌曲唯一标识         |
| name         | TEXT    | 歌曲名称             |
| artist_id    | INTEGER | 艺术家 ID (外键)     |
| danceability | REAL    | 可舞性 (0.0-1.0)     |
| energy       | REAL    | 能量值 (0.0-1.0)     |
| key          | INTEGER | 调性 (0-11)          |
| loudness     | REAL    | 响度 (dB)            |
| speechiness  | REAL    | 语言性 (0.0-1.0)     |
| valence      | REAL    | 情绪积极度 (0.0-1.0) |
| tempo        | REAL    | 节奏 (BPM)           |
| duration_ms  | INTEGER | 时长 (毫秒)          |

### artists 表

| 列名 | 类型    | 描述           |
| ---- | ------- | -------------- |
| id   | INTEGER | 艺术家唯一标识 |
| name | TEXT    | 艺术家名称     |

## 任务

编写 SQL 查询来回答以下问题。每个查询保存在对应编号的 `.sql` 文件中。

### 1.sql

列出所有歌曲的名称。

### 2.sql

按节奏（tempo）升序列出所有歌曲的名称。

### 3.sql

列出时长最长的 5 首歌曲名称（按 duration_ms 降序）。

### 4.sql

列出可舞性（danceability）、能量值（energy）和情绪积极度（valence）都大于 0.75 的歌曲名称。

### 5.sql

计算所有歌曲的平均能量值。

### 6.sql

列出 Post Malone 的所有歌曲名称。

### 7.sql

计算 Drake 歌曲的平均能量值。

### 8.sql

列出名称中包含 "feat." 的歌曲名称。

## answers.txt

在 `answers.txt` 中回答以下问题（用几句话）：

- 你认为 Spotify 的这些音乐特征（如 danceability、energy）是如何计算的？
- 通过这些数据，你发现了 2018 年流行音乐的什么趋势？

## 示例

查询 1.sql 的输出示例：

```
God's Plan
SAD!
rockstar (feat. 21 Savage)
...
```

## 提示

<details>
<summary>点击查看提示</summary>

### 常用 SQL 语法

```sql
-- 选择所有列
SELECT * FROM songs;

-- 选择特定列
SELECT name FROM songs;

-- 条件过滤
SELECT name FROM songs WHERE energy > 0.8;

-- 排序
SELECT name FROM songs ORDER BY energy ASC;

-- 限制结果数量
SELECT name FROM songs ORDER BY energy DESC LIMIT 5;

-- 聚合函数
SELECT AVG(energy) FROM songs;

-- 多表连接
SELECT songs.name
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Drake';
```

</details>

## 参考资料

- [SQL 教程](https://www.w3schools.com/sql/)
- [SQLite 文档](https://www.sqlite.org/docs.html)
