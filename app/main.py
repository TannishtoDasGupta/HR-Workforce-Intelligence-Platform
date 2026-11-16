from fastapi import FastAPI
app=FastAPI(title="HR Workforce Intelligence Platform",version="1.0.0")
# Synthetic, non-identifying demo records only.
PEOPLE=[
{"dept":"Engineering","active":True,"salary":92000,"absence":4,"month":"2025-01"},
{"dept":"Engineering","active":True,"salary":88000,"absence":7,"month":"2025-02"},
{"dept":"People","active":True,"salary":65000,"absence":3,"month":"2025-02"},
{"dept":"Finance","active":True,"salary":71000,"absence":5,"month":"2025-03"},
{"dept":"Engineering","active":False,"salary":80000,"absence":2,"month":"2024-11"},
{"dept":"Sales","active":True,"salary":68000,"absence":8,"month":"2025-03"},
{"dept":"Sales","active":True,"salary":74000,"absence":6,"month":"2025-04"},
{"dept":"People","active":True,"salary":62000,"absence":1,"month":"2025-04"}]
@app.get("/health")
def health(): return {"status":"ok","dataset":"synthetic"}
@app.get("/workforce/summary")
def summary():
 a=[p for p in PEOPLE if p["active"]]; s=sorted(p["salary"] for p in a)
 return {"active_headcount":len(a),"total_records":len(PEOPLE),"median_salary":s[len(s)//2],"currency":"USD","dataset":"synthetic"}
@app.get("/workforce/departments")
def departments():
 d={}
 for p in PEOPLE:
  if p["active"]: d[p["dept"]]=d.get(p["dept"],0)+1
 return [{"department":k,"headcount":v} for k,v in sorted(d.items())]
@app.get("/workforce/absence")
def absence():
 a=[p for p in PEOPLE if p["active"]]; n=sum(p["absence"] for p in a)
 return {"active_employees":len(a),"recorded_absence_days":n,"days_per_employee":round(n/len(a),2)}
@app.get("/workforce/hiring-trend")
def hiring():
 d={}
 for p in PEOPLE: d[p["month"]]=d.get(p["month"],0)+1
 return [{"month":k,"hires":v} for k,v in sorted(d.items())]
