# << functions >>
def subs(text, word):

	# str to lst for item assign
	text = list(text)
	# var for text position
	pos = 0

	for t in text:
		#print(t)
		if t.lower() == word[pos].lower():
			pos += 1
			index = text.index(t)
		else:
			pos = 0
			
		if pos == len(word):
			# substract lenght word minus actual one (-1) in index var to start from the beggining
			index -= len(word) - 1
			for replace in range(len(word)):
				text[index] = "*"
				index += 1
			break
		
	# join for text decoration
	return "".join(text)

# << main code >>
if __name__ == "__main__":
	text = "My city Castel is pretty"
	word = "castel"
	
	print(subs(text, word))