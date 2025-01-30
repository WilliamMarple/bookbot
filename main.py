def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    book_report = get_book_report(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print(book_report) 

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_dict(text):
    chars = {}
    for char in text:
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

def get_book_report(char_dict):
    report = ""
    for key in sorted(char_dict):
        if key.isalpha() == True:
            report += f"The '{key}' character was found {char_dict[key]} times\n"
    return report

main()