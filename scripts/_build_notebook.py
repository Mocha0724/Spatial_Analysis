"""One-off builder for spatial_variability_meuse.ipynb (run from repo root)."""
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def md(s: str):
    return new_markdown_cell(s.strip())


def code(s: str):
    return new_code_cell(s.strip())


cells = []

cells.append(
    md(
        r"""# 空间变异分析：Meuse 河漫滩土壤锌（对数）半变异函数

本 Notebook 与 [`spatial_variability_theory.md`](spatial_variability_theory.md) **配套使用**：理论文档讲定义与假设，这里用数据走完 **经验曲线 → 模型拟合 → 读参数**。

**建议阅读顺序**：先浏览下文「教程结构」→ 需要公式时打开理论文档对应小节 → 自上而下运行全部代码单元。

---

**数据与变量**

- **数据**：荷兰 Meuse 河漫滩土壤样点（与 R `sp::meuse` 教学数据集一致；详见 [`data/README.md`](../../data/README.md)）。
- **区域化变量**：`log(zinc)`（ppm 的对数），减轻偏态、使方差更平稳，与常见 `gstat` 教程一致。
- **坐标**：`x`, `y` 为荷兰 RD（EPSG:28992，米），本例按 **平面欧氏距离** 计算滞后。
"""
    )
)

cells.append(
    code(
        r"""from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

import geopandas as gpd
import gstools as gs

plt.style.use("seaborn-v0_8-whitegrid")


def configure_matplotlib_chinese() -> None:
    # Pick a system font that includes CJK glyphs (avoids tofu boxes / glyph warnings).
    candidates = [
        "PingFang SC",
        "PingFang HK",
        "Hiragino Sans GB",
        "Songti SC",
        "STHeiti",
        "Heiti TC",
        "Arial Unicode MS",
        "Microsoft YaHei",
        "SimHei",
        "Noto Sans CJK SC",
    ]
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            mpl.rcParams["font.family"] = "sans-serif"
            mpl.rcParams["font.sans-serif"] = [name, "DejaVu Sans", "Arial", "Helvetica"]
            mpl.rcParams["axes.unicode_minus"] = False
            return
    mpl.rcParams["font.sans-serif"] = [*candidates, *mpl.rcParams["font.sans-serif"]]
    mpl.rcParams["axes.unicode_minus"] = False


configure_matplotlib_chinese()


def repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for p in (cwd, *cwd.parents):
        if (p / "requirements.txt").is_file() and (p / "data").is_dir():
            return p
    return cwd


ROOT = repo_root()
DATA = ROOT / "data" / "processed" / "meuse.csv"
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
"""
    )
)

cells.append(
    md(
        r"""## 教程结构（与理论文档的对应）

| 步骤 | Notebook 里做什么 | 理论文档 |
|------|-------------------|----------|
| 1 概念示意 | 下格绘制 **示意性** 半变异曲线（块金/基台/变程），与真实拟合数值无关 | [§6 块金、基台与变程](spatial_variability_theory.md#6-块金基台与变程各指什么) |
| 2 数据与样点分布 | 加载 CSV、取 `log(zinc)`、画样点专题图 | [§2 区域化变量](spatial_variability_theory.md#2-区域化变量与随机函数) |
| 3 经验半变异 | 分箱 + Matheron 估计得到 $\hat{\gamma}(h)$ | [§5 经验半变异](spatial_variability_theory.md#5-经验半变异与-matheron-估计) |
| 4 模型拟合 | 球状 / 指数 / 高斯，比较 RMS | [§7 常见模型](spatial_variability_theory.md#7-常见各向同性模型轮廓) |
| 5 读参数 | 块金、部分基台、有效距离换算 | [§6](spatial_variability_theory.md#6-块金基台与变程各指什么)、[§8 与克里金](spatial_variability_theory.md#8-与克里金的关系一句话) |

运行过程中生成的图会保存到仓库 [`outputs/`](../../outputs/)，便于报告或博客引用。
"""
    )
)

