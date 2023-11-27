def convert_to_24_hour(hour, minute, period):
   
    # Adjust the hour for 12 AM and 12 PM
    if hour == 12:
        hour = 0 if period == 'am' else 12

    # Convert PM hours to 24-hour format
    elif period == 'pm':
        hour += 12

    # Format the time as HHMM
    return f"{hour:02d}{minute:02d}"

print(convert_to_24_hour(12, 30, 'pm'))
print(convert_to_24_hour(12, 0, 'am'))

# Path: Challenge-1/time.py

    
