arr = [4, 6, 1, 7, 2, 9, 3]

n = len(arr)

for i in range(n-1, 0, -1):
	for j in range(i):
		if arr[j] > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]