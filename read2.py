data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1 #count = count +1
		data.append(line)
		#if count % 1000 == 0: #餘數等於０
			#print(len(data))

print('檔案讀取完了， 總共有', len(data), '筆資料')

print(data[0]) 
print(len(data[0]))
 
sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)

print('平均長度是', sum_len/len(data))

mata = []

for s in data:
	if len(s) < 100:
		mata.append(s)

print('一共有', len(mata), '筆資料長度小於100')

good = []

for a in data:
	if 'good' in a:
		good.append(a)

print('一共有', len(good),'個留言提到good')
print(good[0])