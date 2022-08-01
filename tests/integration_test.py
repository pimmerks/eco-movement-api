from eco_movement_api.client import EcoMovementClient

def test_get_location():
    client = EcoMovementClient()
    details = client.get_location_details('0c099e6813411ebadeb42010a8400038')

    assert details.status_code == 1000
    assert details.status_message == "OK"

    assert details.data.country == "NLD"
