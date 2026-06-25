# 7. Movie Ticket Booking: Book tickets until all seats are filled

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
        print("seats not available ")  
        break      