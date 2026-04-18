# Spatial_Analysis — 空间变异分析案例仓库

以 **半变异函数 / 空间变异结构** 为核心的可复现 Python 示例（`venv` + `requirements.txt`），默认案例为 **Meuse 河漫滩土壤样点** 上的 `log(锌)`。

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

# 获取数据（或直接使用已提交的 data/processed/meuse.csv）
python scripts/download_meuse.py

# 在仓库根目录启动 Notebook
jupyter notebook cases/spatial-variability/spatial_variability_meuse.ipynb
```

若 `pip` 下载过慢，可使用国内 PyPI 镜像（示例：清华大学）：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 仓库结构


| 路径                                                         | 说明                       |
| ---------------------------------------------------------- | ------------------------ |
| `[cases/spatial-variability/](cases/spatial-variability/)` | 主 Notebook 与案例说明         |
| `[data/processed/meuse.csv](data/processed/meuse.csv)`     | Meuse 数据（可用脚本重新下载校验）     |
| `[scripts/download_meuse.py](scripts/download_meuse.py)`   | 数据下载与 SHA-256 校验         |
| `[outputs/](outputs/)`                                     | Notebook 导出的示例图（可重新运行生成） |
| `[docs/](docs/)`                                           | 面向个人博客的 Markdown 草稿      |


## 方法链条（首版范围）

1. 经验半变异（分箱、Matheron 估计）
2. 球状 / 指数 / 高斯模型拟合（`[gstools](https://geostat-framework.readthedocs.io/)`）
3. 解释 **块金（nugget）**、**部分基台 / 总基台**、**相关尺度（依模型换算的有效距离）**

未包含：各向异性、稳健变异函数、交叉验证与克里金插值（可作为后续扩展）。

## 参考文献（延伸阅读）

奠基与总论：

- Matheron, G. (1963). *Principles of geostatistics*.  
- Cressie, N. (1993). *Statistics for Spatial Data*. Wiley. [出版社页面](https://www.wiley.com/en-us/Statistics+for+Spatial+Data%2C+Revised+Edition-p-9780471002401)  
- Chilès, J.-P., & Delfiner, P. (2012). *Geostatistics: Modeling Spatial Uncertainty*. Wiley.

应用与教学：

- Webster, R., & Oliver, M. A. (2007). *Geostatistics for Environmental Scientists*. Wiley.  
- Isaaks, E. H., & Srivastava, R. M. (1989). *An Introduction to Applied Geostatistics*. Oxford University Press.

中文读者可自行补充常用「地统计学 / 空间统计分析」教材条目（GB/T 7714 或 APA 格式统一即可）。

## 许可

代码与文档以 [MIT License](LICENSE) 发布。数据集为公开教学常用数据，使用时请遵守相应数据政策并在文章中单独说明数据来源。