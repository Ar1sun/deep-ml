def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) != len(b):
		return -1
	return [x + y for x, y in zip(a, b)]
vector_1 = [1, 2, 3]
vector_2 = [3, 4, 5]
result = vector_sum(vector_1, vector_2)