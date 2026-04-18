# 空间变异分析（Meuse）

- **理论导读**（区域化变量、平稳性、半变异与块金/基台/变程等）：[`spatial_variability_theory.md`](spatial_variability_theory.md)
- **可运行案例**：[`spatial_variability_meuse.ipynb`](spatial_variability_meuse.ipynb)

案例流程概览：数据加载 → 以 `log(zinc)` 为区域化变量 → 经验半变异（Matheron）→ 球状 / 指数 / 高斯模型拟合 → 块金、基台与有效相关距离的解读。

环境与依赖见仓库根目录 [`README.md`](../../README.md)。
