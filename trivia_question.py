##########################################################
# SI 106 Fall 2023 Coding Assessment Specification
# 
# Your Name: AJ deVaux
# Your Michigan Email: ajdv@umich.edu
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
import re               # regular expressions

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

def choose_json():
    path = os.path.dirname(os.path.abspath(__file__))
    game_files = os.listdir(f"{path}/game_config_files")
    rule_dict = {}
    for file in game_files:
        game_num = int(re.findall("(\d+)\.json", file)[0])
        rule_dict[game_num] = file
    sorted_rules = sorted(rule_dict.items())

    print("Rule Set Options:\n")
    for rule_set in sorted_rules:
        print(f"{rule_set[0]} - {rule_set[1]}")

    print()

    user_choice = input("Please choose a rule set to use by inputting the number in front of it. ")
        
    try:
        if int(user_choice) > 0 and int(user_choice) < 12:
            print(f"Great!  You chose rule set {user_choice}.")
            return rule_dict[int(user_choice)]
        else:
            print(f"Error, {user_choice} is invalid.")
            return False
        
    except:
        print(f"Error, {user_choice} is invalid.")
        return False
    
    pass


def read_json(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    file = open(f"{path}/game_config_files/{filename}")
    data = json.load(file)

    return data


def rule_set_up(rules):
    round_num = rules["num_rounds"]
    cats = rules["potential_categories"]
    diff = rules["game_difficulty"]
    summary_file = rules["game_summary_filename"]

    # print(round_num, cats, diff, summary_file)
    try:
        if int(round_num) > 0 and int(round_num) < 16:
            print("Valid number of rounds.")
            pass
        else:
            print("Invalid number of rounds, setting it to 2 by default.")
            round_num = 2
    except:
        print("Invalid number of rounds, setting it to 2 by default.")
        round_num = 2

    # print(round_num)

    try:
        if len(cats) != 0:
            print("Valid selection of categories.")
            pass
        else:
            print("Invalid selection of categories, setting it to ['Art', 'Animals','Vehicles'] by default.")
            cats = ["Art", "Animals","Vehicles"]
    except:
        print("Invalid selection of categories, setting it to ['Art', 'Animals','Vehicles'] by default.")
        cats = ["Art", "Animals","Vehicles"]

    # print(cats)

    try:
        diff = diff.lower().strip()
        if diff == 'easy' or diff == 'medium' or diff == 'hard':
            print("Valid game difficulty.")
            pass
        else:
            print("Invalid game difficulty, setting it to 'medium' by default.")
            diff = "medium"
    except:
        print("Invalid game difficulty, setting it to 'medium' by default.")
        diff = "medium"

    # print(diff)

    try:
        summary_file = summary_file.strip().lower()
        if summary_file[-4:] == ".csv":
            print("Valid file for writing game summary.")
            pass
        else:
            print("Invalid file for writing game summary, setting it to 'game_summary_default.csv' by default.")
            summary_file = "game_summary_default.csv"
    except:
        print("Invalid file for writing game summary, setting it to 'game_summary_default.csv' by default.")
        summary_file = "game_summary_default.csv"

    # print(summary_file)

    print("\n---The Game Rules Will be as Follows---\n")



        
        



def call_API():

    pass





def main():
    rule_file = choose_json()
    if rule_file == False:
        print("ending program")
        return None
    
    # print(rule_file)

    base_rules = read_json(rule_file)

    rule_set_up(base_rules)


    pass


main()



























