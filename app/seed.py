import asyncio
from app.database import pricing_collection

def make_pkg(name, volume_int, base_price, features):
    # Calculate the 5 paise markup per message
    markup = int(volume_int * 0.05) 
    final_price = base_price + markup
    
    # Format volume nicely (e.g., 100,000 to 1 LAC)
    if volume_int >= 100000:
        if volume_int % 100000 == 0:
            vol_str = f"{volume_int // 100000} LAC"
        else:
            vol_str = f"{volume_int / 100000} LAC"
    else:
        vol_str = f"{volume_int:,}"
        
    return {
        "name": name,
        "volume": f"{vol_str} MSG",
        "price": final_price,
        "features": features
    }

async def seed_data():
    await pricing_collection.delete_many({})
    
    wa_features = [
        "Delivery Window: 9 AM to 6 PM", 
        "Media: Text, Image, Video", 
        "Refund: For Non-WhatsApp", 
        "Sending: Virtual Numbers"
    ]
    
    tx_features = [
        "Availability: 24x7x365", 
        "DND Support: Delivers to DND", 
        "Integration: HTTP API", 
        "Refund: Failed Messages"
    ]
    
    tiers = [
        {
            "category": "Bulk WhatsApp SMS",
            "accent_color": "emerald",
            "packages": [
                make_pkg("Starter", 10000, 2000, wa_features),
                make_pkg("Growth", 25000, 4500, wa_features),
                make_pkg("Professional", 50000, 7000, wa_features),
                make_pkg("Business", 100000, 12000, wa_features),
                make_pkg("Corporate", 200000, 22000, wa_features),
                make_pkg("Enterprise", 500000, 50000, wa_features),
                make_pkg("Scale", 1000000, 90000, wa_features),
            ]
        },
        {
            "category": "Transactional Bulk SMS (High Priority OTP)",
            "accent_color": "blue",
            "packages": [
                make_pkg("OTP Starter", 10000, 2000, tx_features),
                make_pkg("OTP Growth", 25000, 4500, tx_features),
                make_pkg("OTP Pro", 50000, 7000, tx_features),
                make_pkg("OTP Business", 100000, 13000, tx_features),
                make_pkg("OTP Corp", 200000, 25000, tx_features),
                make_pkg("OTP Enterprise", 500000, 60000, tx_features),
                make_pkg("OTP Scale", 1000000, 110000, tx_features),
            ]
        }
    ]
    
    await pricing_collection.insert_many(tiers)
    print("Database seeded with competitor matching pricing + 5 paise markup!")

if __name__ == "__main__":
    asyncio.run(seed_data())