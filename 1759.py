vowel = {'a', 'e', 'i', 'o', 'u'}

L, C = map(int, input().split())
s = sorted(list(input().split()))

pwd = []

def get_kind_word(pwd):
	con = 0
	vow = 0
	for c in pwd:
		if c in vowel:
			con += 1
		else:
			vow += 1
	return con, vow

def dfs(depth):
	if len(pwd) == L:
		con, vow = get_kind_word(pwd)
		if con >= 1 and vow >= 2:
			print(''.join(map(str, pwd)))
		return
	for i in range(depth, C):
		pwd.append(s[i])
		dfs(i + 1)
		pwd.pop()

dfs(0)
