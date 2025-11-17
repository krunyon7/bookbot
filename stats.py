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