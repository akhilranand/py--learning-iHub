# Bus Seat Reservation: Reserve seats until bus is full.

totalSeats = 5

while True:
    book = input("Do you want to Book ticket (y/n) : ")
    if totalSeats > 0:
        if book == "y" :
            totalSeats -= 1
            print("ticket booked")
        else:
            print("Exit")
            break     
    else:
        print("seats not available bus is full ")  
        break      