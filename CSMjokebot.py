import time
import csv
import sys
import requests
import json

# Sleep two seconds between printing prompt and punchline of a joke
def jokeDeliver(prompt, punchline):
    print(prompt)
    time.sleep(2)
    print(punchline)

# Read userinput for next joke or quitting
def userInput():
    while True:
        read = input()
        if read == "next":
            return True
        elif read == "quit":
            return False
        else:
            print("I don't understand")

# Read csv file formats of prompt,punchline
def csvRead(file):
    jokes = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            jokes += row
    return jokes

# Get and filter reddit dadjokes
def pullJokes():
    # Get JSON and format it
    jokesDict = requests.get('https://www.reddit.com/r/dadjokes.json', headers = {'User-agent': 'bot'}).json()

    jokes = []
    # Check title and over_18 for each tagged post on the page
    for tag in jokesDict['data']['children']:
        headers = tag['data']
        #print(tag['data']['title'])
        if not headers['over_18'] 
            and (headers['title'].startswith('Why') or headers['title'].startswith('What') or headers['title'].startswith('How')):
            jokes += [headers['title'], headers['selftext']]
    return jokes

# Read command line argument in format 'python jokebot.py jokes.csv'
if __name__ == '__main__':
    # Check if a CSV filename is given, if not then get jokes from non-CSV source
    if len(sys.argv) == 1 or not sys.argv[1].endswith('.csv'):
        print("No joke file given")
        jokes = pullJokes()
    else:
        jokes = csvRead(sys.argv[1])
    # First joke is delivered without user input
    if not jokes:
        quit()
    jokeDeliver(jokes[0], jokes[1])
    # If user input is verified and while there are still jokes, deliver
    i = 2
    while userInput() and i + 1 < len(jokes):
        jokeDeliver(jokes[i], jokes[i + 1])
        i += 2
    quit()
