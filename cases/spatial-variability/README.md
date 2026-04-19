# 空间变异分析案例

本案例以 **Meuse 河漫滩土壤重金属污染** 为场景，系统演示半变异函数建模的完整流程。

## 文件说明

| 文件 | 说明 |
|------|------|
| [`spatial_variability_theory.md`](spatial_variability_theory.md) | 理论导读：区域化变量、平稳性、协方差/半变异公式推导与参数含义 |
| [`spatial_variability_meuse.ipynb`](spatial_variability_meuse.ipynb) | 主 Notebook：数据探索、经验半变异估计、三种模型拟合与参数解读 |

## 快速运行

```bash
# 获取数据（仓库已含，也可重新下载并校验 SHA-256）
python scripts/download_meuse.py

# 在仓库根目录激活环境后启动 Notebook
source .venv/bin/activate
jupyter notebook cases/spatial-variability/spatial_variability_meuse.ipynb
```

## 本案例涵盖内容

1. **理论**：区域化变量、二阶平稳与内蕴假设、协方差与半变异函数关系——见 [`spatial_variability_theory.md`](spatial_variability_theory.md)。
2. **实践**：
   - 数据（Meuse，EPSG:28992）读取与对数变换
   - 经验半变异（Matheron 估计，`gstools.vario_estimate`）
   - 球状 / 指数 / 高斯三种模型拟合（`fit_variogram`）
   - 块金、部分基台、总基台、有效相关距离解读

## 与相邻案例的关系

| 维度 | 空间变异 | 空间可达性 |
|------|----------|------------|
| 核心问题 | 空间相关结构的估计与建模 | 点/区域对设施的接近程度度量 |
| 关键工具 | `gstools`（变异函数） | `scipy`（距离与加权计算） |
| 典型应用 | 克里金插值、地统计模拟 | 公共服务规划、区域公平分析 |

产出图件保存在 [`../../outputs/spatial-variability/`](../../outputs/spatial-variability/)。
