##########################################################
# SI 106 Fall 2023 Coding Assessment Specification
# 
# Your Name: 
# Your Michigan Email: 
# 
# API Documentation: https://opentdb.com/api_config.php
##########################################################


# Here are some import statements I found helpful:
# You do not need to use any of these and you can add/delete as many as you'd like
import os               # checking if the config file exists
import json             # handling JSON files and API responses
import requests         # making API requests
import random           # randomly choosing incorrect answers and shuffling the answer list
import csv              # writing CSV files

#########

# The API responses sometimes have URL encoded characters in the text.

# Completely optional, but if you want to get rid of these characters in your output, 
# you should use the following code to extract data from the API response:

# import html 
# resp_data = json.loads(html.unescape(resp.text))

# This is instead of simply using something like:
# resp_data = resp.json() 
# or
# resp_data = json.loads(resp.text)

#########



##### IMPORTANT #####

# When you are specifying the category parameter in your API requests, you can't provide
# the name of the category, instead you need to use the API's corresponding category number.

# For example, if the user wants a question from the "Sports" category, you can't say
# "category=Sports" in your API request. Instead, you need to say something like
# "category=21" because the Sports category's number is 21 according to the map below.

# You should use the following dictionary to take the category that your user selects
# in each round and find the corresponding API category number to use in your API request.

api_category_map = {
        "Any Category": "any",
        "General Knowledge": "9",
        "Entertainment: Books": "10",
        "Entertainment: Film": "11",
        "Entertainment: Music": "12",
        "Entertainment: Musicals & Theatres": "13",
        "Entertainment: Television": "14",
        "Entertainment: Video Games": "15",
        "Entertainment: Board Games": "16",
        "Science & Nature": "17",
        "Science: Computers": "18",
        "Science: Mathematics": "19",
        "Mythology": "20",
        "Sports": "21",
        "Geography": "22",
        "History": "23",
        "Politics": "24",
        "Art": "25",
        "Celebrities": "26",
        "Animals": "27",
        "Vehicles": "28",
        "Entertainment: Comics": "29",
        "Science: Gadgets": "30",
        "Entertainment: Japanese Anime & Manga": "31",
        "Entertainment: Cartoon & Animations": "32",
    }


### YOUR CODE BELOW ###



























