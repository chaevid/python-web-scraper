from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
search_term = "python"

jobs = extract_wwr_jobs(search_term)
print(jobs)
