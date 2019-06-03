def get_all_flights(items):
    flights = []

    for flight in items:
        item = {
            'airline': flight.airline,
            'arrivalLocation': flight.arrival_location,
            'arrivalTime': flight.arrival_time.strftime('%H:%M'),
            'createdAt': flight.created_at.strftime('%Y-%m-%d'),
            'departureDate': flight.departure_date.strftime('%Y-%m-%d'),
            'departureLocation': flight.departure_location,
            'departureTime': flight.departure_time.strftime('%H:%M'),
            'flightCode': flight.flight_code,
            'id': flight.id,
            'isDeleted': flight.is_deleted,
            'noOfSeats': flight.no_of_seats,
            'price': flight.price,
            'status': flight.status.value,
            'updatedAt': flight.updated_at.strftime('%Y-%m-%d')
        }
        flights.append(item)

    return flights