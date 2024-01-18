# Getting colours input
TGREEN = '\033[32m' # Green text
TRED = '\033[41m' # Red text
TBLUE = '\033[44m' # Blue text
TWHITE = '\033[37m' # White text

def hotel_cost(num_nights):
    # Assuming a fixed price per night at the hotel
    nightly_rate = 100  # You can adjust this value
    total_cost = num_nights * nightly_rate
    return total_cost

def plane_cost(city_flight):
    # Assigning different flight costs based on the destination city
         if city_flight == "New York":
           return 300  # Adjust this value for different cities
         elif city_flight == "Paris":
           return 500
         elif city_flight == "Tokyo":
           return 700
         else:
           return 0  # Default cost if the city is not recognized

def car_rental(rental_days):
    # Assuming a fixed darily rental cost for the car
    daily_rate = 50  # You can adjust this value
    total_cost = rental_days * daily_rate
    return total_cost

def holiday_cost(city_flight, num_nights, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_rental_cost = car_rental(rental_days)

    total_holiday_cost = total_hotel_cost + total_plane_cost + total_rental_cost
    return total_holiday_cost

# Getting user inputs
city_flight = input("Enter the city you will be flying to (e.g., New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculating and displaying the holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)
print( TBLUE + "\nHoliday Details:")
print( TGREEN + f"Destination: {city_flight}")
print(f"Hotel Cost: £{hotel_cost(num_nights)}")
print(f"Flight Cost: £{plane_cost(city_flight)}")
print(f"Car Rental Cost: £{car_rental(rental_days)}")
print( TRED + f"Total Holiday Cost: £{total_cost}")

