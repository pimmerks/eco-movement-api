from eco_movement_api.client import EcoMovementClient
from eco_movement_api.models import Status

client = EcoMovementClient()

details = client.get_location_details('670a6ba993011e9949442010a8400035')

print(details)
print(details.data.evses[0].status == Status.AVAILABLE)
