# course-cs50

CS50 课程包，用于 BootCS 平台。

## 结构

```
course-cs50/
├── course.yml              # 课程元信息
├── README.md               # 课程详细介绍
├── stages/                 # 阶段定义
│   ├── hello.yml + .md
│   ├── mario-less.yml + .md
│   └── cash.yml + .md
├── checks/                 # 评测脚本 (bootcs-cli 格式)
│   ├── hello/
│   ├── mario-less/
│   └── cash/
├── starters/               # 起始代码模板
│   ├── hello/
│   ├── mario-less/
│   └── cash/
└── .github/workflows/
    └── sync.yml            # 同步到 bootcs-api
```

## 本地测试

```bash
# 安装 bootcs-cli
npm install -g bootcs

# 测试 hello 阶段
cd starters/hello
bootcs check ../checks/hello
```

## 添加新阶段

1. 在 `stages/` 创建 `{slug}.yml` 和 `{slug}.md`
2. 在 `checks/{slug}/` 创建 `checks.ts`
3. 在 `starters/{slug}/` 创建起始代码
4. 在 `course.yml` 的 `stage_order` 中添加 slug
5. 提交并推送到 main 分支

## 同步配置

需要在仓库 Secrets 中配置：

- `BOOTCS_API_URL`: API 地址
- `SYNC_SECRET`: 同步密钥
