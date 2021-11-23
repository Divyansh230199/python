'''
1. Print Flights by Dates
2. Book Flight
3. Cancel Ticket
4. Show Reservations By 
   a. Flight Type    b. Flight Name
'''

import sample.flights as records
import library.flightoperations as F
#from ticketbooking.library.flightoperations import cancelticket



while True:
    print("1. Print Flights By Dates")
    print("2. Book Flight")
    print("3. Cancel Ticket [Ass]")
    print("4. Show Reservations [Ass]")
    print("5. Exit")

    choice = int(input("Select Option :"))

    if choice==1:
        F.printFlightDetailsByDates(records.flightRecords)
        
    elif choice==2:
        user_depture = input("Enter From  :")
        user_arrival = input("Enter To :")
        
        availableFlights = F.printFlightsByDestination(records.flightRecords, user_depture, user_arrival )
        
        if(availableFlights==None):
            print("Flights not available at this route.")
        else:
            F.bookFlight(availableFlights)

                
    elif choice==4:
        booklist = F.reservations()
    elif choice==3:
        booklist= F.reservations()
        cancellation = F.cancelticket(booklist)
    elif choice==5:
        break
