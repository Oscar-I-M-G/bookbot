def get_num_words(file_data) -> int:
    count = -1
    words = file_data.split()
    count = len(words)
    return count

def get_char_count(file_data) -> dict:
    count = dict()
    for char in file_data:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(item):
    return item["num"]

def get_sorted_char_count(char_dict) -> list:
    sorted_list = []
    for key,value in char_dict.items():
        sorted_list.append({"char" : key , "num" : value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
