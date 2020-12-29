import json
from difflib import SequenceMatcher,get_close_matches

with open('CLI_Dictionary\data.json') as f:
  data = json.load(f)

def getCloseMatch(userKey):
    return get_close_matches(userKey,data.keys(),cutoff=0.8)

def getValue(userKey):
    closeMatches = getCloseMatch(userKey)
    result = data.get(closeMatches[0])

    if userKey in data:
        print(data.get(userKey))
    elif len(closeMatches) > 0:
        choice = input("Did you mean '{0}'?, If yes press 'y' else 'n'".format(closeMatches[0]))
        if choice == "y": print(str(result))
        else: print("Sorry the word you searching for may be incorrect, please check")


userKey = input("Enter the string to search in the dictionary: \n")
getValue(userKey)

