def sort_by(items):
    return items["num"]

def get_num_words(text):
    return len(text.split())

def get_char_count(text):

    # create dictionary for results
    char_counts = {}

    # loop through characters of text
    for x in text:
        
        # convert all characters to lower case
        x = x.lower()
    
        # add counts of characters to dictionary
        if x not in char_counts:
            char_counts.update({x: 1})
        else:
            char_counts[x] += 1

    char_count_list = []
    for item in char_counts:
        if item.isalpha():
            char_count_list.append({"char": item, "num": char_counts[item]})
        else:
            continue

    char_count_list.sort(key=sort_by, reverse=True)
    
    return char_count_list