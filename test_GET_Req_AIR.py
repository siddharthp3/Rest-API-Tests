import requests
import pytest


@pytest.fixture(scope='class')
def get_all_airline_data(request):
    base_url = "https://api.instantwebtools.net/v1/airlines"
    r = requests.get(base_url)
    request.cls.res_obj = r

@pytest.mark.usefixtures("get_all_airline_data")
class Base_Test_GET():
    pass

class Test_Airline_data(Base_Test_GET):

    def test_all_airlines_data_status_code(self):
        assert self.res_obj.status_code == 200

    def test_total_no_airline(self):
        json_response = self.res_obj.json()
        assert len(json_response) == 555

    def test_name_of_airlines(self):
        json_response = self.res_obj.json()
        assert json_response[0]['name'] == "Thai Airways"


    def test_name_and_id_of_airline(self):
        json_response = self.res_obj.json()
        for airline in json_response:
            if airline['id'] == 1:
                assert airline['name'] == "Quatar Airways"
                break
    
    def test_time_taken(self):
        assert self.res_obj.elapsed.total_seconds() < 2
