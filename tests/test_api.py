import requests
import pytest

class TestAPITesting:


    """Fixture to get the API response for user details."""
    @pytest.fixture(scope="class")
    def get_users_response(self):
        
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
        response = requests.get(url)
        return response.json()


    def test_get_users_api(self, get_users_response):
        response_json = get_users_response
        if "error" in response_json and response_json["error"].get("status") == 401:
            pytest.fail("Session expired. Cannot retrieve user data.")

        assert "data" in response_json, "Response does not contain 'data'."



    """Test to validate the structure of the JSON response."""
    def test_structure_validation(self, get_users_response):
        response_json = get_users_response
        for user in response_json["data"]:
            assert "userName" in user, "User details do not contain 'userName'."
            assert "status" in user, "User details do not contain 'status'."
            assert "role" in user, "User details do not contain 'role'."
