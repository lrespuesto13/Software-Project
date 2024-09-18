class BookingSystem:
    
    def __init__(self):
        """
        Initializes the booking system with default values.
        Encapsulates customer information and booking status within the class.
        """
        self.bookings = []  # Stores all bookings in a list for easy management.
        self.pending_count = 0
        self.approved_count = 0
        self.not_approved_count = 0
    
    def submit_booking(self, customer_id, customer_name, id_type):
        """
        Allows customers to submit their booking with an ID, name, and type of identification.
        The method encapsulates all user information and returns a unique booking ID.
        """
        booking_id = len(self.bookings) + 1  # Auto-incrementing booking ID.
        self.bookings.append({
            'id': booking_id,
            'customer_id': customer_id,
            'name': customer_name,
            'id_type': id_type,
            'status': 'Pending'
        })
        self.pending_count += 1  # Update pending bookings count.
        print(f"Booking ID {booking_id} submitted and pending approval.")

    def ferry_service_details(self, service_name, service_price):
        """
        Allows customers to choose a ferry service. Returns the total cost based on the input service.
        Demonstrates encapsulation by keeping service details within the class.
        """
        total_cost = service_price  # In a real system, this might include tax calculations or discounts.
        print(f"Service '{service_name}' selected with a total price of ${total_cost}.")
        return total_cost

    def booking_approval(self, booking_id, manager_decision):
        """
        Allows a manager to approve or reject a booking. Updates the status of the booking accordingly.
        This follows the business rule where bookings require approval before they are confirmed.
        """
        for booking in self.bookings:
            if booking['id'] == booking_id:
                if manager_decision == 'approve':
                    booking['status'] = 'Approved'
                    self.approved_count += 1
                    self.pending_count -= 1
                elif manager_decision == 'reject':
                    booking['status'] = 'Not Approved'
                    self.not_approved_count += 1
                    self.pending_count -= 1
                print(f"Booking ID {booking_id} has been {booking['status']}.")
                return
        print("Booking ID not found.")
    
    def booking_statistics(self):
        """
        Returns booking statistics such as the total number of bookings, approved, pending, and not approved.
        This provides insights for decision-making and managerial oversight.
        """
        total_bookings = len(self.bookings)
        print(f"Total Bookings: {total_bookings}")
        print(f"Approved Bookings: {self.approved_count}")
        print(f"Pending Bookings: {self.pending_count}")
        print(f"Not Approved Bookings: {self.not_approved_count}")
