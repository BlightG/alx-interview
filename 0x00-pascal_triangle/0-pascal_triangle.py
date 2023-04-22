def pascal_triangle(n):

	if n <= 0:
		return [[]]

	triangle = [[]]

	for i in range(n):
		triangle.append(
			triangle_row(i, triangle)
		)

	return triangle

def triangle_row(i, triangle):

	# print(f'in triangle row returning for i = {i}')#, end="")
	if i == 0:
		# print(f" {[1]}")
		return [1]
	elif i == 1:
		print(f" {[1, 1]}")
		return [1, 1]
	elif i == 2:
		print(f" {[1, 2, 1]}")
		return [1, 2, 1]
	elif i == 3:
		print(f' {[1, 3, 3, 1]}')
		return [1, 3, 3, 1]

	row = []
	range_ = int((i) / 2)
	# print(f' and with range {range_}', end="")

	for j in range(range_ + 1):
		# print(f'foward j = {j}')
		if j == 0:
			row.append(1)
		elif j == 1:
			row.append(i)
		else:
			if i % 2 != 0 and j == range_ + 1:
				continue
			row.append(triangle[i][j - 1] + triangle[i][j])

	if i % 2 != 0:
		for j in range(range_, -1, -1):
			# print(f'reverse j = {j}')
			row.append(row[j])
			# if j - i == 1:
			# 	row.append(1)
			# elif j - 1 == 2:
			# 	row.append(i)
			# else:
			# 	row.append(triangle[i - 1][j - 1] - triangle[i - 1][j])
	else:
		for j in range(range_ - 1, -1, -1):
			# print(f'reverse j = {j}')
			row.append(row[j])
	# print(f' {row}')
	return row
		