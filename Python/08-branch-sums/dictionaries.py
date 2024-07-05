# dictionary practice

favorite_languages = {
    'jim': 'python',
    'susan': 'groovy',
    'jenna': 'ruby',
    'steve': 'java',
}

# print name and language
# print(favorite_languages['jim'])
# print(favorite_languages['susan'])

# looping through keys is default so you can leave `keys()` out if you want | title() capitalizes each word
for k in favorite_languages.keys():
    print(k)
    for v in favorite_languages.values():
        print(v)
    

# --------------------------------------------- #

data = {
    "nodes": [
        { "id": "1", "left": "2", "right": "3", "value": 1 },
        { "id": "2", "left": "4", "right": "5", "value": 2 },
        { "id": "3", "left": "6", "right": "7", "value": 3 },
        { "id": "4", "left": "8", "right": "9", "value": 4 },
        { "id": "5", "left": "10", "right": None, "value": 5 },
        { "id": "6", "left": None, "right": None, "value": 6 },
        { "id": "7", "left": None, "right": None, "value": 7 },
        { "id": "8", "left": None, "right": None, "value": 8 },
        { "id": "9", "left": None, "right": None, "value": 9 },
        { "id": "10", "left": None, "right": None, "value": 10 }
    ],
}


for d in data["nodes"]:
    print("A list of dictionary nodes:", d)
    print("\"nodes\" is a list of dictionaries", data)
