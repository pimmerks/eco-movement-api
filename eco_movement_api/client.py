import requests
import jsons

from eco_movement_api.exception import ApiException
from eco_movement_api.models import LocationApiResponse


class EcoMovementClient:
    """Client for eco-movement REST api."""

    BASEURL = 'https://maps.eco-movement.com/api'

    def get_location_details(self, location_id: str) -> LocationApiResponse:
        """Get the details of a charging station location.

        Args:
            location_id (str): The id of the location

        Raises:
            ApiException: When the station could not be found or any other error occurs.

        Returns:
            LocationApiResponse: A LocationApiResponse object.
        """
        r = requests.get(f'{self.BASEURL}/map/location/{location_id}')
        json = r.json()
        instance = jsons.load(json, LocationApiResponse)

        if instance.status_code != 1000:
            raise ApiException(instance.status_message, instance.status_code)

        return instance
