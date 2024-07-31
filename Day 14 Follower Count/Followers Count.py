data = [{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}, {
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer',
    'country': 'Portugal'
}, {
    'name': 'Ariana Grande',
    'follower_count': 183,
    'description': 'Musician and actress',
    'country': 'United States'
}, {
    'name': 'Dwayne Johnson',
    'follower_count': 181,
    'description': 'Actor and professional wrestler',
    'country': 'United States'
}]


def checkfollowercount(two_people_dict):
    if two_people_dict[0]['follower_count'] > two_people_dict[1][
            'follower_count']:
        correctpersonname = two_people_dict[0]['name'].lower()
    elif two_people_dict[0]['follower_count'] < two_people_dict[1][
            'follower_count']:
        correctpersonname = two_people_dict[1]['name'].lower()
    else:
        correctpersonname = "-1"  # I wrote this for the case wthen the both followers count is equal
    return correctpersonname


import random

flag = True
sum = 0
while flag:
    two_people = random.sample(data, 2)
    print(two_people[0]['name'])
    print(two_people[1]['name'])
    storename = checkfollowercount(two_people)
    print("enter the name in lower case plese dont enter other names")
    userinput = input("enter the name of the highest number of people:->")

    if (userinput == storename):
        print("you won a point")
        sum = sum + 1
    else:
        flag = False
print(sum)
