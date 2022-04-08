from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Edith cases")
class TestUserGet(BaseCase):
    @allure.description("Test edit just created user")
    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/api/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        # Assertions.assert_json_has_keys(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/api/use/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )
