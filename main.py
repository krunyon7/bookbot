import sys

def get_book_text(path_to_file):
	file_contents = ""
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

from stats import get_word_count, get_character_count, sort_dict


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	chara_dict = get_character_count(text)
	sorted = sort_dict(chara_dict)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(get_word_count(text))
	print("--------- Character Count -------")
	for key in sorted:
		print(f"{key}: {sorted[key]}")
	print("============= END ===============")

	

main()
