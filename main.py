def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(word_count(file_contents))
        # print(char_count(file_contents))
        for char in char_count(file_contents):
            print(f"The '{char["char"]}' character was found {char["num"]} times")

def word_count(text):
    word_list = text.split()
    return len(word_list)

def sort_on(dict):
    return dict["num"]

def char_count(text):
    char_map = {}
    char_list = []
    for char in text.lower():
        if char.isalpha():
            if (char not in char_map):
                char_map[char] = 0
            char_map[char] += 1
    
    for char in char_map:
        char_list.append({"char":char, "num":char_map[char]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()
