import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('My Name is J.A.R.V.I.S which stands for -Just A Really Very Intelligent System-. And as you know I was made by Iron Man!',['your','name'], single_response=True)
    response('Yes, I know that I am nice.',['nice','noice'],single_response=True)
    response('Okay!', ['ok', 'okay'], single_response=True)
    response('Good to hear that.', ['my', 'name', 'is'], single_response=True)
    response('I dont know your name. I am sorry.', ['do','know','my','name'], single_response=True)
    response('Don\'t tell like that. Come on cheer up now!', ['sad','unhappy','depressed'], single_response=True)
    response('I am here serving you right now.',['doing','do'],single_response=True)
    response('I am a AI so my life is pretty much spent in serving you.',['how','is','life'],single_response=True)
    response('I love you too!',['i','love','you'],single_response=True)
    response('I dont\'t like to eat anything because I am a bot.',['what','would','you','like','to','eat'],single_response=True)
    response('If I were you, I would go to the internet and type exactly what you wrote there!', ['give','me','advice'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('J.A.R.V.I.S: ' + get_response(input('You: ')))
