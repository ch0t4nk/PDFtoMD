<div align="center">

<h1>MarkPDFDown</h1>
<p align="center"><a href="./README.md">English</a> | 中文 </p>

[![Size]][hub_url]
[![Pulls]][hub_url]
[![Tag]][tag_url]
[![License]][license_url]
<p>基于多模态大语言模型的PDF转Markdown工具，高质量实现文档结构化转换</p>

![markpdfdown](https://raw.githubusercontent.com/markpdfdown/markpdfdown/refs/heads/master/tests/markpdfdown.png)

</div>

## 项目概述

MarkPDFDown 是一款智能PDF转换Markdown工具，通过先进的多模态AI模型，能够将PDF文档准确转换为结构清晰的Markdown格式，保留原始文档的排版、表格、公式等复杂元素。

## 功能特性

- **PDF转Markdown**：支持任意PDF文档的格式转换
- **图片转Markdown**：支持JPG/PNG/BMP图片内容转Markdown
- **多模态理解**：利用AI理解文档结构和内容
- **格式保留**：完整保留标题、列表、表格等排版元素
- **模型定制**：支持自定义AI模型参数配置

## 示例演示
![](https://raw.githubusercontent.com/markpdfdown/markpdfdown/refs/heads/master/tests/demo.png)

## 安装指南

### 使用 uv（推荐）

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆仓库
git clone https://github.com/MarkPDFdown/markpdfdown.git
cd markpdfdown

# 安装依赖并创建虚拟环境
uv sync
```

### 使用 conda

```bash
conda create -n markpdfdown python=3.9
conda activate markpdfdown

# 克隆仓库
git clone https://github.com/MarkPDFdown/markpdfdown.git
cd markpdfdown

# 安装依赖
pip install -e .
```

## 使用指南
```bash
# 设置OpenAI API密钥
export OPENAI_API_KEY="你的API密钥"
# 可选设置API端点
export OPENAI_API_BASE="你的API端点"
# 可选设置默认模型
export OPENAI_DEFAULT_MODEL="你的模型"

# PDF转换Markdown
python main.py < input.pdf > output.md

# 图片转换Markdown
python main.py < input_image.png > output.md
```

## 高级用法
```bash
# 转换指定页码范围（限PDF）
python main.py 起始页码 结束页码 < input.pdf > output.md
```

## 在Docker中使用
```bash
docker run -i -e OPENAI_API_KEY=你的API密钥 -e OPENAI_API_BASE=你的API端点 -e OPENAI_DEFAULT_MODEL=你的模型 jorbenzhu/markpdfdown < input.pdf > output.md
```

## 开发环境设置

### 代码质量工具

本项目使用 `ruff` 进行代码检查和格式化，使用 `pre-commit` 进行自动化代码质量检查。

#### 安装开发依赖

```bash
# 如果使用 uv
uv sync --group dev

# 如果使用 pip
pip install -e ".[dev]"
```

#### 设置 pre-commit 钩子

```bash
# 安装 pre-commit 钩子
pre-commit install

# 在所有文件上运行 pre-commit（可选）
pre-commit run --all-files
```

#### 代码格式化和检查

```bash
# 使用 ruff 格式化代码
ruff format

# 运行代码检查
ruff check

# 修复可自动修复的问题
ruff check --fix
```

## 依赖环境
- Python 3.9+
- [uv](https://astral.sh/uv/)（推荐的包管理工具）或 conda/pip
- 项目依赖详见 `pyproject.toml`
- 可访问的多模态AI模型服务

## 贡献指南
欢迎贡献代码！请按以下流程提交PR：

1. Fork 本仓库
2. 新建功能分支（ `git checkout -b feature/somefeat` ）
3. 设置开发环境：
   ```bash
   uv sync --group dev
   pre-commit install
   ```
4. 进行修改并确保代码质量：
   ```bash
   ruff format
   ruff check --fix
   pre-commit run --all-files
   ```
5. 提交修改（ `git commit -m 'feat: 添加XX新功能'` ）
6. 推送分支（ `git push origin feature/somefeat` ）
7. 提交Pull Request

请确保在提交前运行代码检查和格式化工具，以符合项目的代码规范。

## 开源协议
本项目采用 Apache License 2.0 开源协议，详见 LICENSE 文件。

## 致谢
- 感谢多模态AI模型的技术支持
- 受PDF转Markdown工具需求启发而开发

[hub_url]: https://hub.docker.com/r/jorbenzhu/markpdfdown/
[tag_url]: https://github.com/markpdfdown/markpdfdown/releases
[license_url]: https://github.com/markpdfdown/markpdfdown/blob/main/LICENSE

[Size]: https://img.shields.io/docker/image-size/jorbenzhu/markpdfdown/latest?color=066da5&label=size
[Pulls]: https://img.shields.io/docker/pulls/jorbenzhu/markpdfdown.svg?style=flat&label=pulls&logo=docker
[Tag]: https://img.shields.io/github/release/markpdfdown/markpdfdown.svg
[License]: https://img.shields.io/github/license/markpdfdown/markpdfdown
