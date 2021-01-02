#!/usr/bin/env python3
import requests

req = requests.get("https://hnitborg-pkm.ddns.net")
print(req.content)