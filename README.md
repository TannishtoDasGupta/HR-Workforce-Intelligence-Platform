# HR Workforce Intelligence Platform

A workforce analytics API built around synthetic, non-identifying HR records. It exposes headcount, department distribution, absence, and hiring trend metrics without exposing employee-level records.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open /docs. API: /workforce/summary, /workforce/departments, /workforce/absence, /workforce/hiring-trend.

## Responsible analytics
All bundled records are fictional. Never upload identifiable employee data to a public demo. Real deployments require role-based access, purpose limitation, retention controls, minimum aggregation thresholds, bias review, and HR/payroll validation. Metrics must not be used alone for employment decisions.