cells.append(
    code(
        r"""# 教学用示意图：有界球状型半变异曲线的块金 C0、总基台、变程 a（非本数据拟合结果）


def spherical_gamma(h, nugget, partial_sill, rng):
    # 球状模型半变异 γ(h)=C0+C1*[1.5*h/a-0.5*(h/a)^3]，h<=a；h>a 时为 C0+C1。
    h = np.asarray(h, dtype=float)
    C1 = partial_sill
    a = rng
    out = np.empty_like(h)
    m = h <= a
    out[m] = nugget + C1 * (1.5 * h[m] / a - 0.5 * (h[m] / a) ** 3)
    out[~m] = nugget + C1
    return out


h = np.linspace(0, 180, 250)
C0, C1, a = 0.12, 0.38, 70.0
g = spherical_gamma(h, C0, C1, a)

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(h, g, color="#2171b5", lw=2.5, label="示意 γ(h)")
ax.axhline(C0, color="#666", ls="--", lw=1)
ax.axhline(C0 + C1, color="#666", ls=":", lw=1)
ax.axvline(a, color="#666", ls="--", lw=1, alpha=0.85)
ax.fill_between(h, 0, g, alpha=0.12, color="#2171b5")
ax.set_xlim(0, 180)
ax.set_ylim(0, C0 + C1 + 0.06)
ax.set_xlabel("滞后距离 h（示意单位）")
ax.set_ylabel("γ(h)")
ax.set_title("半变异曲线参数示意（球状型；教学用）")
ax.annotate("块金 C₀", xy=(8, C0 + 0.02), fontsize=10, color="#333")
ax.annotate("总基台 C₀+C₁", xy=(120, C0 + C1 - 0.05), fontsize=10, color="#333")
ax.annotate("变程 a", xy=(a + 3, 0.04), fontsize=10, color="#333")
ax.legend(loc="lower right")
fig.tight_layout()
fig.savefig(OUT / "semivariogram_concept.png", dpi=150)
plt.show()
"""
    )
)

cells.append(
    md(
        r"""## 1. 数据与区域化变量

将每个样点上的锌浓度视为区域化变量的一次实现；对 **`zinc` 取自然对数** 得到 `log_zinc`，使分布更接近对称、便于用二阶矩描述空间结构（详见理论文档 [§4](spatial_variability_theory.md#4-协方差函数与变异函数)）。

下表为前几行预览；完整数据见 `data/processed/meuse.csv`。
"""
    )
)

cells.append(
    code(
        r"""df = pd.read_csv(DATA)
df["log_zinc"] = np.log(df["zinc"])
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["x"], df["y"]),
    crs="EPSG:28992",
)
gdf.head()
"""
    )
)

cells.append(
    md(
        r"""## 2. 样点空间分布（探索性）

下图用颜色表示 **log(锌)**：先看是否存在明显 **趋势或分区**（若整体随某一方向漂移，可能需要去趋势或泛克里金——本例只做基础半变异估计）。颜色仅辅助眼睛，**半变异仍基于点对距离** 计算。
"""
    )
)

cells.append(
    code(
        r"""fig, ax = plt.subplots(figsize=(6, 5))
sc = ax.scatter(
    gdf["x"],
    gdf["y"],
    c=gdf["log_zinc"],
    cmap="viridis",
    s=35,
    edgecolor="k",
    linewidths=0.3,
)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x (m, RD)")
ax.set_ylabel("y (m, RD)")
cb = plt.colorbar(sc, ax=ax, shrink=0.85)
cb.set_label("log(Zn), ppm (log scale)")
ax.set_title("Meuse 样点与 log(锌) 分布")
fig.tight_layout()
fig.savefig(OUT / "meuse_logzn_points.png", dpi=150)
plt.show()
"""
    )
)

cells.append(
    md(
        r"""## 3. 经验半变异（Matheron）

在 **各向同性** 假设下，把所有点对的距离分成若干 **滞后箱**，对每个箱内的点对用 Matheron 公式估计 $\hat{\gamma}(h)$（理论见 [§5](spatial_variability_theory.md#5-经验半变异与-matheron-估计)）。

- `max_lag`：考虑的最大距离（过大则点对稀少、估计不稳）。
- `width`：箱宽（过大则曲线过粗，过小则噪声大）。

下面打印前几个箱的中心、$\hat{\gamma}$ 与点对数 **counts**，便于检查是否有空箱。
"""
    )
)

cells.append(
    code(
        r"""pos = np.array([gdf["x"].to_numpy(), gdf["y"].to_numpy()])
field = gdf["log_zinc"].to_numpy()

max_lag = 1600.0
width = 90.0
bin_edges = np.arange(width, max_lag + width, width)

bin_center, emp_gamma, counts = gs.vario_estimate(
    pos,
    field,
    bin_edges,
    estimator="matheron",
    mesh_type="unstructured",
    return_counts=True,
)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(bin_center, emp_gamma, "o", color="0.2", label="经验半变异")
ax.set_xlabel("滞后距离 h (m)")
ax.set_ylabel("γ̂(h)")
ax.set_title("经验半变异（Matheron 估计）")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "empirical_variogram.png", dpi=150)
plt.show()

list(zip(np.round(bin_center).astype(int), np.round(emp_gamma, 4), counts))[:8]
"""
    )
)

cells.append(
    md(
        r"""## 4. 理论模型拟合（球状 / 指数 / 高斯）

在常见 **各向同性** 参数族中搜索参数，使模型曲线在经验点处尽量接近（本例用 **RMS** 作简单比较指标）。三类模型形状差异见理论文档 [§7](spatial_variability_theory.md#7-常见各向同性模型轮廓)。

**注意**：`gstools` 中 `len_scale` 的含义随模型略有不同，解读「有效相关距离」时需按模型换算（见下一格打印）。
"""
    )
)

