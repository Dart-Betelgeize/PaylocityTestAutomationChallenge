from pydantic import ValidationError, BaseModel
import requests
from api_clients.models.models import GetEmployeesListResponseBody, EmployeeData

class ResponseValidator:
    @staticmethod
    def validate_response(response: requests.Response, model: BaseModel) -> BaseModel:
        """
        Validate the API response's status code and body using the provided model.
        :param response: The API response object.
        :param model: The Pydantic model containing expected structure and allowed status codes.
        :return: A validated model instance.
        """
        try:
            response_json = response.json()
        except ValueError:
            raise AssertionError("Response body is not valid JSON")
        
        # Validate status code against allowed values (200 or 500)
        # Probably not the best idea to keep codes here and validate it in this way. Need time to think
        if response.status_code not in [200, 500]:
            raise AssertionError(f"Unexpected status code: {response.status_code}. Allowed values are: 200, 500.")

        # Handle list response (e.g., GetEmployeesListResponseBody)
        if isinstance(response_json, list):
            response_data = {
                "status_code": response.status_code,
                "body": response_json  # Directly use the list as the body
            }
        # Handle dict response (e.g., GetEmployeeResponseBody)
        elif isinstance(response_json, dict):
            response_data = {**response_json, "status_code": response.status_code}
        else:
            raise AssertionError(f"Unexpected response body format: {type(response_json)}")
    
        try:
            # Validate the response using the provided model
            validated_response = model.model_validate(response_data)
        except ValidationError as e:
            raise AssertionError(f"Invalid response structure: {e}")

        return validated_response
