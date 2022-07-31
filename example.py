from oplaadpalen_api.client import OplaadpalenClient
from oplaadpalen_api.models import Status

client = OplaadpalenClient()

details = client.get_location_details('3771ff27e884611ebba6042010a84000')

print(details)
print(details.data.evses[0].status == Status.AVAILABLE)
