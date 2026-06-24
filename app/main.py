from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import pricing_collection, leads_collection

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

# --- SEO Landing Page Routes ---

@app.get("/whatsapp-business-api", response_class=HTMLResponse)
async def whatsapp_page(request: Request):
    return templates.TemplateResponse("whatsapp.html", {"request": request})

@app.get("/rcs-messaging-services", response_class=HTMLResponse)
async def rcs_page(request: Request):
    return templates.TemplateResponse("rcs.html", {"request": request})

@app.get("/bulk-sms-otp-gateway", response_class=HTMLResponse)
async def sms_page(request: Request):
    return templates.TemplateResponse("sms.html", {"request": request})

@app.get("/voice-broadcasting-obd", response_class=HTMLResponse)
async def voice_page(request: Request):
    return templates.TemplateResponse("voice.html", {"request": request})

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