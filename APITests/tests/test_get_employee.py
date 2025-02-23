from utils.env_data import USERNAME

def test_get_valid_employee(api_client):
    # Given
    # I would rather get the employee id from DB and compare results with DB
    random_employee =  api_client.get_random_employee_from_list()
    random_employee_id = random_employee.id
    # When
    response = api_client.get_employee(random_employee_id)
    # Then
    # Response parameters are already validated inside the get_employees()
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert response.partitionKey == USERNAME, "PartitionKey should be equal to username"
    assert response.username == USERNAME, "Username should be equal to the provided username"
    assert response.id == random_employee_id, "Id should match the id in the request"
    assert response.sortKey == random_employee_id, "sortKey should match the id in the request"
    assert response.id == random_employee_id, "Id should match the id in the request"

# Here I would implement more tests for GET employee endpoint:
# - Get with invalid ID
# etc... I will skip this tests in this challenge due of lack of time
