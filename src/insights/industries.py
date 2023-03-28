from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    people = read(path)
    industry = []

    for person in people:
        if not person["industry"] in industry and not person["industry"] == "":
            industry.append(person["industry"])

    return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industryFilter = []

    for job in jobs:
        if job["industry"] == industry:
            industryFilter.append(job)

    return industryFilter
