'''
So far this code could find a path from the source to the target node
but I don't figure out why this code can't find all possible paths.

Anyway this is the first code I use the states idea to code, and it works 
pretty good.

In this code, I use the recursion method to do the DFS search. So I had a 
great start of this new try. 
'''

import itertools
moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
bucks = [8, 5, 3]
		

# def moves():
# 	idx = range(3)
# 	return list(itertools.permutations(idx, 2))

def move_to(state, moves):
	states = []
	
	for move in moves:
		# print state
		state_ = state[:] #this [:] method will copy the list instead of just reference the list
		fr, to = move[0], move[1]
		capacity = bucks[to] - state_[to]

		# print fr, to, state_
		if state_[fr] != 0:
			if capacity > state_[fr]:
				state_[to] = state_[to] + state_[fr]
				state_[fr] = state_[fr] - state_[fr]
			else:
				state_[to] = state_[to] + capacity
				state_[fr] = state_[fr] - capacity
			if state_ not in states:
				# print state_
				states.append(state_)
	return states

def DFS(queue, visited, path, target):
	if len(queue) < 1:
		return
	state = queue.pop()

	if state == target:
		print 'state', path
		# return

	candidates = move_to(state, moves)
	# print 'visited', visited
	visited.append(state)
	for candidate in candidates:
		if candidate not in visited:
			queue.append(candidate)
	DFS(queue, visited, path+str(state), target)


def dfs(start, target):
	'''
	Still here has the problem of recording the visited notes
	'''
	result = []
	queue = [(start,[])]
	cnt = 0
	while queue:
		state, path = queue.pop()
		# print 'path', path
		if state == target:
			result.append((len(path),path))
		candidates = move_to(state, moves)
		# print candidates
		path.append(state)
		for candidate in candidates:
			if candidate not in path:
				queue.append((candidate, path[:]))
	return result

if __name__ == '__main__':
	state = [8, 0, 0]
	target = [4, 4, 0]
	path = ''
	result = dfs(state, target)
	print 'Possible ways: ', len(result)
	for i in sorted(result, key=lambda x:x[0]):
		print i
	# can = [[8, 0, 0], [0, 0, 0]]
	# test = [0,0,0]
	# print test not in can