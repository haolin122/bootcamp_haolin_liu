# Project Title
**Impact Analysis of NYC Congestion Pricing on NYU Commuter Students**

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
New York City's recently implemented Congestion Pricing policy imposes a significant daily fee on vehicles entering Manhattan's Central Business District. This policy creates a direct and substantial financial burden for NYU students who commute by car from outer boroughs or New Jersey, potentially impacting their financial stability and overall well-being.

The university currently lacks specific data on how many students are affected, the scale of the financial impact, and how commuting behaviors are changing in response. Without this data, it is difficult to design effective support programs or advocate on behalf of our students. This project aims to quantify the policy's impact to provide a clear, evidence-based foundation for university action.

## Stakeholder & User
The primary stakeholder and decision-maker is the **Director of the NYU Office of Student Affairs**. They are responsible for student welfare and will use the project's findings to propose new support initiatives.

The end users of the output (the final report) will be the **staff within the Office of Student Affairs and the university budget committee**. They will use the report to understand the problem's scope and evaluate the feasibility of solutions like a commuter subsidy.

## Useful Answer & Decision
- **Answer Type**: **Descriptive Analysis**. The goal is to describe the financial and logistical impact of the policy on students.
- **Metric**: Key metrics include the average increase in monthly commuting costs and the percentage shift from driving to public transit.
- **Artifact to Deliver**: A data report (Jupyter Notebook or PDF) with key visualizations like cost distribution charts.
- **Decision to Support**: This analysis will directly inform the decision on **whether NYU should establish a targeted commuter subsidy program** and how to structure it.

## Assumptions & Constraints
- **Assumptions**: We assume that student discussions on public forums (e.g., Reddit) are broadly representative of the commuter population's concerns.
- **Constraints**: We do not have access to official student address data due to privacy regulations. The analysis must rely on public data and voluntary, anonymous surveys.

## Known Unknowns / Risks
- **Uncertainty**: The actual number of students who commute by car is unknown and may be smaller than anticipated.
- **Monitoring**: Survey data will be monitored for self-selection bias, where only the most negatively affected students might respond.

## Lifecycle Mapping
Goal → Stage → Deliverable
- **Goal A**: Mitigate the financial burden of congestion pricing → Problem Framing & Scoping (Stage 01) → **Deliverable X**: A scoped project plan and a structured GitHub repository.
- **Goal B**: Provide data for future support programs → Data Collection & Cleaning (Stage 02) → A cleaned dataset combining survey and public transit information.

## Repo Plan
- **/data/**: For raw and processed datasets.
- **/src/**: For reusable Python scripts (e.g., data cleaning).
- **/notebooks/**: For exploratory analysis (EDA) and the final report.
- **/docs/**: For project documentation, like the stakeholder memo.
- **Cadence**: Updates will be committed to the repo upon completion of major milestones (e.g., data cleaning, initial EDA, final report).