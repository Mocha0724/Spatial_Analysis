# Spatial_Analysis — 综合空间分析案例仓库

本仓库收录多个 **空间分析** 主题的教学案例，每个案例包含理论导读（Markdown）与可运行的 Jupyter Notebook，使用 Python（`venv` + `requirements.txt` 管理依赖）。

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
```

若 `pip` 下载过慢，可使用国内 PyPI 镜像（示例：清华大学）：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 图表中的中文显示

各 Notebook 在配置 Matplotlib 时会优先搜索系统中安装的中文字体（如 macOS 的「苹方」/「冬青黑体」）。若在 **Linux** 上出现方框或 `Glyph ... missing` 警告，请安装字体包后重试：

```bash
# Debian/Ubuntu
sudo apt install fonts-noto-cjk
```

---

## 案例目录

| 案例 | 主题 | 数据 | Notebook |
|------|------|------|----------|
| [空间变异](cases/spatial-variability/) | 半变异函数与地统计结构 | Meuse 河漫滩土壤（荷兰） | [`spatial_variability_meuse.ipynb`](cases/spatial-variability/spatial_variability_meuse.ipynb) |
| [空间可达性](cases/spatial-accessibility/) | 医疗设施可达性度量 | 合成城市数据（可替换） | [`spatial_accessibility_analysis.ipynb`](cases/spatial-accessibility/spatial_accessibility_analysis.ipynb) |

---

## 仓库结构

```
Spatial_Analysis/
├── cases/
│   ├── spatial-variability/          # 空间变异案例
│   │   ├── README.md
│   │   ├── spatial_variability_theory.md
│   │   └── spatial_variability_meuse.ipynb
│   └── spatial-accessibility/        # 空间可达性案例
│       ├── README.md
│       ├── spatial_accessibility_theory.md
│       └── spatial_accessibility_analysis.ipynb
├── data/
│   ├── README.md
│   └── processed/
│       └── meuse.csv
├── outputs/
│   ├── spatial-variability/          # 空间变异案例输出图件
│   └── spatial-accessibility/        # 空间可达性案例输出图件
├── scripts/
│   ├── _build_notebook.py            # 生成空间变异 Notebook
│   ├── _build_notebook_accessibility.py   # 生成空间可达性 Notebook
│   └── download_meuse.py             # 下载并校验 Meuse 数据
└── requirements.txt
```

---

## 案例一：空间变异分析

**目录**：[`cases/spatial-variability/`](cases/spatial-variability/)

**数据**：Meuse 河漫滩土壤样点（`data/processed/meuse.csv`），区域化变量为 `log(锌)`。

```bash
# 下载或校验数据（仓库已含，也可重新获取）
python scripts/download_meuse.py

# 启动 Notebook
jupyter notebook cases/spatial-variability/spatial_variability_meuse.ipynb
```

**涵盖内容**：

1. **理论**：区域化变量、二阶平稳、内蕴假设、协方差与半变异关系  
2. **实践**：经验半变异（Matheron 估计）、球状/指数/高斯模型拟合（`gstools`）、块金/基台/有效相关距离解读

---

## 案例二：空间可达性分析

**目录**：[`cases/spatial-accessibility/`](cases/spatial-accessibility/)

**数据**：内置合成城市数据集（程序生成，无需额外下载），包含居住人口分区与医疗设施点，可替换为真实数据。

```bash
# 启动 Notebook（数据随 Notebook 内嵌生成，无需提前准备）
jupyter notebook cases/spatial-accessibility/spatial_accessibility_analysis.ipynb
```

**涵盖内容**：

1. **理论**：可达性定义与框架、三类度量方法  
2. **实践**：
   - 缓冲区法（Buffer）：阈值距离内的设施数量  
   - 引力模型（Gravity Model）：距离衰减加权可达性  
   - 两步移动搜寻法（2SFCA）：供需比累加可达性  
3. **可视化**：可达性空间分布图、方法对比图

---

## 参考文献（延伸阅读）

**空间变异 / 地统计**：

- Matheron, G. (1963). *Principles of geostatistics*.  
- Cressie, N. (1993). *Statistics for Spatial Data*. Wiley.  
- Chilès, J.-P., & Delfiner, P. (2012). *Geostatistics: Modeling Spatial Uncertainty*. Wiley.  
- Webster, R., & Oliver, M. A. (2007). *Geostatistics for Environmental Scientists*. Wiley.

**空间可达性**:

- Hansen, W. G. (1959). How accessibility shapes land use. *Journal of the American Institute of Planners*, 25(2), 73–76.  
- Radke, J., & Mu, L. (2000). Spatial decomposition, modeling and mapping service regions to predict access to social programs. *Geographic Information Sciences*, 6(2), 105–112.  
- Luo, W., & Wang, F. (2003). Measures of spatial accessibility to health care in a GIS environment. *Environment and Planning B*, 30(6), 865–884.  
- Luo, W., & Qi, Y. (2009). An enhanced two-step floating catchment area (E2SFCA) method for measuring spatial accessibility to primary care physicians. *Health & Place*, 15(4), 1100–1107.

## 许可

代码与文档以 [MIT License](LICENSE) 发布。数据集为公开教学常用数据，使用时请遵守相应数据政策并在文章中单独说明数据来源。
