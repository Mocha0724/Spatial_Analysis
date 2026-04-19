# 数据目录说明

本目录存放各案例所使用的公开数据集。

## 目录结构

```
data/
└── processed/
    └── meuse.csv     # Meuse 土壤样点数据（空间变异案例）
```

---

## meuse.csv

**用途**：[空间变异案例](../cases/spatial-variability/)

**来源**：源自 R `sp::meuse` 数据集（荷兰莱茵河支流 Meuse 河漫滩土壤样点调查）。  
本仓库使用的 CSV 为公开 Gist 镜像版本，列名与常见 R 导出格式一致。

**主要字段**：

| 字段 | 说明 |
|------|------|
| `x`, `y` | 荷兰 RD 坐标系（EPSG:28992），单位：米 |
| `cadmium` | 镉浓度（ppm） |
| `copper` | 铜浓度（ppm） |
| `lead` | 铅浓度（ppm） |
| `zinc` | 锌浓度（ppm，案例主分析变量） |
| `elev` | 高程（m） |
| `dist` | 到 Meuse 河的相对距离 |
| `om` | 有机质含量（%） |
| `ffreq` | 洪水频率等级 |
| `soil` | 土壤类型 |
| `lime` | 石灰含量 |
| `landuse` | 土地利用类型 |

**SHA-256（默认镜像）**：  
`aca2070a2dfaa9590cadbf9dde3ecec230882b7682dc3f910091a21c0e51f0c2`

**重新下载与校验**：

```bash
python scripts/download_meuse.py
```

**引用**：  
Rikken, M. G. J., & Van Rijn, R. P. G. (1993). Soil pollution with heavy metals — an inquiry into spatial variation, cost of mapping and the risk evaluation of copper, cadmium, lead and zinc in the floodplains of the Meuse west of Stein, the Netherlands. *Doctoraalveldwerkverslag*, Dept. of Physical Geography, Utrecht University.

---

## 可达性案例数据

[空间可达性案例](../cases/spatial-accessibility/) 使用**程序生成的合成数据**（内嵌于 Notebook），无需单独下载。如需使用真实数据，可替换为：

- 人口数据：区/街道级 `shapefile` 或 `GeoJSON`，提取人口字段与质心坐标
- 设施数据：从 OpenStreetMap 导出（`osmnx` / Overpass API），或使用各地卫健委/民政数据

替换方法：在 Notebook 第 2 节将 `demand` 和 `supply` 的 `pd.DataFrame` 构建语句替换为读文件代码，其余分析逻辑无需改动。
