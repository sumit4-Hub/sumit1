import calendar

def display_month(year, month):
    """Display the calendar for a specific month and year."""
    try:
        # Create a TextCalendar object
        cal = calendar.TextCalendar(calendar.SUNDAY)
        
        # Generate the calendar for the given month and year
        month_calendar = cal.formatmonth(year, month)
        
        # Print the calendar
        print(month_calendar)
    except calendar.IllegalMonthError:
        print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid year. Please enter a valid year.")

def main():
    # Get user input for the year and month
    try:
        year = int(input("Enter the year (e.g., 2024): "))
        month = int(input("Enter the month (1-12): "))
        
        # Display the calendar for the provided month and year
        display_month(year, month)
    except ValueError:
        print("Please enter valid integers for year and month.")

if __name__ == "__main__":
    main()
