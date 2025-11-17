def get_book_text(path_to_file):
	file_contents = ""
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

from stats import get_word_count
from stats import get_character_count

def main():
	chara_dict = get_character_count(get_book_text("books/frankenstein.txt"))
	print(get_word_count(get_book_text("books/frankenstein.txt")))
	print(chara_dict)

main()
