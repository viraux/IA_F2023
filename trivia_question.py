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
import html             #converts html characters

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
    # Find the current file path and go into the game_config_files folder
    path = os.path.dirname(os.path.abspath(__file__))
    game_files = os.listdir(f"{path}/game_config_files")
    rule_dict = {}

    # Go through each file and create a key value pair of the config numbers and the file name to a dictionary
    for file in game_files:
        game_num = int(re.findall("(\d+)\.json", file)[0])
        rule_dict[game_num] = file


    # Print each config number and file name in numerical order for the user to see, 
    # then ask for them to choose a file using its number.
    sorted_rules = sorted(rule_dict.items())
    print("Rule Set Options:\n")
    for rule_set in sorted_rules:
        print(f"{rule_set[0]} - {rule_set[1]}")

    print()

    user_choice = input("Please choose a rule set to use by inputting the number in front of it. ")
        
    # Testing if the number is valid, if it is return it.  Otherwise return false.
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
        round_num = int(round_num)
        if round_num > 0 and round_num < 16:
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

    print(f"Number of Rounds: {round_num}\n")

    print(f"Possible Categories: {cats}\n")
    
    print(f"Difficulty: {diff}\n")
    
    print(f"Summary File: {summary_file}\n")

    print("-----------------------------------------")

    return round_num,cats,diff,summary_file


def start_game(rounds,cats,diff,filename,score):
    # print(rounds,cats,diff,filename)
    # print(cats)

    cats.sort()

    # print(cats)

    headings = ['round_number','question_category','question_difficulty','question_text','user_answer','correct_answer','correct','unscaled_points_earned']

    f = open(f"game_summary_files/{filename}","w")

    data_writer = csv.writer(f)

    data_writer.writerow(headings)

    for i in range(rounds):
        i += 1
        print(f"\n---Round Number {i}---\n")
        
        # print(i)
        
        print("Category Options:")
        for j in range(len(cats)):
            print(f"{j+1}. {cats[j]}")

        user_cat = input("\nPlease type the number associated with your preferred category. ").strip()

        # Adding in check of user input - added feature
        while True:
            try:
                user_cat = int(user_cat)
                if user_cat in list(range(1,len(cats)+1)):
                    cat_name = cats[user_cat-1]
                    print(f"\nGreat! This rounds category is {cat_name}.\n")
                    break
                else:
                    user_cat = input("Invalid response, please type the number associated with your preferred category only. ")
            except:
                user_cat = input("Invalid response, please type the number associated with your preferred category only. ")
        
        # print("out")

        print("""Question Difficult Options: \n-> Easy \n-> Medium \n-> Hard""")

        user_diff = input("Please choose the question difficulty you would like from the options above. ").lower().strip()

        if user_diff == 'easy' or user_diff == 'medium' or user_diff == 'hard':
            print(f"\nWonderful!  Fetching a {user_diff} difficulty question in the {user_cat} category")
        else:
            user_diff = "medium"
            print(f"\nSorry, invalid response!  Fetching a {user_diff} difficulty question in the {cat_name} category default")

        score, data = call_API(cat_name,user_diff,i,score)

        data_writer.writerow(data)

        interrupt = input(f"Round {i} is now over, type anything to continue. ")


    print("\n-----------------------------------------")

    print("Thank you for playing my Trivia Game!\n")

    if diff == "medium":
        weighted_score = score*2
        print("\nDoubling your score because the difficulty was medium.")
        pass
    elif diff == "hard":
        print("\nTripling your score because the difficulty was medium.")
        weighted_score = score*3
        pass
    else:
        weighted_score = score
        print("\nSorry, no score multiplier because the difficulty was easy.")
        pass

    print(f"Your Unweighted Score: {score}")
    print(f"Your weighted Score: {weighted_score}\n")

    print(f"All your game data is saved in {filename}.  Check it out in the game_config_files folder!")

    print("\n-----------------------------------------")

    data_writer.writerow(f"Total Game Score (Unscaled): {score}")
                         
    data_writer.writerow(f"Total Game Score (Scaled): {weighted_score}")

    f.close()




    pass
        
        



def call_API(cat,diff,round,score):
    
    cat_id = api_category_map[cat]

    url = f"https://opentdb.com/api.php?amount=1&category={cat_id}&difficulty={diff}&type=multiple"

    # print(url)

    response = requests.get(url)

    # print(response.json())

    whole_data = response.json()

    data = whole_data["results"][0]

    question = html.unescape(data["question"])
    # print(question)
    correct = str(data["correct_answer"])
    incorrect = data["incorrect_answers"]

    answer_pool = [correct]

    input_bool = True

    if diff == "easy":
        rand_incorrect = incorrect.pop(random.randrange(0,len(incorrect)))
        # print(rand_incorrect)
        answer_pool.append(str(rand_incorrect))
        random.shuffle(answer_pool)
        print(f"\nEasy Question {round}: {question}\n")

        print("Possible Answers:")
        for answer in answer_pool:
            print(f"-> {answer}")

        user_answer = input("\nNow it's your turn, enter your answer! ").lower()

        if user_answer == correct.lower():
            score += 10
            print(f"\nCorrect! The answer was {correct}.  Adding 10 to your score; it is currently {score}")
        else:
            score -= 5
            print(f"\nIncorrect! The answer was {correct}.  Subtracting 5 from your score; it is currently {score}")
            input_bool = False
        
        pass
    elif diff == "medium":
        answer_pool += incorrect
        random.shuffle(answer_pool)
        print(f"\nMedium Question {round}: {question}\n")

        print("Possible Answers:")
        for answer in answer_pool:
            print(f"-> {answer}")

        user_answer = input("\nNow it's your turn, enter your answer! ")

        if user_answer == correct.lower():
            score += 20
            print(f"\nCorrect! The answer was {correct}.  Adding 20 to your score; it is currently {score}")
        else:
            score -= 10
            print(f"\nIncorrect! The answer was {correct}.  Subtracting 10 from your score; it is currently {score}")
            input_bool = False
        pass
    else:
        print(f"\nHard Question {round}: {question}\n")

        user_answer = input("\nNow it's your turn, enter your answer! ")

        if user_answer == correct.lower():
            score += 30
            print(f"\nCorrect! The answer was {correct}.  Adding 30 to your score; it is currently {score}")
        else:
            score -= 15
            print(f"\nIncorrect! The answer was {correct}.  Subtracting 15 from your score; it is currently {score}")
            input_bool = False
        pass


    data_content = [round,cat,diff,question,user_answer,correct,input_bool,score]

    return score, data_content






# Setting up main function to run file through
def main():
    score = 0

    # Calling function to find the rule file to use
    rule_file = choose_json()


    # If rule_file returns false, end program
    if rule_file == False:
        print("ending program")
        return None
    
    # print(rule_file)

    # Call function to establish base rules
    base_rules = read_json(rule_file)

    # Call function to set up final rules and displays them to user
    rounds,cats,diff,filename = rule_set_up(base_rules)

    # Call function to start game with finalized rules
    start_game(rounds,cats,diff,filename,score)


    pass


main()
