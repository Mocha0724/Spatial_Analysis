---

# Hexo / Hugo 等静态博客：将下方字段映射为你站点的前言区（YAML / TOML）

## title: 空间变异分析实例：Meuse 土壤锌的半变异函数与模型拟合
date: 2026-04-18
tags:
  - geostatistics
  - variogram
  - Python
  - gstools

本文对应仓库：[Spatial_Analysis](https://github.com/Mocha0724/Spatial_Analysis)（案例路径：`cases/spatial-variability/spatial_variability_meuse.ipynb`）。

## 问题与目标

在给定点状土壤样点上，描述某重金属（本例为 **锌**）在空间上的 **变异结构**：随距离增加的 **半变异函数** 形态，以及 **块金**、**基台** 与 **变程尺度** 的可解释估计，为后续克里金或不确定性分析打基础。

## 数据与变量

采用荷兰 Meuse 河漫滩经典教学数据（R `sp::meuse` 体系）。区域化变量取 `**log(zinc)`**（ppm 的对数），与常见 `gstat` 教程一致。坐标为荷兰 RD（EPSG:28992）平面米制坐标。

数据获取与校验见仓库 `[data/README.md](../data/README.md)` 与 `[scripts/download_meuse.py](../scripts/download_meuse.py)`。

## 方法要点

1. **经验半变异**：对选定的滞后分箱，使用 Matheron 估计量得到 γ̂(h)。
2. **理论模型**：在球状、指数、高斯等候选模型中拟合 **块金 + 偏基台 + 相关长度**，并在 γ 域比较拟合残差（本 Notebook 以 RMS 作简单准则）。
3. **解释**：报告总基台（块金 + 部分基台）与 **有效相关距离** 的常用换算（依所选模型而异）。

## 结果图件（与仓库 `outputs/` 同步）

将下列文件复制到你的博客静态资源目录（例如 Hexo 的 `source/images/spatial-analysis/`），并相应修改图片路径。

样点与 log(锌)

经验半变异

模型拟合对比

## 本地复现

```bash
git clone git@github.com:Mocha0724/Spatial_Analysis.git
cd Spatial_Analysis
python3 -m venv .venv && source .venv/bin/activate   # Windows 使用 .venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_meuse.py
jupyter notebook cases/spatial-variability/spatial_variability_meuse.ipynb
```

## 参考文献（GB/T 7714 风格示例）

[1] MATHERON G. Principles of geostatistics[J]. *Economic Geology*, 1963, 58(8): 1246-1266.

[2] CRESSIE N. *Statistics for Spatial Data: Revised Edition*[M]. New York: Wiley, 1993.

[3] WEBSTER R, OLIVER M A. *Geostatistics for Environmental Scientists (2nd ed.)*[M]. Chichester: Wiley, 2007.

[4] ISAAKS E H, SRIVASTAVA R M. *An Introduction to Applied Geostatistics*[M]. New York: Oxford University Press, 1989.

[5] CHILÈS J P, DELFINER P. *Geostatistics: Modeling Spatial Uncertainty (2nd ed.)*[M]. Hoboken: Wiley, 2012.

（可按需要增补中文教材条目。）