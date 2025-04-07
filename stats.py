def get_word_count(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter

def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    char_count = dict()
    for word in words:
        characters = list(word)
        for char in characters:
            character_lower = char.lower()
            if character_lower in char_count:
                char_count[character_lower] += 1
            else:
                char_count[character_lower] = 1
    return char_count

def sort_on(item):
    # Extract the count value from the dictionary
    return list(item.values())[0]


def get_sorted_char_count(char_count):
    sorted_char = []
    for key in char_count:
        sorted_char.append({key: char_count[key]})
    sorted_char.sort(reverse=True, key=sort_on)  # Ensure sort_on is defined

    for pair in sorted_char:
        for char, count in pair.items():
            if char.isalpha():
                print(f"{char}: {count}")

