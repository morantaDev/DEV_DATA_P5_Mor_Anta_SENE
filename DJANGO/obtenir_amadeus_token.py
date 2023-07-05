# import requests

import json
import requests

# # URL pour obtenir le jeton d'accès
# token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

# # Paramètres de la requête POST
# params = {
#     "grant_type": "client_credentials",
#     "client_id": "m6DhvrLb1NAoGygATfeD8lEpMKlQxva8",
#     "client_secret": "i7Npu291wpGAexgu"
# }

# # Envoi de la requête POST pour obtenir le jeton d'accès
# response = requests.post(token_url, data=params)

# # Extraction du jeton d'accès de la réponse JSON
# access_token = response.json()["access_token"]


# print(access_token)
# # Utilisez le jeton d'accès pour vos appels à l'API Amadeus
# ...

# curl "https://api.amadeus.com/v1/security/oauth2/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id={m6DhvrLb1NAoGygATfeD8lEpMKlQxva8}&client_secret={i7Npu291wpGAexgu}"



##################################################################################################

# Install the Python library from https://pypi.org/project/amadeus

# this code is working

# hotel list datas

# from amadeus import ResponseError, Client

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Get list of hotels by city code
#     '''
#     response = amadeus.reference_data.locations.hotels.by_city.get(cityCode='PAR')

#     print(response.data)
# except ResponseError as error:
#     raise error


###################################################################################################
# Install the Python library from https://pypi.org/project/amadeus

#This code doesn't work

#hotels by hotels

# from amadeus import ResponseError, Client

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Get list of hotels by hotel id
#     '''
#     response = amadeus.reference_data.locations.hotels.by_hotels.get(hotelIds='ADPAR001')

#     print(response.data)
# except ResponseError as error:
#     raise error


######################################################################################

#hotels_by_geocode

#This code is working

# Install the Python library from https://pypi.org/project/amadeus
# from amadeus import ResponseError, Client

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Get list of hotels by a geocode
#     '''
#     response = amadeus.reference_data.locations.hotels.by_geocode.get(longitude=2.160873,latitude=41.397158)

#     print(response.data)
# except ResponseError as error:
#     raise error

####################################################################################

# airport and city search


# # Install the Python library from https://pypi.org/project/amadeus
# from amadeus import Client, ResponseError
# from amadeus import Location

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Which cities or airports start with 'r'?
#     '''
#     response = amadeus.reference_data.locations.get(keyword='r',
#                                                     subType=Location.ANY)
#     print(response.data)
# except ResponseError as error:
#     raise error


############################################################################

# def insert_Vol():
#     flight_data =[]
#     with open('/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/DJANGO/data1.json', 'r') as file:
#         flight_data = json.dumps(file.read())
#         print(flight_data[0])


# def insert_Vol():
#   with open('/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/projet_django/fisrt_projet/myapp/data.json', 'r') as file:
#     flight_data = file.read()
#     flight_data = json.loads(file)
#     # flight_data['type'] = 'flight-offer'
#     print(flight_data)

# insert_Vol()
    # flight_data = json.loads(file)
    # flight_data['type'] = 'flight-offer'
        # for row in file:
            # print(row)
            # data = json.load(row)
            # flight_data.append(row)
        
    # return data
    
    
# with open('/home/moranta/django_reservations/data.json') as file:
#     json_data = file.read()
#     json_data = json_data.replace("'", '"')
#     data = json.loads(json_data)  # Parse the JSON data
#     print(data)


#####################################################################
# Install the Python library from https://pypi.org/project/amadeus
#this code is working

#aiport_route(contain name, city, )

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     What are the destinations served by BLR airport?
#     '''
#     response = amadeus.airport.direct_destinations.get(departureAirportCode='MAD')
#     print(response.data)
# except ResponseError as error:
#     raise error


############################################################
#traveled_destination

# Install the Python library from https://pypi.org/project/amadeus

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     body = {
#         "originDestinations": [
#             {
#                 "id": "1",
#                 "originLocationCode": "MIA",
#                 "destinationLocationCode": "ATL",
#                 "departureDateTime": {
#                     "date": "2023-11-01"
#                 }
#             }
#         ],
#         "travelers": [
#             {
#                 "id": "1",
#                 "travelerType": "ADULT"
#             }
#         ],
#         "sources": [
#             "GDS"
#         ]
#     }

#     response = amadeus.shopping.availability.flight_availabilities.post(body)
#     print(response.data)
# except ResponseError as error:
#     raise error


#############################################################################

#City search

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )
# try:
#     '''
#     What are the cities matched with keyword 'Paris' ?
#     '''
#     response = amadeus.reference_data.locations.cities.get(keyword='London')
#     print(response.data)
# except ResponseError as error:
#     raise error


######################################################################

#this code is working

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )
# try:
#     '''
#     Find the probability of the flight MAD to NYC to be chosen
#     '''
#     body = amadeus.shopping.flight_offers_search.get(originLocationCode='MAD',
#                                                      destinationLocationCode='NYC',
#                                                      departureDate='2023-11-01',
#                                                      returnDate='2023-11-09',
#                                                      adults=1).result
#     response = amadeus.shopping.flight_offers.prediction.post(body)
#     print(response.data)
# except ResponseError as error:
#     raise error


