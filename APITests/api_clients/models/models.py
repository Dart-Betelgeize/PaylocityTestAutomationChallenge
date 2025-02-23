from pydantic import BaseModel
from typing import List

class EmployeeData(BaseModel):
    partitionKey: str
    sortKey: str
    username: str
    id: str
    firstName: str
    lastName: str
    dependants: int
    expiration: str
    salary: int
    gross: int
    benefitsCost: float
    net: float

class GetEmployeesListResponseBody(BaseModel):
    status_code: int
    body: List[EmployeeData] = []

class GetEmployeeResponseBody(BaseModel):
    status_code: int
    partitionKey: str
    sortKey: str
    username: str
    id: str
    firstName: str
    lastName: str
    dependants: int
    expiration: str
    salary: int
    gross: int
    benefitsCost: float
    net: float
