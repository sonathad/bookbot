def main():
    path = "books/frankenstein.txt"
    contents = get_contents(path)
    if contents is not None:
        words_counter = word_count(contents)
        chars_counter = char_count(contents)
        print_report(path, words_counter, chars_counter)

def print_report(path, words_counter, chars_counter):
    print(f"--- Begin report of {path} ---")
    print(f"{words_counter} words found in the document\n")

    # printing letter counts, ordered by frequency
    sorted_chars = sorted(list(chars_counter), key=lambda x: chars_counter[x], reverse=True)
    for char in sorted_chars:
        print(f"The '{char}' character was found {chars_counter[char]} times")
    
    print("--- End report ---")



def get_contents(path):
    contents = None
    with open(path) as f:
        try:
            contents = f.read()
        except FileNotFoundError as fe:
            print(f"The file {path} was not found. Error: {fe}")
        except Exception as e:
            print(f"error: {e}")

    return contents

def word_count(text):
    return len(text.split())

def char_count(text):
    chars = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            chars[lower_char] = chars.setdefault(lower_char, 0) + 1
    
    return chars

if __name__ == "__main__":
    main()