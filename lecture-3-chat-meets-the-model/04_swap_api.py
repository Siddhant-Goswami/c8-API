# Homework: same 4 parts, different API. Run: python 04_swap_api.py

import requests

r = requests.get(                                            # ACTION
    "https://date.nager.at/api/v3/PublicHolidays/2026/US",   # ADDRESS
)                                                            # KEY: none
                                                             # PACKAGE: none
print("Status code:", r.status_code)
for holiday in r.json():
    print(holiday["date"], "-", holiday["localName"])
