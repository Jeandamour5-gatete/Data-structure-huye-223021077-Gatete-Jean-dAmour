from collections import deque
cancellations_stack = []
ticket_queue = deque()
available_seats = [f"Seat {i+1}" for i in range(10)]  
def view_available_seats():
     print("Available Seats:",available_seats)
def book_ticket(customer_name):
    if available_seats:
        seat = available_seats.pop(0)
        ticket_queue.append((customer_name, seat))
        print(f"Ticket booked successfully! {customer_name} has been assigned {seat}.")
    else:
        print("No available seats. Please wait or check back later.")
def process_ticket():
    if ticket_queue:
        customer_name, seat = ticket_queue.popleft()
        print(f"Processing ticket for {customer_name} with {seat}.")
    else:
        print("No tickets to process.")
def cancel_ticket():
    if ticket_queue:
        customer_name, seat = ticket_queue.pop()
        cancellations_stack.append(seat)
        print(f"Ticket for {customer_name} has been canceled. {seat} is now available.")
    else:
        print("No tickets to cancel.")
def restore_seat():
    if cancellations_stack:
        seat = cancellations_stack.pop()
        available_seats.append(seat)
        print(f"{seat} has been restored to available seats.")
    else:
        print("No seats to restore.")
def view_current_available_seats():
     print("Available Seats:",available_seats)
view_available_seats()
book_ticket("Denis")
book_ticket("Eric")
book_ticket("Elie")
process_ticket()
cancel_ticket()
restore_seat()
process_ticket()
view_current_available_seats()