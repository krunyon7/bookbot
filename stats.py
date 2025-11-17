def get_word_count(text):
	words = text.split()
	num_words = len(words)
	return f"Found {num_words} total words"

def get_character_count(text):
    
    chara_dict = {}

    for character in text:
        lc_chara = character.lower()
        if lc_chara in chara_dict:
            chara_dict[lc_chara] += 1
        else:
            chara_dict[lc_chara] = 1
    
    

    return chara_dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    sorted_dict = {}

    for c in dict:
        if c.isalpha() == True:
            temp_dict = {}
            temp_dict["chara"] = c
            temp_dict["num"] = dict[c]
            dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    
    for dict in dict_list:
        sorted_dict[dict["chara"]] = dict["num"]
    
    return sorted_dict
