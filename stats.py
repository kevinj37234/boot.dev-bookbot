def get_word_count(path):
        with open(path) as f:
                text = f.read()
                wordlist = text.split()
                count = len(wordlist)
                return count

def get_characters(text):
	dict = {}
	for ch in text:
		lch = ch.lower()
		if(lch in dict):
			nlch = dict[lch] + 1
			dict[lch] = nlch
		else:
			dict[lch] = 1
	return dict

def sort_on(items):
    	return items["num"]

def dict_sort(dict):
	sortlist = []
	for let in dict:
		onedict = {}
		count = dict[let]
		onedict["char"] = let
		onedict["num"] = count
		sortlist.append(onedict)
	sortlist.sort(reverse=True, key = sort_on)
	return sortlist
