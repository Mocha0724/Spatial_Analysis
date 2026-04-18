# 空间变异分析（Meuse）

主 Notebook：[`spatial_variability_meuse.ipynb`](spatial_variability_meuse.ipynb)

流程概览：数据加载 → `log(zinc)` 作为区域化变量 → 经验半变异（Matheron）→ 球状 / 指数 / 高斯模型拟合 → 块金、基台与有效相关距离解读。

运行前请在仓库根目录创建虚拟环境并安装依赖，然后启动 Notebook（见根目录 `README.md`）。
