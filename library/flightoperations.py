
from datetime import datetime

bookings = dict()


def printFlightDetailsByDates(flightDict):
    
    
    if type(flightDict)==dict:
        dateSet = set()
        
        for key,value in flightDict.items():
            for flightName,scheduleList in value.items():
                for rec in scheduleList:
                    dateSet.add(rec['date'])
                    
        dateList = list(dateSet)
        dateList.sort(key=lambda date:datetime.strptime(date, "%d/%m/%Y"))
        
        for date in dateList:
            print(date)
            print("--------------------------------------------------------------------------------------------------------------")
            
            for key,value in flightDict.items():
                for flightName,scheduleList in value.items():
                    for rec in scheduleList:
                        if rec['date']==date:
                            print("%20s %20s %20s %20s %20s"%(key, flightName, rec['departure'], rec['arrival'], rec['cost']))
                
    else:
        print("Function Argument not match type Dictionary")
        
        
def printFlightsByDestination(flightDict, departure, arrival):
    if type(flightDict)==dict:
       
        availableFlights = list()
        
        for key,value in flightDict.items():
            for flightName,scheduleList in value.items():
                for rec in scheduleList:                    
                    if rec['departure']==departure and rec['arrival']==arrival:
                        availableFlights.append({'flightName':flightName, 'date':rec['date'], 'seats':rec['seats'], 'cost':rec['cost']})
                        print("%20s %20s %20d %20s"%(flightName, rec['date'], rec['seats'],rec['cost']))
        
        if len(availableFlights)==0:
            return None
        else:
            return availableFlights
        
    else:
        print("Function Argument not match type Dictionary")
        
        
def bookFlight(availableFlights):
    pos = int(input(f"select flight (1 to {len(availableFlights)}) :"))
    
    if pos>=1 and pos<=len(availableFlights):
        n = int(input("How many tickets you want to book? :"))
        if n>=1 and n<=6:
            for i in range(0, n):
                passportNo = input("Enter Passport number :")
                fname = input("Enter First Name :")
                lname = input("Enter Last Name :")
                gender = input("Enter Gender :")
                age = int(input("Enter age :"))
                user_depture = input("Enter From  :")
                user_arrival = input("Enter To :")
                
                bookings[passportNo] = {'flightName':availableFlights[pos-1]['flightName'], 'departure':user_depture, 'arrival':user_arrival, 'cost':availableFlights[pos-1]["cost"] , 'fname':fname, 'lname':lname, 'gender':gender, 'age':age}
        
            print("Your Flight Booking Details are :")                      
            print(bookings)
            
        else:
            print("Invalid Number of Bookings..")                
            
    else:
        print("You entered wrong position of the flight. please select Book flight")       

    return(bookings)     
            

def cancelticket(booklist):
    passno= int(input("Enter the password no you want to cancel the flight ticket"))
    booklist.pop(passno)

def reservations():
    return(bookings)
            
