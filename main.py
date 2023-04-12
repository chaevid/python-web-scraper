from requests import get

results = {}

websites = ("google.com", "airbnb.com", "https://twitter.com",
            "facebook.com", "https://youtube.com")

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = (get(website))
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"


print(results)