########################################################################
# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     # Retrieve all airports
#     response = amadeus.reference_data.locations.get(
#         subType='AIRPORT'
#     )
#     airports = response.data
#     for airport in airports:
#         print(airport['iataCode'], airport['name'])
# except ResponseError as error:
#     print(f"An error occurred: {error}")



###########################################################################
#airport and city search

# from amadeus import Client, ResponseError
# from amadeus import Location
# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Which cities or airports start with 'r'?
#     '''
#     response = amadeus.reference_data.locations.get(keyword='r',
#                                                     subType=Location.ANY)
#     print(response.data)
# except ResponseError as error:
#     raise error



################################################################


# flight offer Price

# from amadeus import Client, ResponseError
# # from amadeus import Location
# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )



# try:
#     '''
#     Confirm availability and price from SYD to BKK in summer 2022
#     '''
#     flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
#                                                         departureDate='2023-07-01', adults=1).data
#     response_one_flight = amadeus.shopping.flight_offers.pricing.post(
#         flights[0])
#     print(response_one_flight.data)

#     response_two_flights = amadeus.shopping.flight_offers.pricing.post(
#         flights[0:2])
#     print(response_two_flights.data)
# except ResponseError as error:
#     raise error


##############################################################################
# this code is working

# flight offer search

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     Find the cheapest flights from SYD to BKK
#     '''
#     response = amadeus.shopping.flight_offers_search.get(
#         originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2023-06-01', adults=1)
#     print(response.data)
# except ResponseError as error:
#     raise error


#########################################################################################


# hotels offers

# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     # Get list of available offers in specific hotels by hotel ids
#     hotels_by_city = amadeus.shopping.hotel_offers_search.get(
#         hotelIds='RTPAR001', adults='2', checkInDate='2023-10-01', checkOutDate='2023-10-04')
#     print(hotels_by_city.data)
# except ResponseError as error:
#     raise error


###############################################################################
# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     # Get list of hotel offers by city code
#     hotels_by_city = amadeus.shopping.hotel_offers_search.get(cityCode='CITY_CODE')
#     print(hotels_by_city.data)
# except ResponseError as error:
#     print(error)

#########################################################################################
# from ast import keyword
# from amadeus import Client, ResponseError

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# try:
#     '''
#     What are the location scores for the given coordinates?
#     '''
#     response = amadeus.location.analytics.category_rated_areas.get(latitude=41.397158, longitude=2.160873)
#     print(response.data)
# except ResponseError as error:
#     raise error

################################################################################
# from amadeus import Client, ResponseError
# import random

# amadeus = Client(
#     client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
#     client_secret='i7Npu291wpGAexgu'
# )

# city_code = 'PAR'  # Replace with the desired city code

# try:
#     # Search for hotel offers in the specified city
#     response = amadeus.shopping.hotel_offers_search.get(cityCode=city_code)

#     # Get the list of hotel offers
#     hotel_offers = response.data

#     num_hotels = 5  # Number of random hotels to generate

#     # Select random hotels from the available offers
#     random_hotels = random.sample(hotel_offers, num_hotels)

#     for hotel in random_hotels:
#         hotel_name = hotel['hotel']['name']
#         room_capacity = random.randint(1, 4)
#         room_description = hotel['offers'][0]['room']['description']
        
#         print(f"Hotel: {hotel_name}")
#         print(f"Room Capacity: {room_capacity}")
#         print(f"Description: {room_description}")
#         print()

# except ResponseError as error:
#     print(error)



###########################################################################################
#my code that generate hotel

# import random

# hotels = ['Hotel A', 'Hotel B', 'Hotel C', 'Hotel D', 'Hotel E']
# room_types = ['Single Room', 'Double Room', 'Suite', 'Deluxe Room', 'Family Room']

# def generate_hotel():
#     hotel = random.choice(hotels)
#     room_capacity = random.randint(1, 4)
#     room_type = random.choice(room_types)
#     description = f"{room_type} at {hotel}"
#     return hotel, room_capacity, description

# num_hotels = 5

# for _ in range(num_hotels):
#     hotel, room_capacity, description = generate_hotel()
#     print(f"Hotel: {hotel}")
#     print(f"Room Capacity: {room_capacity}")
#     print(f"Description: {description}")
#     # print()


###########################################################################################
from faker import Faker
import random

fake = Faker()

hotels = []

image_available = [
    {"name":"chambre_simple", "url": "https://images.unsplash.com/flagged/photo-1556438758-8d49568ce18e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1174&q=80"},
    {"name": "chambre_double", "url": "https://unsplash.com/fr/photos/_Sr6plc5dpQ"},
    {"name": "chambre_de_luxe", "url":"https://images.unsplash.com/photo-1519710889408-a67e1c7e0452?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80"},
    {"name":"suite", "url":"https://unsplash.com/fr/photos/AOBEP4Qq00s"}
     
]
image_url=""
for _ in range(100):
    room=random.choice(["chambre_simple", "chambre_double", "chambre_de_luxe", "suite"])
    for img_url in image_available:
        if room==img_url['name']:
            image_url = img_url['url']
    hotel = {
        "name": fake.company(),
        "room" :room,
        "description": fake.text(),
        "capacity": fake.random_int(min=1, max=6),
        "address": fake.address(),
        "city": fake.city(),
        "country": fake.country(),
        "image_url" : image_url
    }
    hotels.append(hotel)

print(hotels)

