# 空间可达性分析案例

本案例以 **医疗设施可达性** 为场景，使用内置合成城市数据，系统演示三种主流空间可达性度量方法的原理与实现。

## 文件说明

| 文件 | 说明 |
|------|------|
| [`spatial_accessibility_theory.md`](spatial_accessibility_theory.md) | 理论导读：可达性框架、三类方法的公式推导与适用条件 |
| [`spatial_accessibility_analysis.ipynb`](spatial_accessibility_analysis.ipynb) | 主 Notebook：数据生成、方法实现、可视化与对比分析 |

## 快速运行

```bash
# 在仓库根目录激活环境后启动 Notebook
source .venv/bin/activate
jupyter notebook cases/spatial-accessibility/spatial_accessibility_analysis.ipynb
```

数据由 Notebook 内嵌代码生成，无需提前下载。

## 本案例涵盖内容

1. **理论**：Hansen 可达性势模型、引力模型的距离衰减形式、两步移动搜寻法（2SFCA）的供需比逻辑——详见 [`spatial_accessibility_theory.md`](spatial_accessibility_theory.md)。
2. **实践**：
   - **缓冲区法**（Buffer）：阈值距离内设施数量
   - **引力模型**（Gravity Model）：$A_i = \sum_j \frac{S_j}{d_{ij}^\beta}$
   - **两步移动搜寻法**（2SFCA）：分步计算供需比并累加
3. **可视化**：三种方法的可达性空间分布图、全局相关性对比

## 与相邻案例的关系

与 [`../spatial-variability/`](../spatial-variability/) 的主要差异：

| 维度 | 空间变异 | 空间可达性 |
|------|----------|------------|
| 核心问题 | 空间相关结构的估计与建模 | 点/区域对设施的接近程度度量 |
| 关键工具 | `gstools`（变异函数） | `scipy`、`numpy`（距离与加权计算） |
| 典型应用 | 克里金插值、地统计模拟 | 公共服务规划、区域公平分析 |

产出图件保存在 [`../../outputs/spatial-accessibility/`](../../outputs/spatial-accessibility/)。
