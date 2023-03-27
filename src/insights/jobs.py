from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    people = []
    with open(path, "r", encoding='utf-8') as file_in:
        data = csv.DictReader(file_in, delimiter=',')

        for person in data:
            people.append(person)

    return people


def get_unique_job_types(path: str) -> List[str]:
    people = read(path)
    test = []

    for person in people:
        test.append(person)
        print(test)
    return len(people)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
