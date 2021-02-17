Data-Exploration-Using-Python-(Pandas-Numpy-Time) On-US-Bikeshare-Data
Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics

# Project Overview:
This project relies on the use of pandas library and simple statistical techniques to conduct a rudimentary analysis on bike share data from three major U.S. cities-Chicago, Washington, and New York City-to view details such as the most popular days or the most common stations.

# How To run:
You can input 'python bikeshare_2.py' on your gitbash terminal to run this program.

#Program Details:
The program takes user input for the city (e.g. Chicago or 1), 
month for which the user wants to view data (e.g. January; also includes an 'all' option to apply no month filter) and day for which the user wants to view data (e.g. Monday; also includes an 'all' to apply no day filter).

Upon receiving the user input the program prints the following details:

Most popular month 
Most popular day 
Most popular hour 
Most popular start station 
Most popular end station 
Most popular combination of start and end stations 
Total trip duration 
Average trip duration 
Types of users by number 
Types of users by gender (does not include washington) 
The oldest user (does not include washington) 
The youngest user (does not include washington) 
The most common birth year amongst users (does not include washington)

# Requirements:
Language: Python 3.6 or above Libraries: pandas, numpy, time

# Project Data:
chicago.csv - Stored in the Dataset folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.

# Built with:
Python 3.6.6 - The language used to develop this. 
Pandas - One of the libraries used in this project. 
Numpy - One of the libraries used in this project. 
Time - One of the libraries used in this project.

# Author:
Ahmed Soliman - Mentioned all the help received in 'Acknowledgements' section.

# Acknowledgements:
Numpy docs - Numpy documentation was very helpful in understanding the implemention of Numpy methods that I used in this project. 
Pandas docs - Pandas documentation was very helpful in understanding the implemention of Pandas methods that I used in this project. 
Udacity - Udacity's Data Analyst Nanodegree program and their instructors were extremely helpful.
