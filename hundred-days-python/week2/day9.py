# Dictionaries and nesting

# # DICTIONARIES
# # {key: value}
# car = {
#     'dom': 'mazda 3',
#     'mom': 'nissan murano'
#     }
# # to access the value you need to print the specific key associated with it
# print(car['dom'])

# # adding items to a dictionary
# # dictionary_name[new_key] = 'new value'
# car['want_car'] = 'New Jeep Wrangler'
# print(car)

# # # wipe an existing dictionary
# # car = {}
# # print(car)

# # edit an item in a dictionary
# car['want_car'] = 'New BMW'
# print(car['want_car'])
# # if the key you are trying to edit does not exist it will just create a new key and value

# # looping through a dictionary
# for key in car:
#     # this will print all of the keys only
#     print(key)
#     # then this will print the values for those keys
#     print(car[key])


# Coding challenge 1 (Grading Program)

# # create a dictionary with scores then using a second dictionary convert those scores into grades
# student_scores = {
#     'Harry': 81,
#     'Ron': 78,
#     'Herminoe': 99,
#     'Draco': 74,
#     'Neville': 62
# }
# print(student_scores)
# # create the empty dictionary
# student_grades = {}

# # create a for loop that will loop through all of the scores
# for score in student_scores:
#     # create an if conditional to evaluate the scores
#     if student_scores[score] >= 91:
#         student_grades[score] = 'Outstanding'
#     elif student_scores[score] >= 81:
#         student_grades[score] = 'Exceeds Expectations'
#     elif student_scores[score] >= 71:
#         student_grades[score] = 'Acceptable'
#     else:
#         student_grades[score] = 'FAIL!'

# print(student_grades)


# # NESTING DICTIONARIES AND LISTS

# # test = {
# #     key1: [list],
# #     key2: {dictionary}
# # }

# capitals = {
#     'Japan': 'Tokyo',
#     'Korea': 'Seoul',
#     'China': 'Bejing',
# }

# travel_log = {
#     'Japan': ['Tokyo', 'Yokohama', 'Chiba'],
#     'Korea': ['Seoul', 'Paju', 'Busan', 'Daegu']
# }

# print(capitals)
# print(travel_log)
# print(travel_log['Japan'])

# # nesting a dictionary inside of a dictionary
# travel_log = {
#     'Japan': {
#         'cities_visited': ['Tokyo', 'Yokohama', 'Chiba'],
#         'cities_lived': ['Tokyo', 'Chiba']
#         },
#     'Korea': {
#         'cities_visited': ['Seoul', 'Paju', 'Busan', 'Daegu'],
#         'cities_lived': ['Seoul']
#         }
# }

# # print everything in the dictionary
# print(travel_log)
# # print one key in the dictionary
# print(travel_log['Korea'])
# # printing the list nested within two dicionaries
# print(travel_log['Korea']['cities_lived'][0])


# # you can also nest dictionaries inside of lists
# travel_log_list = [
#     {
#         'Country': 'Japan',
#         'cities_visited': ['Tokyo', 'Chiba', 'Yokohama'],
#         'years_lived': 1.5
#     },
#     {
#         'Country': 'Korea',
#         'cities_visited': ['Seoul', 'Busan', 'Paju', 'Daegu'],
#         'years_lived': 3.5
#     }
# ]

# print(travel_log_list)


# # Coding challenge 2 (Travel Log)

# # given a list that has a dict containg info on countries visited created a function that will allow you to add data augmenting the dictionary

# travel_log = [
#     {
#         'country': 'Japan',
#         'years_lived': 1.5,
#         'cities_visited': ['Tokyo', 'Yokohama', 'Chiba']
#     },
#     {
#         'country': 'Korea',
#         'years_lived': 3.5,
#         'cities_visited': ['Seoul', 'Busan', 'Paju', 'Daegu']
#     }
# ]

# print(travel_log)

# # create a function allowing you to add a new entry in the dictionary

# def add_new_country(country, years_lived, cities_visited):
#     # first need to access the first list that contains the dictionaries
#     travel_log.append(
#         {
#             'country': country,
#             'years_lived': years_lived,
#             'cities_visited': cities_visited
#         }
#     )

# # add info using new parameters
# add_new_country('Thailand', 0, ['Bangcock'])
# print(travel_log)


# DAY 9 PROJECT (SILENT AUCTION)

# import the logo and then print it to start the program
import silent_auction_logo_module as sal
print(sal.logo)

# opening message
print('Welcome to the Silent Auction I hope everyone is ready to bid!')

# create dictionary that will be used to store all of the bids with name as key and bid as value
bids = {}
# create a variable to allow a while loop
bidding_finished = False

# a function to compare bids and bidders
def find_highest_bidder(bidding_record):
    # a variable to find highest bid
    highest_bid = 0
    # empty string to hold the winner with highest bid
    winner = ''

    # for loop going through dictionary
    for bidder in bidding_record:
        # set bid_amount to bidding_record[bidder] key[value]
        # print(bidding_record)
        bid_amount = bidding_record[bidder]
        # check the new bid_amount against the highest_bid 
        if bid_amount > highest_bid:
            # highest_bid will change depending on what the highest integer is
            highest_bid = bid_amount
            # bidder goes through each dictionary 
            winner = bidder
    print(f'The winner is {winner} and the winning bid was ${highest_bid}')

# a while loop that keeps this going until the auction is over
while not bidding_finished:
    # input for the users name
    name = input('What is your name?\n')
    # input for the users bid
    price = int(input('What is your bid?\n'))
    # sets the key in 'bids' as NAME and the 'value' as PRICE
    bids[name] = price
    # will change the should_continue to True and end the while loop
    should_continue = input('Are their any other bidders? Y or N\n')
    if should_continue == 'N':
        bidding_finished = True
        # call the function and pass in the 'bids' dictionary
        find_highest_bidder(bids)