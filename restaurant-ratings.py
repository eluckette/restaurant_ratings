# your code goes here
restaurant_dict = {}


def print_current_list(filename):
    with open(filename, 'rw') as score_file: 
        for line in score_file:
            restaurant_info = line.rstrip().split(':')
            restaurant_name, restaurant_rating = restaurant_info
            restaurant_dict[restaurant_name] = restaurant_rating

    for name in sorted(restaurant_dict):
        print "Restaurant %s is rated at %s." % (name, restaurant_dict[name])

    user_input = raw_input("Would you like to add a new rating? (Y/N) ").upper()

    if user_input == 'Y':
        ask_for_rating('scores.txt')

def ask_for_rating(filename):
    restaurant_name = raw_input("Which restaurant would you like to add? ")
    restaurant_rating = raw_input("Please give it a rating from 1 (worst) to 5 (best). ")

    with open(filename, 'a') as score_file:
        score_file.write('\n' + restaurant_name + ':' + restaurant_rating)
    
    print_current_list(filename)

print_current_list('scores.txt')



