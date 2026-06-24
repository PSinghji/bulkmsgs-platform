from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import pricing_collection, leads_collection

app = FastAPI(title="BulkMsgs AI Platform")

# Mount template engine
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    # Dynamically fetch structured pricing directly from MongoDB
    cursor = pricing_collection.find({}, {"_id": 0})
    pricing_data = await cursor.to_list(length=100)
    
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "pricing_groups": pricing_data}
    )

@app.post("/submit-lead")
async def handle_lead(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    volume: str = Form(...)
):
    # Store Google Ads leads securely in DB
    lead_doc = {"name": name, "email": email, "phone": phone, "volume": volume}
    await leads_collection.insert_one(lead_doc)
    
    # Redirect to a thank you anchor to trigger conversion pixel tracker easily
    return RedirectResponse(url="/#thankyou", status_code=status.HTTP_303_SEE_OTHER)