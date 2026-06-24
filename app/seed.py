import asyncio
from app.database import pricing_collection

async def seed_data():
    # Clear existing to prevent duplicates
    await pricing_collection.delete_many({})
    
    tiers = [
        {
            "category": "BULK WHATSAPP / SMS",
            "accent_color": "emerald",
            "packages": [
                {"name": "Starter", "volume": "5,000 Messages", "price": 2500, "features": ["99% Delivery Rate", "AI Copy Assistant", "Video & PDF Preview support", "API Integration"]},
                {"name": "Growth", "volume": "10,000 Messages", "price": 5000, "features": ["High Priority Route", "Dedicated Channel", "Video & PDF Preview support", "24/7 Priority Support"]}
            ]
        },
        {
            "category": "TRANSACTIONAL BULK SMS (HIGH PRIORITY OTP)",
            "accent_color": "blue",
            "packages": [
                {"name": "OTP Basic", "volume": "5,000 OTPs", "price": 2500, "features": ["Instant 2-Sec Delivery", "DND Scrubbed", "Failover Routing", "HTTP API Client"]},
                {"name": "OTP Pro", "volume": "10,000 OTPs", "price": 4500, "features": ["Dynamic Route Engine", "Realtime Analytics", "Unlimited Sender IDs", "Dedicated Support"]}
            ]
        },
        {
            "category": "BULK VOICE CALLS (OBD - 30 SEC PULSE)",
            "accent_color": "purple",
            "packages": [
                {"name": "Voice Entry", "volume": "10,000 Calls", "price": 3500, "features": ["Concurrent Calls", "Custom Audio Upload", "IVR Interactive Input", "Detailed Retry Analytics"]}
            ]
        }
    ]
    
    await pricing_collection.insert_many(tiers)
    print("Database successfully seeded with categories from reference image!")

if __name__ == "__main__":
    asyncio.run(seed_data())