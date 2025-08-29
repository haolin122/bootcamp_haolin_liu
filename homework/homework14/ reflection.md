# Deployment & Monitoring Reflection (≈240 words)

Our current simple linear regression (Stage 11) would face real-world risks if deployed: (1) data schema or distribution drift , (2) spikes in outliers, (3) delayed or noisy labels for evaluation, (4) segment C instability observed during evaluation, and (5) infrastructure hiccups (latency/errors) that degrade user experience.
**Data.**: Freshness (max age of last batch < 60 minutes for streaming or within daily SLA),
null rate on `x_feature` (< 10% and stable), schema hash (no breaking changes), and drift via
PSI on `x_feature` and `segment` (alert at PSI > 0.2). Owners: Data Engineering on-call;
**Model.** 14-day rolling MAE with a guardrail (e.g., > 15% above baseline or exceeding the Stage-11 bootstrap CI upper bound), residuals by segment (Segment C std or bias rising > 30% vs baseline), and prediction range sanity checks.

**System.** p95 latency (< 300 ms), error rate (< 1% 5xx), availability (≥ 99.5%), and queue depth. 
**Business.** One KPI tied to the decision (e.g., approval/uptake rate, cost per action). Alert if KPI drops > 5pp week-over-week or uplift vs. control turns negative. Owners: Product/Analytics
**Retraining.** Cadence monthly **or** trigger on PSI > 0.2 or 2-week MAE breach. Handoffs: dashboards maintained by Analytics; rollbacks approved by Platform + ML