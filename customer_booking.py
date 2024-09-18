
def customerBooking():
    id_type = input ("Enter form of ID(Passport, driver's license): ")

    id_number = input("Enter ID Number: ")

    passenger_name = input ("Enter Passenger Name: ")
    ticket_id = 2000
    customerBooking.counter += 1

    ticket_id += customerBooking.counter

    print("\nPrinting Booking Information: ")
    print(f"Form of ID (Passport, driver's license): {id_type}")
    print(f"ID Number: {id_number}")
    print(f"Passenger Name: {passenger_name}")
    print(f"Ticket ID: {ticket_id}")
    return ticket_id, passenger_name, id_number

    customerBooking.counter: 0

def ferry_service_total ():
    
    ticket_id, passenger_name, id_number= customerBooking()

    total_cost= 0

    while True:
        service= input("\n Enter service name (or 'done' to finish): ")

        if service.lower() == 'done': break
        try:
            price = float(input(f"Enter the price for {service}: $"))
            total_cost += price
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price. ")

            print("\n Total Cost: $", total_cost)
            return total_cost

def booking_approval(ticket_id, passenger_id, total_cost):

    status = "Pending"

    if total_cost > 0:
        status = "Approved"
    
    approval_reference_number = passenger_id[:3] + str(ticket_id)[-2:]

    return status, approval_reference_number

def display_booking(id_type, passenger_id, passenger_name, tikcet_id, total_cost, status, approval_reference_number):

    print("\nPrinting Booking:")
    print(f"Form of ID (Passport, driver's license): {id_type}")
    print(f"ID Number (Passport, driver's license): {id_type}")
    print(f"Passenger Name : {passenger_name}")
    print(f"Ticket ID : {tikcet_id} ")
    print(f"Total: ${total_cost}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_reference_number}")

def main():
    
    ticket_id, passenger_name, passenger_id = customerBooking()
    total_cost = ferry_service_total()

    
    status, approval_reference_number = booking_approval(ticket_id, passenger_id, total_cost)

    
    id_type = "Driver's License"  
    display_booking(id_type, passenger_id, passenger_name, ticket_id, total_cost, status, approval_reference_number)


main()