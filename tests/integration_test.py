from oplaadpalen_api.client import OplaadpalenClient

def test_get_location():
    client = OplaadpalenClient()
    details = client.get_location_details('3771ff27e884611ebba6042010a84000')

    assert details.status_code == 1000
    assert details.status_message == "OK"

    assert details.data.country == "NLD"
