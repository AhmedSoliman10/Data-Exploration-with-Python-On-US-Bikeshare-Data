import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#----------------------------------------------------------------------------------------------------------------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! My Name is Ahmed Soliman Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nChicago : 1')
    print('New York : 2')
    print('Washington : 3')
    city = input('Specify the city name or number to begin analyzing the data: ')
    city = city.lower()
    while True:     # while loop for handling the unexpected input by user
            if city == '1' or city == 'chicago':
                print("\nYou Have Choosen Chicago City!\n")
                city = 'chicago'
                break
            elif city == '2' or city == 'new york':
                print("\nYou Have Choosen New York City!\n")
                city = 'new york city'
                break
            elif city == '3' or city == 'washington':
                print("\nYou Have Choosen Washington City!\n")
                city = 'washington'
                break
            else:
                city = input('\nYou have choosen a non valid city ,Please specify the city name or number to analyze correctly: ')
                city = city.lower()
    # get user input for month (all, january, february, ... , june)
    month = input('Please enter a month from january to june to analyze or "all" to apply no month filter: ')
    month = month.lower()
    while True:
        if month in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            break
        else:
            month = input("\nSorry, your input should be: january, february, march, april, may, june or all: ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease enter a day of a week to analyze or "all" to apply no day filter: ')
    day = day.lower()
    while True:
        if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            break
        else:
            day = input("\nSorry, your input should be: 'sunday','monday','tuesday','wednesday','thursday','friday','saturday' or all: ")
    print('-'*40)
    return city, month, day

#----------------------------------------------------------------------------------------------------------------------------------------
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the Start Time column to datetime
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 #use the index of the months list to get the corresponding int in the csv file
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df

#----------------------------------------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
    # display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)
    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Start Hour:', common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#----------------------------------------------------------------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    start_time = time.time()
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)
    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station'])
    frequent_combination_station = combination.size().sort_values(ascending=False).head(1) # to display only the first row
    print('\nMost frequent combination of Start Station and End Station trip:\n', frequent_combination_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#----------------------------------------------------------------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#----------------------------------------------------------------------------------------------------------------------------------------
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    start_time = time.time()
    # Display counts of user types
    print('User Type Statistics:')
    print(df['User Type'].value_counts())
    if city != 'washington': #only for new york city and chicago
        # Display counts of gender
        print('\nGender Statistics:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:',earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#----------------------------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
