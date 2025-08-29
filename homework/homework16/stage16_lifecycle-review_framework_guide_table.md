# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Predict `y_target` from `x_feature` to provide simple, explainable estimates. | Missing data; need for interpretability over raw accuracy. | Chose linear regression baseline ; kept scope narrow. | Add business context (tolerance bands) and costs-of-error. |
| **2. Tooling Setup** | Python, NumPy/pandas/matplotlib, seaborn; Flask for API. | venv vs base deps mismatch (NumPy not found). | Standardized `requirements.txt`; install inside venv. | Add Makefile, pre-commit, and pinned versions. |
| **3. Python Fundamentals** | Vectorized pandas ops; small `SimpleLinReg` class; CLI wrapper for training. | Error handling/logging conventions. | Added minimal logging and deterministic seed. | Add typing, unit tests, and docstrings. |
| **4. Data Acquisition / Ingestion** | CSV (`data_stage11_eval_risk.csv`) or synthetic fallback. | Possible file missing / schema drift. | Ingest step with schema check; synthetic generation when absent. | Data contracts + source freshness checks. |
| **5. Data Storage** | CSV for source; Parquet for intermediates (`ingested`,`features`). | Consistent schema across steps. | Use Parquet for idempotent, reproducible checkpoints. | Lightweight data catalog and versioned artifacts. |
| **6. Data Preprocessing** | Mean/median imputation; basic normalization as needed. | Higher null rates degrade stability. | Default = mean impute; record %missing. | Robust scalers; imputation strategy by segment. |
| **7. Outlier Analysis** | 3σ scenario vs baseline comparison. | Distinguishing noise from rare events. | Kept both scenarios; reported sensitivity. | Try Huber loss / winsorization with thresholds. |
| **8. Exploratory Data Analysis (EDA)** | Scatter, line, residuals; subgroup by `segment`. | Segment C behaved differently. | Side-by-side plots; residual diagnostics. | Correlation heatmaps; partial dependence style views. |
| **9. Feature Engineering** | Minimal . | Risk of overfitting with polynomial terms. | Deferred complex features to keep clarity. | Add lags/ratios and regularization if scope expands. |
| **10. Modeling (Regression / Time Series / Classification)** | Simple linear regressio. | Sensitivity to missing/outliers. | Seeded fit; compared scenarios. | Try ridge; quantile regression for intervals. |
| **11. Evaluation & Risk Communication** | *(Which metrics did you evaluate?)* | *(Which assumptions/risks were most concerning?)* | *(How did you communicate uncertainty, error, tradeoffs?)* | *(What evaluation methods would improve robustness?)* |
| **12. Results Reporting, Delivery & Stakeholder Communication** | 3 key charts + executive summary; clear captions. | Translating tech terms to actions. | Plain-language bullets; consistent axes/colors. | Add a 1-page “What this means for you” appendix. |
| **13. Productization** | Saved `model.pkl`; Flask API; `requirements.txt`. | Environment parity, deterministic outputs. | Fixed seed, checksum for inputs, simple error handling. | Containerize; add basic auth & rate limits. |
| **14. Deployment & Monitoring** | Defined 4-layer monitors: Data/Model/System/Business with thresholds. | Alert routing & drift triggers. | PSI>0.2 or 2-week MAE breach triggers retrain; owners named. | Dashboard with drill-downs; incident templates. |
| **15. Orchestration & System Design** | DAG: ingest → clean → train_or_score → report; logs + checkpoints. | Idempotency/skip logic. | Feature-hash checkpoint; `--force` overrides. | Consider Airflow/Prefect; parallelize charts. |
| **16. Lifecycle Review & Reflection** | Documented end-to-end; repo cleaned and reproducible. | Balancing simplicity vs robustness. | Prefer small, testable steps; log + seed + checkpoints. | Expand features, add tests/CI, tighten monitoring. |


---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
- Which stage was the most **rewarding**?  
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
- If you repeated this project, what would you **do differently across the lifecycle**?  
- Which skills do you most want to **strengthen** before your next financial engineering project?  

---