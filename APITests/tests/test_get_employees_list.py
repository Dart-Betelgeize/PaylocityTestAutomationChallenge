from utils.env_data import USERNAME

def test_get_employees_list(api_client):
    # When
    response = api_client.get_employees()
    # Then
    # Response parameters are already validated inside the get_employees()
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert len(response.body) > 0, "Employee list should not be empty"
    assert response.body[0].partitionKey == USERNAME, "PartitionKey should be equal to username"
    assert response.body[0].username == USERNAME, "Username should be equal to the provided username"