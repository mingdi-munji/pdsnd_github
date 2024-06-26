# -*- coding: utf-8 -*-
"""US Bikeshare Project 2 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wt8sZOo2rBF82TuYzZCTL54kAF5F-qTL
"""

import time
import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

"""CITY_DATA, MONTHS, DAYS
CITY_DATA: A dictionary that stores data file names for three cities. Each city name is a key, and the name of the CSV file is a value.

MONTHS: A list of months that can be analyzed. The 'all' option covers all months.
DAYS: A list of days you can analyze. The 'All' option covers all days of the week.
"""

CITY_DATA = {
    'chicago': '/content/drive/My Drive/chicago.csv',
    'new york city': '/content/drive/My Drive/new_york_city.csv',
    'washington': '/content/drive/My Drive/washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august','september','october','november','december','all']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

"""get_filters()
Enter the city, month, and day of the week from the user to set the filter for the data to be analyzed.
The values entered are converted to lowercase or title cases and processed in the correct format.
To prevent incorrect input, use the while loop to repeat the request until the user enters a valid value.
"""

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city >>> (Chicago, New York City or Washington): ").lower()
    while city not in CITY_DATA:
        print("Please try again, name not recognized")
        city = input("Please choose a city >>> (Chicago, New York City or Washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please choose a month >>> (January, February, March, April, May, June or All): ").lower()
    while month not in MONTHS:
        print("Please try again, month not recognized")
        month = input("Please choose a month >>> (January, February, March, April, May, June or All): ").lower()

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose a Day >>> (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All): ").title()
    while day not in DAYS:
        print("Please try again, day not recognized")
        day = input("Please choose a day >>> (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All): ").title()

    print('-'*40)
    return city, month, day

"""[Data loading and preprocessing]
load_data(city, month, day)

Reads the data from the selected city from a CSV file and converts it into a Pandas data frame.
Clean up the data and add new columns (for example, Monday and Day).
Filters data according to the month and day of the week selected by the user.
"""

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
    #Read and load in as df to return df / use CITY DATA
    df = pd.read_csv(CITY_DATA[city])

    # Clean Data
    df.drop(columns='Unnamed: 0', inplace=True)

    #Missing values
    df.fillna(method='ffill', inplace=True)

    # Change data types
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert 'End Time' column to datetime.
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month from 'Start Time' column to create 'Month' column.
    df['Month'] = df['Start Time'].dt.month

    # extract day from 'Start Time' column to create 'Day' column.
    df['Day'] = df['Start Time'].dt.day_name()

    # filter by month
    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['Month'] == month_index]

    # Filter by day
    if day != 'All':
        df = df[df['Day'] == day]

    return df

"""
statistical analysis functions
time_stats(df, month, day)
Calculate the most common travel month, day, and time.
# Formatted as code
"""

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # # TO DO: display the most common month
    if month == 'all':

        print('The most common month is: ', MONTHS[df['Month'].mode()[0] - 1].title() )
    else:

        print('The most common month is: ', month.title())

    # TO DO: display the most common day of week
    if day == 'All':

        print('The most common day is: ', df['Day'].mode()[0])
    else:

        print('The most common day is: ', day)


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    print('The Most Common Start Hour is: ', df['Start Hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""station_stats(df)
Calculate the most popular departure and arrival stations, and travel routes.
The data frame provides statistics on the popular departure, arrival, and travel routes of the bike-sharing service. This allows users to better understand the service's usage patterns.
trip_duration_stats(df)

Calculate the total travel time and the average travel time.
It functions to calculate the total time and average time of the trip from the bike-sharing data. This function takes the Pandas data frame df as input and calculates statistics related to the travel time from that data frame

user_stats(df)
Provides statistics on user type, gender, and year of birth. It is responsible for calculating and outputting user-related statistics from bike-sharing data. The function takes the pandas data frame df as input, and calculates various user statistics from that data frame.

raw_data(df)
If the user wants it, it displays 5 raw rows of data. It functions to show part of the raw data in the data frame df. This function asks the user if they want to see the raw data, and outputs part of the data frame when they answer 'yes'. Repeat this process until the user no longer wants to see the data
"""

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Commonly used Start Station is: ' , df['Start Station'].mode()[0])

     # TO DO: display most commonly used end station
    print('The Most Commonly used End Station is: ' , df['End Station'].mode()[0])

   # TO DO: display most frequent combination of start station and end station
    df['journey'] = df['Start Station'] + " to " + df['End Station']
    print('The Most Frequent Trip from: ', df['journey'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time / sum = total
    print('The Total Travel Time is: ', df['Trip Duration'].sum(), "'sec")

    # TO DO: display mean travel time / mean = average
    print('The Mean Travel Time is: ', int(df['Trip Duration'].mean()), "'sec")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender is available:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' data in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth / earliest = min, recent = max, common = mode
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year data in this file.")

    print("\This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # Create index and increase by 5

    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            # print 5 lines
            print(df[i:i+5])

            # increase index by 5
            i = i+5

        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes to continue: ')
        if restart.lower() not in ['yes', 'y'] :
            break


if __name__ == "__main__":
	main()