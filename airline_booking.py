from flights_data import flights

def show_flights():
    print("\n🛫 Available Flights:\n")
    print(f"{'ID':<5}{'From':<15}{'To':<15}{'Time':<10}{'Price ($)':<10}")
    print("-" * 55)
    for flight in flights:
        print(f"{flight['id']:<5}{flight['from']:<15}{flight['to']:<15}{flight['time']:<10}{flight['price']:<10}")

def book_ticket():
    try:
        flight_id = int(input("\nEnter Flight ID to book: "))
        selected = next((f for f in flights if f['id'] == flight_id), None)

        if not selected:
            print("❌ Invalid flight ID.")
            return

        name = input("Enter your full name: ")
        email = input("Enter your email: ")

        print("\n✅ Booking Confirmed!\n")
        print("🎫 Ticket Details")
        print("-" * 25)
        print(f"Passenger Name: {name}")
        print(f"Email: {email}")
        print(f"Flight: {selected['from']} ➜ {selected['to']}")
        print(f"Time: {selected['time']}")
        print(f"Price: ${selected['price']}")
        print("-" * 25)

    except ValueError:
        print("❗ Please enter a valid number.")

def main():
    print("✈️ Welcome to Airline Booking System ✈️")
    while True:
        print("\n1. View Flights\n2. Book a Ticket\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            show_flights()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("👋 Thank you for using the system. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
