import sys
count = len(sys.argv)
if(count != 2):
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path):
	with open(path) as f:
		# f is a file object
		file_contents = f.read()
		return file_contents


from stats import get_word_count
from stats import get_characters
from stats import sort_on
from stats import dict_sort



count = get_word_count(sys.argv[1])
text = get_book_text(sys.argv[1])
dictionary = get_characters(text)
letlist = dict_sort(dictionary)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
# print(letlist)
for l in letlist:
	if(l["char"].isalpha()):
		print(f"{l["char"]}: {l["num"]}")
print("============= END ===============")
