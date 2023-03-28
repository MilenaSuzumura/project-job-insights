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


def validate_salary_max_min(job, salary):
    max = int(job["max_salary"])
    min = int(job["min_salary"])
    if max > min and max >= salary >= min:
        return True

    return False


def is_not_list(job):
    if type(job) is not list:
        if "max_salary" not in job or "min_salary" not in job:
            return False
        return True
    return False


def validate_value_salary_range(job, salary):
    validateSalary = is_not_list(job)

    if validateSalary is True:
        test = validate_salary_max_min(job, salary)
        return test
    return False


def array_salary_range(jobs, salary):
    data = []
    for job in jobs:
        validateValues = validate_value_salary_range(job, salary)
        if validateValues is True:
            data.append(job)
    return data


def other_values_salary_range(jobs, salary):
    if type(salary) is str and salary != '':
        return array_salary_range(jobs, int(salary))
    return []


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    try:
        if type(salary) is int:
            return array_salary_range(jobs, salary)
        return other_values_salary_range(jobs, salary)
    except ValueError:
        raise ValueError
