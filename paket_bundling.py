import json
from api_request import send_api_request, get_family

PACKAGE_FAMILY_CODE = "U0NfX5WmsK6qiDkee_-aCL5oHT_J8VpRXtruMdAPKbyeKlM7bccIVJqHJanSnbp7tfQ-wvTjfp5Py8ayz1HSMw0"

def get_package_bundling(api_key: str, tokens: dict):
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
                        friendly_name = "45GB Setahun"
                        
                    packages.append({
                        "number": start_number,
                        "name": friendly_name,
                        "price": option["price"],
                        "code": option["package_option_code"]
                    })
                    
                    start_number += 1
    return packages
