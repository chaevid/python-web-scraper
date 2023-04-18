from bs4 import BeautifulSoup
import requests


def extract_job_info(job_element):
    job_title = job_element.find("h2", {"itemprop": "title"}).get_text()
    company_name = job_element.find("h3", {"itemprop": "name"}).get_text()
    job_url = "https://remoteok.com" + job_element.find(
        "a", {"itemprop": "url"})["href"]
    return {"title": job_title, "company": company_name, "url": job_url}


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        job_elements = soup.find_all("tr", {"class": "job"})
        jobs = [extract_job_info(job_element) for job_element in job_elements]
        for job in jobs:
            print(
                f"Job Title: {job['title']}\nCompany: {job['company']}\nURL: {job['url']}\n"
            )
    else:
        print("Can't get jobs.")


extract_jobs("rust")
