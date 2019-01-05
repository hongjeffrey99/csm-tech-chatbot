import time
import csv
import sys

def jokeDeliver(prompt, punchline):
    print(prompt)
    time.sleep(2)
    print(punchline)

def userInput():
    while True:
        read = input()
        if read == "next":
            return True
        elif read == "quit":
            return False
        else:
            print("I don't understand")

def csvRead(file):
    jokes = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            div = row.split(',')
            jokes += div
    return jokes

# Reads command line argument in format 'python jokebot.py jokes.csv'
if __name__ == '__main__':
    # Checks if a CSV filename is given
    if not sys.argv[1] or sys.argv[1].endswith('.csv'):
        print("No joke file given")
        quit()
    # Else deliver prompt and punchline, then await userinput
    # First joke is delivered without user input
    jokes = csvRead(sys.argv[1])
    jokeDeliver(jokes[0][0], jokes[0][1])
    # If user input is verified and while there are still jokes, deliver
    i = 1
    while userInput() or i == len(jokes):
        jokeDeliver(jokes[i][0], jokes[i][1])
    quit()