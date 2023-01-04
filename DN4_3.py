import requests


spletna_stran = requests.get("https://www.rtvslo.si/iskalnik?q=iskalni%20niz")

print(spletna_stran.status_code)

print(spletna_stran.text)
