'''
import phonenumbers

from phonenumbers import carrier, geocoder, timezone

mobileNo=input("Enter mobile number with courntry code:") 
mobileNo=phonenumbers.parse(mobileNo)

print("Is number valid:",phonenumbers.is_valid_number(mobileNo))
print("Time Zone:", timezone.time_zones_for_number(mobileNo))
print("Carrier Name:",carrier.name_for_number(mobileNo,"en"))
print("Location:",geocoder.description_for_number(mobileNo,"en"))
'''


import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="phone_locator")
    location = geolocator.geocode(location)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def main():
    mobile_no = input("Enter mobile number with country code: ")

    try:
        # Parse the phone number
        mobile_no = phonenumbers.parse(mobile_no)

        # Check if the number is valid
        if not phonenumbers.is_valid_number(mobile_no):
            print("The number is not valid.")
            return

        # Get time zone
        time_zones = timezone.time_zones_for_number(mobile_no)
        print("Time Zone:", time_zones)

        # Get carrier name
        carrier_name = carrier.name_for_number(mobile_no, "en")
        print("Carrier Name:", carrier_name)

        # Get location
        location = geocoder.description_for_number(mobile_no, "en")
        print("Location:", location)

        # Get coordinates
        coordinates = get_coordinates(location)
        if coordinates:
            print("Coordinates:", coordinates)
        else:
            print("Coordinates not found for the location.")

    except phonenumbers.phonenumberutil.NumberParseException:
        print("The phone number entered is not in a valid format.")

if __name__ == "__main__":
    main()
