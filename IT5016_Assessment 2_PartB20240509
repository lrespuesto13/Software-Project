
class BookingSystem:
    booking_id_counter = 1  
    total_bookings = 0  
    approved_bookings = 0  
    pending_bookings = 0  
    not_approved_bookings = 0  

    def __init__(self, customer_name, id_number, id_type):
        self.booking_id = BookingSystem.booking_id_counter
        BookingSystem.booking_id_counter += 1
        self.customer_name = customer_name
        self.id_number = id_number
        self.id_type = id_type
        self.status = "Pending"
        self.ferry_service = None
        self.total_cost = 0
        self.approval_reference = None

        BookingSystem.total_bookings += 1
        BookingSystem.pending_bookings += 1

    def ferry_service_details(self, service_name, price):
        self.ferry_service = service_name
        self.total_cost = price

    def booking_approval(self, is_approved):
        if self.status == "Pending":
            BookingSystem.pending_bookings -= 1
            if is_approved:
                self.status = "Approved"
                self.approval_reference = f"PAX{self.booking_id:02d}"
                BookingSystem.approved_bookings += 1
            else:
                self.status = "Not Approved"
                BookingSystem.not_approved_bookings += 1

    def display_booking_info(self):
        print(f"Form of ID: {self.id_type}")
        print(f"ID Number: {self.id_number}")
        print(f"Passenger Name: {self.customer_name}")
        print(f"Ticket ID: {self.booking_id}")
        print(f"Total: ${self.total_cost}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference or 'N/A'}\n")

    @staticmethod
    def booking_statistics():
        print(f"Total Bookings: {BookingSystem.total_bookings}")
        print(f"Approved Bookings: {BookingSystem.approved_bookings}")
        print(f"Pending Bookings: {BookingSystem.pending_bookings}")
        print(f"Not Approved Bookings: {BookingSystem.not_approved_bookings}\n")





booking1 = BookingSystem("Emily Clark", "PAX123", "Driver's License")
booking1.ferry_service_details("Service A", 280)

booking2 = BookingSystem("Paul Emma", "ID456", "International Passport")
booking2.ferry_service_details("Service B", 150)

booking3 = BookingSystem("Jane Smith", "ID789", "Driver's License")
booking3.ferry_service_details("Service C", 200)

booking4 = BookingSystem("Michael Lee", "ID101", "International Passport")
booking4.ferry_service_details("Service D", 320)

booking5 = BookingSystem("Sophia Davis", "PAX567", "Driver's License")
booking5.ferry_service_details("Service E", 100)

booking1.booking_approval(True)  
booking2.booking_approval(False)  
booking3.booking_approval(True)  
booking4.booking_approval(False)  
booking5.booking_approval(True)  


booking1.display_booking_info()
booking2.display_booking_info()
booking3.display_booking_info()
booking4.display_booking_info()
booking5.display_booking_info()


BookingSystem.booking_statistics()
