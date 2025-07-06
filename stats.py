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
    sorted_char_count = dict(sorted(char_count.items(), key = lambda item: item[1], reverse=True))
    # print(sorted_char_count)

    # list_of_dicts = []
    # temp_dict = {}
    for key, value in sorted_char_count.items():
        print(f"{key}: {value}")
    #     temp_dict[key] = value
        
    #     # print(temp_dict)
    #     list_of_dicts.append(temp_dict.copy())
    #     del temp_dict[key]
    # # return list(list_of_dicts)