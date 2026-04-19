# 空间变异分析（Meuse）

- **理论导读**（区域化变量、平稳性、半变异与块金/基台/变程等）：[`spatial_variability_theory.md`](spatial_variability_theory.md)
- **可运行案例**：[`spatial_variability_meuse.ipynb`](spatial_variability_meuse.ipynb)

案例按 **与理论文档相同的教学顺序** 编排：动机 → 数据与对数变换 → 平稳性直觉（样点图）→ 半变异定义与示意曲线 → 经验半变异（Matheron）→ 模型拟合与对比 → 块金/基台/尺度及与克里金的衔接。运行后图件写入 [`outputs/`](../../outputs/)（含 `meuse_zinc_log_hist.png`），与 [`spatial_variability_theory.md`](spatial_variability_theory.md) 插图一致，可图文对照阅读。

环境与依赖见仓库根目录 [`README.md`](../../README.md)。
