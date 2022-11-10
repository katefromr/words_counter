with open('name.txt', 'r') as file: #instead of name.txt put your .txt file with text
	text = file.read()
    
def lets_count(text):
    counter = {}
    for elem in text.lower().split():
        if elem not in counter:
            counter[elem] = 1
        else:
            counter[elem] += 1
    import collections
    for key, value in collections.Counter(counter).most_common(1):
        print("{} {}".format(key, value))
    
lets_count(text)
