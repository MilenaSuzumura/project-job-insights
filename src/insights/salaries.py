from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    people = read(path)
    maxSalary = 0

    for person in people:
        try:
            max_salary = int(person["max_salary"])
            if max_salary > maxSalary:
                maxSalary = int(person["max_salary"])
        except ValueError:
            pass

    return maxSalary


def get_min_salary(path: str) -> int:
    people = read(path)
    minSalary = 99999999999999

    for person in people:
        try:
            min_salary = int(person["min_salary"])
            if min_salary < minSalary:
                minSalary = int(person["min_salary"])
        except ValueError:
            pass

    return minSalary


def validate_salary(job):
    if "max_salary" not in job or "min_salary" not in job:
        return False

    maxSalary = type(job["max_salary"]) is int
    minSalary = type(job["min_salary"]) is int

    if maxSalary is True and minSalary is True:
        return True

    return False


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        validate = validate_salary(job)

        if validate is False:
            raise ValueError

        max = int(job["max_salary"])
        min = int(job["min_salary"])
        valueSalary = salary if type(salary) is int else int(salary)

        if min > max:
            raise ValueError

        return max >= valueSalary >= min
    except ValueError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
