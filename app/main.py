from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import pricing_collection, leads_collection

app = FastAPI(title="BulkMsgs AI Platform")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    pricing = await pricing_collection.find({}, {"_id": 0}).to_list(100)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "pricing_groups": pricing,
        "page_title": "Enterprise WhatsApp, RCS, SMS & Voice API Platform",
        "page_description": "Scale your business with AI-powered communication. High-throughput delivery for Meta WhatsApp Business API, interactive RCS, Bulk SMS, and Voice Calls."
    })

@app.get("/whatsapp-business-api", response_class=HTMLResponse)
async def whatsapp_page(request: Request):
    pricing = await pricing_collection.find({}, {"_id": 0}).to_list(100)
    return templates.TemplateResponse("whatsapp.html", {
        "request": request, 
        "pricing_groups": pricing,
        "page_title": "Enterprise WhatsApp Business API & Bulk Sender",
        "page_description": "Scale your customer engagement with the official Meta WhatsApp API. Send interactive campaigns with rich media, buttons, and automated flows."
    })

@app.get("/rcs-messaging-services", response_class=HTMLResponse)
async def rcs_page(request: Request):
    pricing = await pricing_collection.find({}, {"_id": 0}).to_list(100)
    return templates.TemplateResponse("rcs.html", {
        "request": request, 
        "pricing_groups": pricing,
        "page_title": "RCS Business Messaging Platform | The Future of SMS",
        "page_description": "Upgrade your SMS campaigns to RCS. Deliver app-like interactive experiences natively in the Android messages app with verified sender branding."
    })

@app.get("/bulk-sms-otp-gateway", response_class=HTMLResponse)
async def sms_page(request: Request):
    pricing = await pricing_collection.find({}, {"_id": 0}).to_list(100)
    return templates.TemplateResponse("sms.html", {
        "request": request, 
        "pricing_groups": pricing,
        "page_title": "High-Speed Bulk SMS & OTP API Gateway",
        "page_description": "99.9% uptime for mission-critical SMS. Fast OTP delivery and heavily scrubbed promotional routes compliant with DLT and TRAI regulations."
    })

@app.get("/voice-broadcasting-obd", response_class=HTMLResponse)
async def voice_page(request: Request):
    pricing = await pricing_collection.find({}, {"_id": 0}).to_list(100)
    return templates.TemplateResponse("voice.html", {
        "request": request, 
        "pricing_groups": pricing,
        "page_title": "Programmatic Voice Broadcasting & IVR Solutions",
        "page_description": "Launch massive outbound dialing (OBD) campaigns in minutes. Perfect for urgent alerts, political campaigns, and interactive lead generation."
    })

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