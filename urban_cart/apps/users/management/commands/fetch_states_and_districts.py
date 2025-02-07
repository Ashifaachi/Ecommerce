import requests
from django.core.management.base import BaseCommand
from apps.users.models import State,District
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_cart.settings')



# class Command(BaseCommand):
#     help = "Fetch Indian states and districts from an online API and populate the database"

#     def handle(self, *args, **kwargs):
#         # API URL (Replace this with a working API endpoint)
#         api_url = "https://github.com/sab99r/Indian-States-And-Districts/blob/master/states-and-districts.json"

#         try:
#             # Fetch data from the API
#             response = requests.get(api_url)
#             response.raise_for_status()  # Raise error if status != 200

#             # Parse JSON data
#             data = response.json()

#             # Iterate through states and districts
#             for item in data:
#                 state_name = item["state"]
#                 districts = item["districts"]

#                 # Create or get the State object
#                 state, created = State.objects.get_or_create(name=state_name)

#                 # Create districts for the state
#                 for district_name in districts:
#                     District.objects.get_or_create(name=district_name, state=state)

#             self.stdout.write(self.style.SUCCESS("Successfully populated states and districts!"))

#         except requests.exceptions.RequestException as e:
#             self.stdout.write(self.style.ERROR(f"Failed to fetch data from the API: {e}"))
#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

# def fetch_and_store_states_and_districts():
#     API_URL = "https://github.com/sab99r/Indian-States-And-Districts/blob/master/states-and-districts.json"  # Replace with correct API URL

#     try:
#         response = requests.get(API_URL)
#         response.raise_for_status()  # Raise exception for HTTP errors
#         data = response.json()  # Parse the JSON response
        
#         for state_data in data['states']:
#             # Create or get the state
#             state, created = State.objects.get_or_create(name=state_data['state'])

#             # Create districts for the state
#             for district_name in state_data['districts']:
#                 District.objects.get_or_create(name=district_name, state=state)
        
#         print("Data fetched and stored successfully.")

#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#     except ValueError as json_err:
#         print(f"JSON parsing error: {json_err}")
#         print("Response Content:", response.text)

# # Call the function to fetch and store data
# fetch_and_store_states_and_districts()
class Command(BaseCommand):
    help = 'Fetches states and districts from the API and stores them in the database'

    def handle(self, *args, **kwargs):
        try:
            # Raw URL to fetch the JSON file from GitHub
            url = 'https://raw.githubusercontent.com/sab99r/Indian-States-And-Districts/master/states-and-districts.json'
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

            # Parse JSON response
            data = response.json()

            # Iterate through the states and districts
            for state_data in data['states']:
                # Save or update the state
                state, created = State.objects.get_or_create(name=state_data['state'])

                # Save districts for each state
                for district_name in state_data['districts']:
                    District.objects.get_or_create(name=district_name, state=state)

            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved states and districts.'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Request error occurred: {e}'))
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Error processing the response data: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))

