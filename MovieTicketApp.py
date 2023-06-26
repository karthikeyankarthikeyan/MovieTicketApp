import datetime

users = []
movieNames = []
bookings_list = []

class MovieList:
    def __init__(self, id, moviename, no_of_ticket, price):
        self.movieId = id
        self.movieName = moviename
        self.no_of_ticket = no_of_ticket
        self.Price = price

class Bookings:
    def __init__(self, BookingID, userId, BookedAt, movieDetails):
        self.booking_id = BookingID
        self.userId = userId
        self.booked_at = BookedAt
        self.movieDetails = movieDetails


class ticketApp:
    booking_count = 0

    def __init__(self, id: int, Name: str, Email: str, Password: str, Role: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        self.role = Role
        

    def hardCodedData(self):
        users.append(self)
        return users
    
    def validateLogin(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None
    

    def getUserName(self) -> str:
        return self.name


    def Welcome(self):
        print('Hi Welcome Customer', self.name)



class movieListings(ticketApp):
    def __init__(self, id, Name, Email, Password, Role):
        super().__init__(id, Name, Email, Password, Role)
        self.no_of_tickets = []  # Initialize an empty cart for the user


    def booking_for_customer(self):
        stayInCustomerMenu = True
        movie1 = MovieList(1, 'KGF',50,100)
        movie2 = MovieList(2, 'VARISU',50,110)
        movie3 = MovieList(3, 'VIKIRAM',60,120)
        movieNames.append(movie1)
        movieNames.append(movie2)
        movieNames.append(movie3)
        while stayInCustomerMenu:
            print("\n******************************")
            print("Customer Menu")
            print("1. List Of Movies")
            print("2. Select The Movies")
            print("3. Booked History")
            print("4. Delete your history")
            print("5. Logout")
            choice = int(input("Enter your Choice: "))


            if choice == 1:


                for movie in movieNames:
                    print(movie.movieId)
                    print(movie.movieName)
                    print(movie.no_of_ticket)
                    print(movie.Price)
                    print('---------------------------------------------')

            if choice == 2:
                while True:
                    print("Movies List:")
                    for movie in movieNames:
                        print(movie.movieId, movie.movieName, movie.no_of_ticket, movie.Price)
                    
                    movie_id = int(input("Enter the ID of the movie to add to bookings (or 0 to stop adding): "))
                    if movie_id == 0:
                        break
                    no_of_ticket = int(input("Enter the no_of_tickets: "))
                    selected_item = None
                    for movie in movieNames:
                        if movie.movieId == movie_id:
                            selected_item = movie
                            break
                    
                    if selected_item is None:
                        print("Invalid movie ID. Please try again.")
                    else:
                        total_price = int(selected_item.Price) * no_of_ticket
                        cart_item = {
                            'movieId': selected_item.movieId,
                            'movieName': selected_item.movieName,
                            'no_of_ticket': no_of_ticket,
                            'Price': total_price
                        }
                        self.no_of_tickets.append(cart_item)
                        print("Item added to booking successfully.")
                    view_cart = input("Do you want to see the booking? (y/n): ")
                    if view_cart.lower() == "y":
                        if len(self.no_of_tickets) == 0:
                            print("Your booking is empty.")
                        else:
                            print("Your Booking:")
                            for item in self.no_of_tickets:
                                print("Movie ID:", item['movieId'])
                                print("movie Name:", item['movieName'])
                                print("no_of_ticket:", item['no_of_ticket'])
                                print("Price:", item['Price'])
                                print('---------------------------------------------')
                        print("Payment Options:")
                        print("1. Card")
                        print("2. UPI")
                        
                        payment_choice = int(input("Choose a payment option: "))
                    
                        if payment_choice == 1:
                            print("Payment successful. Thank you for using card.")
                        elif payment_choice == 2:
                            print("Payment successful. Thank you for using UPI.")
                        else:
                            print("Invalid payment option.")
                        booking_data = Bookings(self.booking_count, self.userID, datetime.datetime.now(), self.no_of_tickets)
                        bookings_list.append(booking_data)
                        self.booking_count += 1  
                        break

            elif choice == 3:
                for booking in bookings_list:
                    print(f"Booking ID: {booking.booking_id}")
                    print(f"User ID: {booking.userId}")
                    print(f"Booked At: {booking.booked_at}")
                    for item in self.no_of_tickets:
                        print("movie Name:", item['movieName'])
                        print("no_of_ticket:", item['no_of_ticket'])
                        print("Price:", item['Price'])
                    print('---------------------------------------------')
            elif choice == 4:
                if len(bookings_list) == 0:
                    print("No booking history available.")
                else:
                    print("Booking History:")
                    for booking in bookings_list:
                        print("Booking ID:", booking.booking_id)
                        print("User ID:", booking.userId)
                        print("Booked At:", booking.booked_at)
                        print('---------------------------------------------')
            
                    delete_choice = input("Enter the Booking ID to delete the history (or 'n' to cancel): ")
                    if delete_choice == 'n':
                        print("Deletion canceled.")
                    else:
                        delete_choice = int(delete_choice)
                        deleted = False
                        for booking in bookings_list:
                            if booking.booking_id == delete_choice:
                                bookings_list.remove(booking)
                                deleted = True
                                break
                        if deleted:
                            print("Booking history deleted successfully.")
                        else:
                            print("Invalid Booking ID. Please try again.")
                            
            elif choice == 5:
                print("Logout Successfully")
                break
            else:
                print("Invalid Entry")
class AdminFlow(ticketApp):
    def __init__(self, id, Name, Email, Password, Role):
        super().__init__(id, Name, Email, Password, Role)

    def Welcome(self):
        print('Hi Welcome Admin')
        print(self.getUserName())          

if __name__ == "__main__":
    app = ticketApp(1, "Priya", "kamal@gmail.com", "kamal123", "customer")
    app.hardCodedData()
    app = ticketApp(2, "Kamali", "kamali@gmail.com", "kamali123", "Admin")
    app.hardCodedData()

    login_user = app.validateLogin("kamal@gmail.com", "kamal123")

    if login_user:
        print('Login Success')
        if login_user.role == "Admin":
            admin = AdminFlow(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
            admin.Welcome()
        elif login_user.role == "customer":
            app.Welcome()
            book = movieListings(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
            book.booking_for_customer()