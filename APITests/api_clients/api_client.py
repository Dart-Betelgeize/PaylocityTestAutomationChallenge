import random
import requests

from api_clients.models.models import EmployeeData, GetEmployeeResponseBody, GetEmployeesListResponseBody
from response_validator import ResponseValidator

class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
        self.response_validator = ResponseValidator()  # Instantiate here directly

    def _send_get_request(self, endpoint: str, method: str = 'GET', **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Basic {self.token}",
        }

        response = requests.request(method, url, headers=headers, **kwargs)
        return response

    def get_employees(self) -> GetEmployeesListResponseBody:
        response = self._send_get_request("/employees")
        validated_response = self.response_validator.validate_response(response, GetEmployeesListResponseBody)
        
        return validated_response

    def get_employee(self, id: str) -> GetEmployeeResponseBody:
        response = self._send_get_request(f"/employees/{id}")
        validated_response = self.response_validator.validate_response(response, GetEmployeeResponseBody)
        
        return validated_response 

    def get_random_employee_from_list(self) -> EmployeeData:
        employees_list_response = self.get_employees()
        if not employees_list_response.body:
            raise ValueError("No employees available in the list.")
        random_employee = random.choice(employees_list_response.body)
        return random_employee