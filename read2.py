data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1 #count = count +1
		data.append(line)
		if count % 1000 == 0: #餘數等於０
			print(len(data))


