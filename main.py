
from stats import word_count, repeat_char, sorted_list
def get_book_text(file_path_input):
    with open(file_path_input) as f:
        file_contents = f.read()
    # return file_contents
   
    return file_contents
    
    
# def word_count(text):
#     word_count = 0
#     for each in text.split():
#         word_count +=1
#     return word_count

def main():
    book_path = "/home/fedora/bootdev/bookbot/books/frankenstein.txt"
    # get_book_text(book_path)
    # print(f"{word_count(get_book_text(book_path))} words found in the document")
    # print(repeat_char(get_book_text(book_path)))
    print(sorted_list(get_book_text(book_path)))
    
if __name__ == "__main__":
    main()
    
    
    
# def get_book_text(file_path_input):
#     with open(file_path_input) as f:
#         file_contents = f.read()
#     # return file_contents
#     return word_count(file_contents)
    
# def word_count(text):
#     word_count = 0
#     for i in range(text.spilt()):
#         word_count = word_count +1
#     return word_count
    
# # path_to_file = input("Eter book file path")

# def main():
#     book_path = "/home/fedora/bootdev/bookbot/books/frankenstein.txt"
#     print(get_book_text(book_path))
#     # return get_book_text(book_path)
    
# if __name__ == "__main__":
#     main()