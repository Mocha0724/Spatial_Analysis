# Spatial_Analysis — 空间变异分析案例仓库

本仓库提供基于 **半变异函数** 的 **空间变异结构** 分析示例：使用 Python（`venv` 与 `requirements.txt` 管理依赖），案例数据为 **Meuse 河漫滩土壤样点**，区域化变量为 **`log(锌)`**（ppm 的对数）。

## 快速开始

```bash
git clone git@github.com:Mocha0724/Spatial_Analysis.git
cd Spatial_Analysis

python3 -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows (cmd):
# .venv\Scripts\activate.bat

pip install -U pip
pip install -r requirements.txt

# 获取数据（仓库已含 data/processed/meuse.csv，也可重新下载并校验）
python scripts/download_meuse.py

# 在仓库根目录启动 Notebook
jupyter notebook cases/spatial-variability/spatial_variability_meuse.ipynb
```

若 `pip` 下载过慢，可使用国内 PyPI 镜像（示例：清华大学）：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 图表中的中文显示

Notebook 在 `plt.style.use("seaborn-v0_8-whitegrid")` **之后**会重新指定带中日韩字形的系统字体（如 macOS 的「苹方」/「冬青黑体」等），避免 Matplotlib 默认落到 Arial 上出现缺字与 `Glyph ... missing from font(s) Arial` 警告。

若在 **Linux** 上仍出现方框或警告，请安装任一字体包后重试，例如 Debian/Ubuntu：`sudo apt install fonts-noto-cjk`。在无图形服务器环境下批量执行 Notebook 时，可将 Matplotlib 配置目录指到可写路径，例如：

```bash
export MPLCONFIGDIR="$PWD/.mplconfig"
jupyter nbconvert --execute cases/spatial-variability/spatial_variability_meuse.ipynb --inplace
```

## 仓库结构

| 路径 | 说明 |
|------|------|
| [`cases/spatial-variability/`](cases/spatial-variability/) | 理论导读（Markdown）、主 Notebook 与案例说明 |
| [`data/processed/meuse.csv`](data/processed/meuse.csv) | Meuse 数据表；亦可由脚本重新下载并校验 |
| [`scripts/download_meuse.py`](scripts/download_meuse.py) | 数据下载与完整性校验（SHA-256） |
| [`outputs/`](outputs/) | 与 Notebook 一致的示例图（运行 Notebook 可重新生成） |

## 本案例涵盖的内容

1. **理论**：区域化变量、平稳性、协方差与半变异的关系、经验估计与参数含义——见 [`cases/spatial-variability/spatial_variability_theory.md`](cases/spatial-variability/spatial_variability_theory.md)。
2. **实践**：经验半变异（分箱、Matheron 估计）、球状 / 指数 / 高斯模型拟合（[`gstools`](https://geostat-framework.readthedocs.io/)）、**块金**、**部分基台 / 总基台**、**相关尺度**（含按模型换算的有效距离）的解读。

各向异性变异函数、稳健估计、交叉验证以及克里金插值等主题未在本例代码中展开，可在标准地统计教材与文献中延伸学习。

## 参考文献（延伸阅读）

奠基与总论：

- Matheron, G. (1963). *Principles of geostatistics*.  
- Cressie, N. (1993). *Statistics for Spatial Data*. Wiley. [出版社页面](https://www.wiley.com/en-us/Statistics+for+Spatial+Data%2C+Revised+Edition-p-9780471002401)  
- Chilès, J.-P., & Delfiner, P. (2012). *Geostatistics: Modeling Spatial Uncertainty*. Wiley.

应用与教学：

- Webster, R., & Oliver, M. A. (2007). *Geostatistics for Environmental Scientists*. Wiley.  
- Isaaks, E. H., & Srivastava, R. M. (1989). *An Introduction to Applied Geostatistics*. Oxford University Press.

中文教材或译著可按 GB/T 7714、APA 等惯例另行著录。

## 许可

代码与文档以 [MIT License](LICENSE) 发布。数据集为公开教学常用数据，使用时请遵守相应数据政策并在文章中单独说明数据来源。