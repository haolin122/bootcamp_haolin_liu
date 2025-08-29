# Stage 15 Orchestration Plan
## 1. Project Task Decomposition
- ingest → produce `prices_raw.json`
- clean → produce `prices_clean.json`
- train_or_score → produce `model.json`
- report → produce `report.txt`
## 2. Dependencies (DAG)
Tasks run sequentially. In the future, `train_or_score` and `report` could be parallelized.
## 3. Logging & Checkpoints
- ingest: log start/end, rows, source URI; checkpoint `prices_raw.json`
- clean: log start/end, rows in/out; checkpoint `prices_clean.json`
- train_or_score: log params, metrics; checkpoint `model.json`
## 5. Reliability Notes
- Retry failed tasks once, log errors.
- Save run metadata (timestamps, counts).