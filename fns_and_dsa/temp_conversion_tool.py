from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Ask user for number of days
    days = int(input("Enter the number of days to add to the current date: "))
    # Save future date
    future_date = datetime.now() + timedelta(days=days)
    # Format as "YYYY-MM-DD"
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
 