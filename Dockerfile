# 基础镜像：使用轻量的 Python 3.12 镜像
FROM python:3.12-slim

# 设置工作目录（避免文件混乱）
WORKDIR /app

# 复制依赖清单并安装（利用 Docker 缓存，依赖不变时不重复安装）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有代码到工作目录
COPY . .

# 容器启动命令：运行 app.py
CMD ["python", "app/app.py"]