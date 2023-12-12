# 1
def reverse_tuple():
    tuple_list = tuple(input("Enter your tuple data : "))
    rev_tuple_list = tuple_list[::-1]
    print(rev_tuple_list)

    return rev_tuple_list


# 2
def remove_duplicates_in_tuple():
    unique_tuple_list = set(tuple(input("Enter your tuple data : ")))
    print(unique_tuple_list)
    return unique_tuple_list


# 3
def check_symmetrical_and_palindrome(string_object):
    if (string_object == string_object[::-1]):
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

    print(string_object[0:int(len(string_object) / 2)])

    if string_object[0:int(len(string_object) / 2)] == string_object[int(len(string_object) / 2): len(string_object)]:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")


# 4
def print_the_even_length_string_in_sentence(sentence):
    sentence_words = [word for word in sentence.split() if len(word) % 2 == 0]

    str1 = ' '.join(sentence_words)

    print(str1)


# 5
def order_the_dictionary_by_key():
    d = {2: '56', 1: '2', 4: '12', 5: '24', 6: '18', 3: '323'}

    print(dict(sorted(d.items())))

    pass


# 6
def sum_of_list(list1):
    # num = 0
    # list1 = [(num = num+i) for i in list1]
    print(sum(list1))
    return sum(list1)


# 7
def reverse_string(str_obj):
    print(str_obj)
    rev_str = ''
    print(len(str_obj))
    for ch in range((len(str_obj) - 1), 0, -1):
        print(ch)
        print(str_obj[ch])
        rev_str = rev_str + str_obj[ch]

    print(rev_str)
    return rev_str


# 8
def find_max_and_min_number_in_array(list1):
    return "minimum number is : " + str(min(list1)) + ", And Maximum number is : " + str(max(list1))


# 9
def check_common_element_in_given_two_lists(list1, list2):
    s3 = set(list1).intersection(set(list2))
    return True if len(s3) > 0 else False


# 10
def pattern_check_reverse_string(pat, str_obj):
    check_pat = ''
    for char in pat:
        for cha in  str_obj:
            if cha in char:
                check_pat = check_pat + char

    check_pat_rev = check_pat[::-1]
    # print(check_pat_rev)

    return check_pat_rev


#11
def flash_card():
    class Flashcard:
        def __init__(self, word, meaning):
            self.word = word
            self.meaning = meaning

        def __str__(self):
            return f"Word: {self.word}\nMeaning: {self.meaning}"

    # Create an empty list to store flashcards
    flashcards = []

    # Use a while loop to take input and store flashcards
    while True:
        word_input = input("Enter a word (or 'exit' to stop): ")

        # Check if the user wants to exit
        if word_input.lower() == 'exit':
            break

        meaning_input = input("Enter the meaning: ")

        # Create a new flashcard object and add it to the list
        new_flashcard = Flashcard(word_input, meaning_input)
        flashcards.append(new_flashcard)

    # Use a while loop to print all the stored flashcards
    for flashcard in flashcards:
        print("\n", flashcard)

#12
def deck_of_cards():
    import random

    # Declare global variables for suits and values
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    class Cards:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value

        def __str__(self):
            return f"{self.value} of {self.suit}"

    # Function to create a deck of cards
    def create_deck():
        deck = []
        for suit in suits:
            for value in values:
                card = Cards(suit, value)
                deck.append(card)
        return deck

    # Function to shuffle the deck
    def shuffle_deck(deck):
        random.shuffle(deck)

    # Create a deck of cards
    deck_of_cards = create_deck()

    # Print the original deck
    print("Original Deck:")
    for card in deck_of_cards:
        print(card)

    # Shuffle the deck
    shuffle_deck(deck_of_cards)

    # Print the shuffled deck
    print("\nShuffled Deck:")
    for card in deck_of_cards:
        print(card)


if __name__ == "__main__":
    # reverse_tuple()
    # remove_duplicates_in_tuple()
    # check_symmetrical_and_palindrome("amama")
    # print_the_even_length_string_in_sentence("This is a python language")
    order_the_dictionary_by_key()
    # sum_of_list([1,22,33,4])
    # reverse_string("Hello World!")
    # print(find_max_and_min_number_in_array([1,22,33,4]))
    # print(check_common_element_in_given_two_lists([1,2,3],[1,4,5]))
    # print(pattern_check_reverse_string("asbcklfdmegnot", "eksge"))
    # flash_card()
    # deck_of_cards()
    pass
