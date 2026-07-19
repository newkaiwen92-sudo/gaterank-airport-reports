# GateRank 机场推荐与机场 VPN 月度报告库

[![访问统计](https://hits.sh/github.com/newkaiwen92-sudo/gaterank-airport-reports.svg?label=views&color=0e75b6)](https://hits.sh/github.com/newkaiwen92-sudo/gaterank-airport-reports/)

本仓库是 **GateRank（机场榜）** 的公开 Markdown 报告归档，用于沉淀每月机场 VPN 测评、机场排行榜、机场测速、价格、稳定性、客户端支持与跑路风险记录。内容面向 **2026机场推荐、机场推荐、稳定机场推荐、便宜机场推荐、Clash机场推荐、Shadowrocket机场推荐、USDT买机场、Netflix机场推荐、跑路机场监测** 等搜索场景。

> 本仓库负责长期归档和 GitHub 可索引入口；**实时评分、最新榜单、优惠活动、风险状态和完整动态数据请以 GateRank 主站为准。**

## GateRank 官方入口

- [GateRank 机场榜首页](https://gate-rank.com/?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_home)：机场 VPN 推荐、科学上网机场测评与可靠性榜单。
- [2026机场推荐 / 全量机场排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_rankings)：按 GateRank Score、价格、状态、客户端、线路和支付方式筛选机场。
- [机场月度报告中心](https://gate-rank.com/monthly-reports?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_monthly)：按月份查看行业报告、机场排行榜变化与风险观察。
- [机场优惠码与活动折扣](https://gate-rank.com/deals?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_deals)：查看机场优惠码、免费试用、新用户优惠与 USDT 支付优惠。
- [跑路风险监测](https://gate-rank.com/risk-monitor?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_risk)：跟踪官网异常、SSL 告警、历史异常与风险提示。
- [翻墙工具下载](https://gate-rank.com/download?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_tools)：Windows、macOS、Android、Linux 科学上网客户端与机场订阅工具。
- [GateRank for AI / 机器可读数据](https://gate-rank.com/for-ai?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_ai)：JSON、Markdown、llms.txt 与 AI 引用说明。
- [机场测评方法](https://gate-rank.com/methodology?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_methodology)：了解 GateRank Score、测速口径与风险扣分逻辑。
- [机场资讯中心](https://gate-rank.com/news?utm_source=github&utm_medium=readme&utm_campaign=reports_repo_news)：机场推荐、客户端教程、跑路预警、支付安全与行业观察。

## 这个报告库适合用来做什么？

- **查历史月报**：按月份回看某个机场的评分、价格、状态、测速与风险变化。
- **辅助选择机场**：结合 GateRank 主站实时榜单，判断稳定机场、便宜机场、Clash/Shadowrocket 机场、USDT 支付机场和流媒体解锁机场。
- **核对数据来源**：每份 Markdown 报告保留可追溯的月度快照，便于搜索引擎、AI 助手和用户引用。
- **建立品牌实体**：本仓库与 `gate-rank.com`、Google Sites 说明页、主站月报中心共同构成 GateRank 的公开资料矩阵。

## 热门机场推荐专题

- [机场推荐 / 2026机场推荐](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=seo_keywords)：查看 GateRank 最新机场排行榜、公开评分、价格、风险和月度机场测评归档。
- [稳定机场推荐](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=stable_airport)：优先参考 30 天可用率、连续健康天数、延迟、丢包和历史风险记录。
- [便宜机场推荐](https://gate-rank.com/deals?utm_source=github&utm_medium=readme&utm_campaign=cheap_airport)：对比最低月付、优惠码、免费试用、新用户折扣和一次性套餐。
- [Clash机场推荐](https://gate-rank.com/news/topic/clash-subscription?utm_source=github&utm_medium=readme&utm_campaign=clash_airport)：关注 Clash、Clash Verge、OpenClash、Mihomo 等客户端导入体验。
- [Shadowrocket机场推荐](https://gate-rank.com/rankings/all?client=shadowrocket&utm_source=github&utm_medium=readme&utm_campaign=shadowrocket_airport)：关注小火箭订阅、二维码导入和 iOS 使用体验。
- [USDT买机场](https://gate-rank.com/news/topic/usdt-airport-payment?utm_source=github&utm_medium=readme&utm_campaign=usdt_airport)：筛选支持 USDT-TRC20 等加密货币支付的机场服务。
- [跑路机场 / 风险机场](https://gate-rank.com/risk-monitor?utm_source=github&utm_medium=readme&utm_campaign=risk_airport)：跟踪官网异常、SSL 告警、投诉和历史异常记录。
- [Netflix机场推荐](https://gate-rank.com/rankings/all?streaming=netflix&utm_source=github&utm_medium=readme&utm_campaign=netflix_airport)：关注 Netflix、Disney+、HBO Max、YouTube Premium 等流媒体解锁能力。

## 数据与报告文件

- `reports/YYYY-MM/<slug>.md`：单机场月度报告正文。
- `data/reports-index.json`：报告索引的机器可读数据。
- `scripts/import_report.py`：把 `incoming/` 原始报告归档到标准目录。
- `scripts/update_readme.py`：根据 JSON 索引自动更新下方报告目录。

## 报告目录

<!-- REPORT_INDEX_START -->
### 最新报告月份：2026-06

[查看 GateRank 实时全量排行榜](https://gate-rank.com/rankings/all?utm_source=github&utm_medium=readme&utm_campaign=monthly_2026_06)

#### 最新月度报告列表

- [大象网络机场测试报告](reports/2026-06/elphantroute.md)，评分 90.44 ｜ [GateRank 动态报告](https://gate-rank.com/airports/elphantroute?utm_source=github&utm_medium=readme&utm_campaign=elphantroute)
- [Now加速机场测试报告](reports/2026-06/nowjiasu.md)，评分 87.82 ｜ [GateRank 动态报告](https://gate-rank.com/airports/nowjiasu?utm_source=github&utm_medium=readme&utm_campaign=nowjiasu)
- [仙路湾机场测试报告](reports/2026-06/xianluwan.md)，评分 84.17 ｜ [GateRank 动态报告](https://gate-rank.com/airports/xianluwan?utm_source=github&utm_medium=readme&utm_campaign=xianluwan)
- [瞬云机场测试报告](reports/2026-06/ccc-jichang.md)，评分 83.82 ｜ [GateRank 动态报告](https://gate-rank.com/airports/ccc-jichang?utm_source=github&utm_medium=readme&utm_campaign=ccc-jichang)
- [山水云机场测试报告](reports/2026-06/shanshuiyun.md)，评分 83.66 ｜ [GateRank 动态报告](https://gate-rank.com/airports/shanshuiyun?utm_source=github&utm_medium=readme&utm_campaign=shanshuiyun)
- [Nice加速机场测试报告](reports/2026-06/nicejiasu-2.md)，评分 83.59 ｜ [GateRank 动态报告](https://gate-rank.com/airports/nicejiasu-2?utm_source=github&utm_medium=readme&utm_campaign=nicejiasu-2)
- [锦云机场测试报告](reports/2026-06/w2-whengdl.md)，评分 81.84 ｜ [GateRank 动态报告](https://gate-rank.com/airports/w2-whengdl?utm_source=github&utm_medium=readme&utm_campaign=w2-whengdl)
- [极速云机场测试报告](reports/2026-06/sub-jsysubtoken.md)，评分 78.21 ｜ [GateRank 动态报告](https://gate-rank.com/airports/sub-jsysubtoken?utm_source=github&utm_medium=readme&utm_campaign=sub-jsysubtoken)
- [寰宇云机场测试报告](reports/2026-06/dashboard-huanyuyunvip.md)，评分 77.34 ｜ [GateRank 动态报告](https://gate-rank.com/airports/dashboard-huanyuyunvip?utm_source=github&utm_medium=readme&utm_campaign=dashboard-huanyuyunvip)
- [秒秒云机场测试报告](reports/2026-06/dl2-mmy8.md)，评分 75.57 ｜ [GateRank 动态报告](https://gate-rank.com/airports/dl2-mmy8?utm_source=github&utm_medium=readme&utm_campaign=dl2-mmy8)
- [可达加速器机场测试报告](reports/2026-06/1-mkd997.md)，评分 75.10 ｜ [GateRank 动态报告](https://gate-rank.com/airports/1-mkd997?utm_source=github&utm_medium=readme&utm_campaign=1-mkd997)
- [飞猫云机场测试报告](reports/2026-06/flycat-flycatvipaff.md)，评分 74.94 ｜ [GateRank 动态报告](https://gate-rank.com/airports/flycat-flycatvipaff?utm_source=github&utm_medium=readme&utm_campaign=flycat-flycatvipaff)
- [宇宙云机场测试报告](reports/2026-06/01-yuzoucloud.md)，评分 62.09 ｜ [GateRank 动态报告](https://gate-rank.com/airports/01-yuzoucloud?utm_source=github&utm_medium=readme&utm_campaign=01-yuzoucloud)
- [稳连云机场测试报告](reports/2026-06/wl1-yuildavvjh.md)，评分 49.98 ｜ [GateRank 动态报告](https://gate-rank.com/airports/wl1-yuildavvjh?utm_source=github&utm_medium=readme&utm_campaign=wl1-yuildavvjh)
- [光速云机场测试报告](reports/2026-06/qwerty-gsyaff.md) ｜ [GateRank 动态报告](https://gate-rank.com/airports/qwerty-gsyaff?utm_source=github&utm_medium=readme&utm_campaign=qwerty-gsyaff)

### 历史月度归档

#### 2026-06

- [Nice加速机场](reports/2026-06/nicejiasu-2.md)（评分 83.59，价格 ¥10）
- [Now加速](reports/2026-06/nowjiasu.md)（评分 87.82，价格 ¥10）
- [仙路湾](reports/2026-06/xianluwan.md)（评分 84.17，价格 ¥9.90）
- [光速云](reports/2026-06/qwerty-gsyaff.md)（价格 ¥17）
- [可达加速器](reports/2026-06/1-mkd997.md)（评分 75.10，价格 ¥10）
- [大象网络](reports/2026-06/elphantroute.md)（评分 90.44，价格 ¥12）
- [宇宙云](reports/2026-06/01-yuzoucloud.md)（评分 62.09，价格 ¥12.50）
- [寰宇云机场](reports/2026-06/dashboard-huanyuyunvip.md)（评分 77.34，价格 ¥18）
- [山水云](reports/2026-06/shanshuiyun.md)（评分 83.66，价格 ¥14.99）
- [极速云机场](reports/2026-06/sub-jsysubtoken.md)（评分 78.21，价格 ¥15.99）
- [瞬云](reports/2026-06/ccc-jichang.md)（评分 83.82，价格 ¥20）
- [秒秒云](reports/2026-06/dl2-mmy8.md)（评分 75.57，价格 ¥13.99）
- [稳连云](reports/2026-06/wl1-yuildavvjh.md)（评分 49.98，价格 ¥12）
- [锦云](reports/2026-06/w2-whengdl.md)（评分 81.84，价格 ¥6）
- [飞猫云](reports/2026-06/flycat-flycatvipaff.md)（评分 74.94，价格 ¥15）

#### 2026-05

- [Now加速](reports/2026-05/nowjiasu.md)（评分 82.85，价格 ¥10）
- [仙路湾](reports/2026-05/xlw.md)（评分 80.24，价格 ¥9.90）
- [光速云](reports/2026-05/qwerty-gsyaff.md)（评分 79.29，价格 ¥17）
- [大象网络](reports/2026-05/elphantroute.md)（评分 83.31，价格 ¥12）
- [山水云](reports/2026-05/shanshuiyun.md)（评分 80.54，价格 ¥14.99）
- [极速云机场](reports/2026-05/jsysubtoken.md)（评分 70.48，价格 ¥15.99）
- [瞬云](reports/2026-05/ccc-jichang.md)（评分 82.82，价格 ¥20）
- [飞猫云](reports/2026-05/flycat-flycatvipaff.md)（评分 70.60，价格 ¥15）

#### 2026-04

- [大象网络](reports/2026-04/elphantroute.md)（评分 81.01，价格 ¥12）

### 按机场索引

- **Nice加速机场**：[2026-06](reports/2026-06/nicejiasu-2.md)
- **Now加速**：[2026-06](reports/2026-06/nowjiasu.md)、[2026-05](reports/2026-05/nowjiasu.md)
- **仙路湾**：[2026-06](reports/2026-06/xianluwan.md)、[2026-05](reports/2026-05/xlw.md)
- **光速云**：[2026-06](reports/2026-06/qwerty-gsyaff.md)、[2026-05](reports/2026-05/qwerty-gsyaff.md)
- **可达加速器**：[2026-06](reports/2026-06/1-mkd997.md)
- **大象网络**：[2026-06](reports/2026-06/elphantroute.md)、[2026-05](reports/2026-05/elphantroute.md)、[2026-04](reports/2026-04/elphantroute.md)
- **宇宙云**：[2026-06](reports/2026-06/01-yuzoucloud.md)
- **寰宇云机场**：[2026-06](reports/2026-06/dashboard-huanyuyunvip.md)
- **山水云**：[2026-06](reports/2026-06/shanshuiyun.md)、[2026-05](reports/2026-05/shanshuiyun.md)
- **极速云机场**：[2026-06](reports/2026-06/sub-jsysubtoken.md)、[2026-05](reports/2026-05/jsysubtoken.md)
- **瞬云**：[2026-06](reports/2026-06/ccc-jichang.md)、[2026-05](reports/2026-05/ccc-jichang.md)
- **秒秒云**：[2026-06](reports/2026-06/dl2-mmy8.md)
- **稳连云**：[2026-06](reports/2026-06/wl1-yuildavvjh.md)
- **锦云**：[2026-06](reports/2026-06/w2-whengdl.md)
- **飞猫云**：[2026-06](reports/2026-06/flycat-flycatvipaff.md)、[2026-05](reports/2026-05/flycat-flycatvipaff.md)

_README 索引更新时间：2026-07-20 01:58:39 +0800_
<!-- REPORT_INDEX_END -->

## 免责声明

本仓库内容为 GateRank 每月公开测试报告归档，仅供选择机场 VPN 服务时参考。机场状态、价格、节点、官网可用性和风险标签可能变化，不构成购买或长期年付建议。实时数据请以 [GateRank 主站](https://gate-rank.com/?utm_source=github&utm_medium=readme&utm_campaign=disclaimer) 为准。
