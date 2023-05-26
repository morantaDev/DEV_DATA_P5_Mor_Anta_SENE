import requests

def get_car_reservation_data(pickup, dropoff, date):
  """Gets car reservation data from the Rentalcars Connect API.

  Args:
    pickup: The location where the car will be picked up.
    dropoff: The location where the car will be dropped off.
    date: The date of the rental.

  Returns:
    A JSON object containing information about the cars that are available for rent.
  """

  url = "https://rentalcars.com/api/v1/cars/availability?pickup={}&dropoff={}&date={}".format(
      pickup, dropoff, date)

  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("Error getting car reservation data: {}".format(response.status_code))


if __name__ == "__main__":
  # Get car reservation data for a rental from San Francisco International Airport (SFO)
  # to Los Angeles International Airport (LAX) on May 17, 2023.
  data = get_car_reservation_data("SFO", "LAX", "2023-05-17")

  # Print the data.
  print(data)



# hotelId = ['HSBCNARR', 'DSBCNOMM', 'XHBCN8LA', 'XHBEL232', 'XHBELHE9', 'XHBEL0RU', 'XHBCNBU7', 'ONBCNELP', 'UIBCNCCH', 'LWBCN430', 'HSBCNBCZ', 'PHBCNMUR', 'UIBCN265', 'WWBCNBAL', 'UIBCN987', 'HLBCN116', 'UIBCNNHO', 'HSBCNAED', 'WVBCNEMA', 'HSBCNAQP', 'UIBCNBAM', 'UIBCNHAG']
