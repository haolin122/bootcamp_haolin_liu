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
| **9. Feature Engineering** | *(What features did you construct? Technical indicators, lags, ratios?)* | *(Which features were difficult to design or justify?)* | *(How did you validate usefulness of features?)* | *(What domain-driven features could you add?)* |
| **10. Modeling (Regression / Time Series / Classification)** | *(Which models did you try and why?)* | *(What challenges arose — overfitting, convergence, runtime?)* | *(How did you choose/tune the final model?)* | *(What alternative models would you try in future?)* |
| **11. Evaluation & Risk Communication** | *(Which metrics did you evaluate?)* | *(Which assumptions/risks were most concerning?)* | *(How did you communicate uncertainty, error, tradeoffs?)* | *(What evaluation methods would improve robustness?)* |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | *(How did you present results? Slides, reports, dashboards?)* | *(What was difficult to explain to non-technical stakeholders?)* | *(What delivery choices helped communication land?)* | *(What would you change in delivery/communication?)* |
| **13. Productization** | *(How did you prepare the model/data pipeline for production use?)* | *(What issues arose around scalability, maintainability?)* | *(What design decisions ensured reliability?)* | *(What productization steps would you add?)* |
| **14. Deployment & Monitoring** | *(How did you deploy your solution?)* | *(What monitoring or alerting challenges did you face?)* | *(How did you track model drift or system performance?)* | *(What would you upgrade in deployment/monitoring?)* |
| **15. Orchestration & System Design** | *(How did you integrate tasks into workflows/pipelines?)* | *(What complexity or dependency issues appeared?)* | *(How did you solve orchestration problems?)* | *(What would you change in system design?)* |
| **16. Lifecycle Review & Reflection** | *(What are your biggest takeaways from the full lifecycle?)* | *(Where did you struggle the most?)* | *(What patterns or strategies helped across multiple stages?)* | *(What would you do differently in your next project?)* |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
- Which stage was the most **rewarding**?  
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
- If you repeated this project, what would you **do differently across the lifecycle**?  
- Which skills do you most want to **strengthen** before your next financial engineering project?  

---