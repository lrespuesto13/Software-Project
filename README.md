
# Ferry Booking System

## Overview

This project is a prototype of a Ferry Booking System that allows customers to submit booking requests, choose ferry services, and have their bookings approved or rejected. The system tracks all bookings and provides statistical information about the booking statuses, including approved, pending, and not approved bookings. This project demonstrates the use of **Object-Oriented Programming (OOP)** principles to solve real-world problems.

## Features

- Allows customers to submit basic booking information (ID number, name, and form of ID).
- Enables ferry service selection, including service name and price calculation.
- Implements a booking approval system where managers can approve or reject bookings based on service requests.
- Tracks and displays booking statistics (total bookings, approved bookings, pending bookings, not approved bookings).
- Provides a summary of booking information, including the approval reference number.

## How to Run the Project

1. Clone or download the repository from GitHub.
2. Ensure you have Python 3.x installed on your machine.
3. Open the terminal/command prompt and navigate to the folder where the files are stored.
4. Run the Python file using the following command:

```bash
python booking_system.py
```

5. Follow the prompts to submit bookings and view booking statistics.

## Programming Concepts Used

### Object-Oriented Programming (OOP)

- **Encapsulation**: The `BookingSystem` class encapsulates all booking-related information, including customer details and ferry service requests.
- **Methods**: The class methods such as `ferry_service_details()`, `booking_approval()`, and `display_booking_info()` allow for specific operations like service selection, approval, and displaying results.
- **Class Variables**: A class-level variable is used to generate unique booking IDs for each new booking.

### Error Handling
- Error handling is implemented to ensure that valid data is provided by users, such as proper service names and valid pricing.

### Modularity
- The program is divided into separate methods within the `BookingSystem` class, ensuring that each method has a single responsibility (e.g., handling service details, approvals, or statistics).

### Scalability
- The system is designed to be easily extendable. Future modifications could include integrating a database for persistent booking storage or implementing additional services and pricing tiers.

## Folder Structure

- `booking_system.py`: The main Python file that contains the implementation of the Ferry Booking System.
- `README.md`: This file, which contains project instructions and an overview.

## Analytical Commentary

Throughout the project, key programming principles are applied:
- **OOP Principles**: The use of classes and methods ensures that the code is organized, modular, and reusable. The encapsulation of data (e.g., customer name, ID, booking status) helps manage and track booking requests.
- **Data Tracking**: The system provides clear mechanisms for tracking the state of each booking and allows for managerial decision-making (approval/rejection).
- **User Interaction**: The system handles user inputs in a structured way, guiding them through the booking and approval process.

## Future Improvements

- **Database Integration**: To store bookings persistently.
- **Web or GUI Interface**: Developing a graphical interface for better user interaction.
- **More Robust Error Handling**: Improve input validation to handle incorrect data entries.

## License

This project is open-source and available for educational purposes. You can modify and use it as per your needs.

