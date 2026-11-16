from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_summary(): 
 r=c.get("/workforce/summary").json(); assert r["active_headcount"]==7 and r["dataset"]=="synthetic"
def test_department_and_absence():
 assert sum(x["headcount"] for x in c.get("/workforce/departments").json())==7
 assert c.get("/workforce/absence").json()["recorded_absence_days"]==34
def test_hiring_trend():
 x=c.get("/workforce/hiring-trend").json(); assert [r["month"] for r in x]==sorted(r["month"] for r in x)
