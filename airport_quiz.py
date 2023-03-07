import random

def airport_traffic(month_days):
    # Initialize variables for total takeoffs and landings
    total_takeoffs = 0
    total_landings = 0
    
    # Set probabilities for takeoffs, landings, and bad weather
    takeoff_prob = 0.6
    landing_prob = 0.4
    bad_weather_prob = 0.3
    
    # Loop through each day of the month
    for day in range(0, month_days):
        # Generate a daily average for takeoffs and landings
        daily_avg_takeoffs = random.randint(50, 70)
        daily_avg_landings = random.randint(50, 70)
        
        # Determine if bad weather is present on this day
        is_bad_weather = random.random() < bad_weather_prob

        # If bad weather is present, reduce the number of takeoffs and landings
        if is_bad_weather:
            takeoffs = int(daily_avg_takeoffs * (1-takeoff_prob))
            landings = int(daily_avg_landings * (1-landing_prob))
    
        # If bad weather is not present, use the daily averages for takeoffs and landings
        else:
            takeoffs = int(daily_avg_takeoffs)
            landings = int(daily_avg_landings)

        # Print the number of takeoffs and landings for this day
        print(f"Day {day+1}: {takeoffs} takeoffs and {landings} landings")
        
        # Add the number of takeoffs and landings for this day to the total for the month
        total_takeoffs += takeoffs
        total_landings += landings

    # Convert the total number of takeoffs and landings to integers
    total_takeoffs = int(total_takeoffs)
    total_landings = int(total_landings)
    
    # Print the total number of takeoffs and landings for the month
    print(f"Total takeoffs for the month: {total_takeoffs}")
    print(f"Total landings for the month: {total_landings}")

airport_traffic(30)
