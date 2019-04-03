"""This function takes two tuples as input that represent line segments on the x-axis and returns whether or not they overlap"""
def isOverlap(segment1, segment2):
	x1, x2 = segment1
	x3, x4 = segment2

	# If the beginning of segment1 is after segment2's beginning and before segment2's end
	# then the two segments overlap
	if (x1 >= x3 and x1 <= x4):
		return True

	# If the beginning of segment2 is after segment1's beginning and before segment1's end
    # 	# then the two segments overlap
	if (x3 >= x1 and x3 <= x2):
		return True

    # Else the two segments don't overlap
	return False

# Test cases

print(isOverlap((1,5),(2,6)))
print(isOverlap((1,5),(6,8)))

print(isOverlap((2,6),(1,5)))
print(isOverlap((6,8),(1,5)))

print(isOverlap((4,10),(2,6)))
print(isOverlap((4,10),(6,8)))

print(isOverlap((1,5),(3,7)))
print(isOverlap((4,7),(8,10)))

print(isOverlap((3,6),(6,10)))
print(isOverlap((2,7),(1,4)))
