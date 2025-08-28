import json
from api_request import send_api_request, get_family

PACKAGE_FAMILY_CODE = "6bcc96f4-f196-4e8f-969f-e45a121d21bd"

def get_package_masa_aktif(api_key: str, tokens: dict):
    packages = []
    
    data = get_family(api_key, tokens, PACKAGE_FAMILY_CODE)
    package_variants = data["package_variants"]
    start_number = 1
    for variant in package_variants:
        if True:
            for option in variant["package_options"]:
                if True:
                    friendly_name = option["name"]
                    
                    if friendly_name.lower() == "45GB":
                        friendly_name = "Kuota 45GB Setahun"
                        
                    packages.append({
                        "number": start_number,
                        "name": friendly_name,
                        "price": option["price"],
                        "code": option["package_option_code"]
                    })
                    
                    start_number += 1
    return packages
