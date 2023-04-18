from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print(f"Failed to get jobs. Status code: {response.status_code}")
    # raise Exception("Failed to get jobs")
else:
    print(response.text)
