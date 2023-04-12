from requests import get

results = {}

websites = ("google.com", "airbnb.com", "https://twitter.com",
            "facebook.com", "https://youtube.com")

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response_code = (get(website).status_code)

    if response_code >= 200 & response_code < 300:
        results[website] = "Success"
    elif response_code >= 300 & response_code < 400:
        results[website] = "Redirect"
    elif response_code >= 400 & response_code < 500:
        results[website] = "Client Error"
    else:
        results[website] = "Server Error"

print(results)
