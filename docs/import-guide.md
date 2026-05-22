# GateRank 报告导入说明

## 方式一：本地导入

把原始 Markdown 报告放入 `incoming/`，然后运行：

```bash
python3 scripts/import_report.py --incoming incoming
python3 scripts/update_readme.py
git add README.md data/reports-index.json reports/ incoming/
git commit -m "add monthly airport reports"
git push
```

## 方式二：GitHub Actions 自动导入

1. 把原始 Markdown 报告提交到 `incoming/`。
2. GitHub Actions 会自动运行：
   - `scripts/import_report.py --incoming incoming`
   - `scripts/update_readme.py`
3. 工作流会自动提交更新后的：
   - `reports/YYYY-MM/<slug>.md`
   - `data/reports-index.json`
   - `README.md`

## 建议报告字段

原始报告可以自由书写，但包含以下字段时解析效果更好：

```md
# 大象网络机场测试报告

- 机场名称：大象网络
- slug：elphantroute
- 报告月份：2026-05
- GateRank 公开评分：83.11
- 当前状态：正常
- 月付价格：¥12
- 30 天可用率：98.31%
- 中位延迟：42.66 ms
- 下载速率：36.06 Mbps
- 风险提示：暂无明显风险
```

如果未提供 `slug`，脚本会尽量从标题或机场名称生成。
