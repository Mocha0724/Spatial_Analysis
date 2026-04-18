# 数据说明

## Meuse 土壤样点（`processed/meuse.csv`）

- **内容**：荷兰 Meuse 河漫滩土壤重金属与协变量；`x`, `y` 为 **RD 新坐标**（米，EPSG:28992）；`zinc` 等为 ppm。与 R 包 `sp::meuse` / `gstat` 教程常用数据集一致。
- **获取**：运行仓库根目录下命令（需联网）：

  ```bash
  python scripts/download_meuse.py
  ```

  默认从公开镜像拉取 CSV；`scripts/download_meuse.py` 会对文件做 **SHA-256** 校验（见脚本内 `EXPECTED_SHA256`）。若镜像文件有更新导致校验失败，可核对来源后更新哈希，或使用 `--url` 指定新的数据地址。
- **许可与引用**：数据广泛用于地统计教学；请在公开使用时**同时**说明数据源自 Meuse 教学数据集并引用相关文献（见根目录 `README.md`「参考文献」）。本仓库不主张对原始测量数据本身拥有版权。
