from eco_movement_api.client import EcoMovementClient
from eco_movement_api.models import Status

client = EcoMovementClient()

details = client.get_location_details('3771ff27e884611ebba6042010a84000')

print(details)
print(details.data.evses[0].status == Status.AVAILABLE)
