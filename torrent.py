def parse_chunks(chunks):
	item = chunks.pop()
	
	if item == 'i':
		item = chunks.pop()
		num = ''
		while item != 'e':
			num += item
			item = chunks.pop()
		return int(num)
	
	elif item.isdigit():
		num = ''
		while item.isdigit():
			num += item
			item = chunks.pop()
		line = ''
		i = 0
		while i < int(num):
			line += chunks.pop()
			i += 1
		return line
		
	elif item == 'l':
		list = []
		item = chunks.pop()
		while item != 'e':
			chunks.append(item)
			list.append(parse_chunks(chunks))
			item = chunks.pop()
		return list
		
	elif item == 'd':
		dictionary = {}
		item = chunks.pop()
		while item != 'e':
			chunks.append(item)
			key = parse_chunks(chunks)
			dictionary[key] = parse_chunks(chunks)
			item = chunks.pop()
		return dictionary
		
	raise "invalid input"
	
def decode(data):
	chunks = list(data)
	chunks.reverse()
	decoded = parse_chunks(chunks)
	return decoded