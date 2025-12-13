# bootcs-cli CS50 Course Image
# 包含 CS50 课程的检查脚本

FROM ghcr.io/bootcs-cn/bootcs-cli:latest

LABEL org.opencontainers.image.source="https://github.com/bootcs-cn/bootcs-cli"
LABEL org.opencontainers.image.description="BootCS CLI with CS50 course checks"

# 复制检查脚本
COPY checks/ /checks/

# 复制评测脚本
COPY --from=ghcr.io/bootcs-cn/bootcs-cli:latest /app/scripts/bootcs-evaluate.sh /usr/local/bin/bootcs-evaluate
RUN chmod +x /usr/local/bin/bootcs-evaluate || true

# 工作目录
WORKDIR /workspace

# 入口点
ENTRYPOINT ["python", "-m", "bootcs"]
CMD ["--help"]
