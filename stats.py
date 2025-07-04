def word_count(text):
    word_count = 0
    for each in text.split():
        word_count +=1
    return word_count

def repeat_char(text):
    # all_the_chars = list(text.lower())
    # print(all_the_chars)
    indvidual_char = list(text.lower())
    char_count = dict.fromkeys(list(text.lower()), 0)
    # print(indvidual_char)
    for each in indvidual_char:
    #    char_count[each] +=1
        char_count[each] +=1
    return char_count
            
def sorted_list(text):
    char_count = repeat_char(text)
    # print (char_count)
    # list_of_dicts = []
    temp_dict = {}
    for key, value in char_count:
        print(key, value)
        temp_dict[key] = value
    return list(temp_dict)