cells.append(
    code(
        r"""candidates = {
    "Spherical": gs.Spherical(dim=2),
    "Exponential": gs.Exponential(dim=2),
    "Gaussian": gs.Gaussian(dim=2),
}

fits = {}
for name, model in candidates.items():
    m = model
    m.fit_variogram(bin_center, emp_gamma, nugget=True)
    fits[name] = m
    print(
        f"{name:12s}  nugget={m.nugget:.4f}  partial_sill={m.var:.4f}  len_scale={m.len_scale:.1f} m"
    )
"""
    )
)

cells.append(
    md(
        r"""## 5. 拟合曲线对比图

- **散点**：经验 $\hat{\gamma}(h)$。
- **实线**：按 RMS 最优的模型（颜色与图例）。
- **虚线**：其余候选模型，便于对比形状差异。

若最优线与散点系统偏离，可能提示 **各向异性、趋势或稳健估计** 的需求（本例不展开）。
"""
    )
)

cells.append(
    code(
        r"""errs = {}
x = np.linspace(0, float(max_lag), 200)
for name, m in fits.items():
    errs[name] = float(np.sqrt(np.mean((m.variogram(bin_center) - emp_gamma) ** 2)))

best = min(errs, key=errs.get)
print("各模型在 γ 上的 RMS:", {k: round(v, 5) for k, v in errs.items()})
print("按 RMS 选取的模型:", best)
best_m = fits[best]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(bin_center, emp_gamma, "o", color="0.2", label="经验半变异")
ax.plot(x, best_m.variogram(x), "-", color="C0", linewidth=2, label=f"拟合：{best}")
for name, m in fits.items():
    if name == best:
        continue
    ax.plot(x, m.variogram(x), "--", alpha=0.55, label=f"{name}")
ax.set_xlabel("滞后距离 h (m)")
ax.set_ylabel("γ(h)")
ax.set_title("理论半变异模型 vs 经验半变异")
ax.legend(ncol=2, fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "fitted_variogram_models.png", dpi=150)
plt.show()
"""
    )
)

cells.append(
    md(
        r"""## 6. 块金、基台与有效距离（结合本例输出）

下面数值由 **当前最优模型** 直接读出；**有效相关距离** 采用常见工程换算（与理论文档表一致处见 [§6](spatial_variability_theory.md#6-块金基台与变程各指什么)）。
"""
    )
)

cells.append(
    code(
        r"""nug = float(best_m.nugget)
ps = float(best_m.var)
sill = nug + ps
print(f"块金 (nugget): {nug:.4f}")
print(f"部分基台 (partial sill): {ps:.4f}")
print(f"总基台 (approx. sill): {sill:.4f}")
print(f"相关长度参数 len_scale: {float(best_m.len_scale):.1f} m")

if best == "Spherical":
    eff_range = float(best_m.len_scale)
elif best == "Exponential":
    eff_range = float(3 * best_m.len_scale)
elif best == "Gaussian":
    eff_range = float(np.sqrt(3) * best_m.len_scale)
else:
    eff_range = float("nan")
print(f"经验有效相关距离（常用换算，模型={best}）: ~{eff_range:.0f} m")
"""
    )
)

cells.append(
    md(
        r"""### 小结

- **块金**：短于采样尺度或测量误差带来的「不连续」部分。
- **部分基台 / 总基台**：空间相关所能解释的方差份额（与 $C(0)-C(h)$ 关系见理论 [§4](spatial_variability_theory.md#4-协方差函数与变异函数)）。
- **变程尺度**：超过该距离后点对相关性显著减弱；克里金权重会更多依赖远处样点时需审视模型是否合适（[§8](spatial_variability_theory.md#8-与克里金的关系一句话)）。

**延伸阅读**：各向异性、稳健半变异、交叉验证、泛克里金等见理论文档 [§9](spatial_variability_theory.md#9-本仓库-notebook-未展开的主题延伸阅读)。

---

**本 Notebook 产出图件（已写入 `outputs/`）**

| 文件 | 内容 |
|------|------|
| `semivariogram_concept.png` | 块金/基台/变程 **示意**（非拟合参数） |
| `meuse_logzn_points.png` | 样点 log(锌) 分布 |
| `empirical_variogram.png` | 经验半变异 |
| `fitted_variogram_models.png` | 模型与经验对比 |
"""
    )
)

nb = new_notebook(
    metadata={
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.9"},
    },
    cells=cells,
)

nbformat.write(nb, "cases/spatial-variability/spatial_variability_meuse.ipynb")
print("OK", len(cells), "cells")
