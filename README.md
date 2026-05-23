# GateRank 机场测评报告库：机场推荐、机场排行榜、机场测速与风险监测

本仓库用于归档 GateRank 每月机场测试报告，覆盖机场推荐、机场排行榜、机场测评、机场测速、稳定机场、便宜机场、Clash 机场、Shadowrocket 机场、USDT 支付机场与跑路风险监测等公开信息。

> 本仓库是 GitHub Markdown 归档入口；实时评分、最新榜单、风险状态和完整动态数据请以 GateRank 主站为准。

## GateRank 主站入口

- [机场排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=reports_repo)
- [跑路风险监测](https://gate-rank.com/risk-monitor?utm_source=github&utm_medium=readme&utm_campaign=reports_repo)
- [机场测评方法](https://gate-rank.com/methodology?utm_source=github&utm_medium=readme&utm_campaign=reports_repo)
- [机场资讯中心](https://gate-rank.com/news?utm_source=github&utm_medium=readme&utm_campaign=reports_repo)

## 最新月度报告

最新归档报告见下方报告目录。将 Markdown 报告放入 `incoming/` 后运行：

```bash
python3 scripts/import_report.py --incoming incoming
python3 scripts/update_readme.py
```

脚本会自动生成：

- `reports/YYYY-MM/<slug>.md`
- `data/reports-index.json`
- README 月度报告索引

## 报告目录

<!-- REPORT_INDEX_START -->
### 最新报告月份：2026-04

[查看 GateRank 实时全量排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=monthly_2026_04)

#### 最新月度报告列表

- [大象网络机场测试报告](reports/2026-04/elphantroute.md)，评分 81.01，状态：稳定 ｜ [GateRank 动态报告](https://gate-rank.com/airports/elphantroute?utm_source=github&utm_medium=readme&utm_campaign=elphantroute)

### 历史月度归档

#### 2026-04

- [大象网络](reports/2026-04/elphantroute.md)（评分 81.01，价格 ¥12）

### 按机场索引

- **大象网络**：[2026-04](reports/2026-04/elphantroute.md)

_README 索引更新时间：2026-05-23 12:34:35 +0800_
<!-- REPORT_INDEX_END -->

## 自动化说明

推荐流程：

1. 将 GateRank 原始机场测试报告 Markdown 放入 `incoming/`。
2. 运行 `python3 scripts/import_report.py --incoming incoming` 标准化归档。
3. 运行 `python3 scripts/update_readme.py` 更新 README 索引。
4. 提交并推送到 GitHub。

也可以使用 GitHub Actions 的 `Update README report index` 工作流自动执行。

## 免责声明

本仓库内容为 GateRank 每月公开测试报告归档，仅供选择机场 VPN 服务时参考。机场状态、价格、节点、官网可用性和风险标签可能变化，不构成购买或长期年付建议。实时数据请以 [GateRank 主站](https://gate-rank.com/?utm_source=github&utm_medium=readme&utm_campaign=disclaimer) 为准。
