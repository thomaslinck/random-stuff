def check_valid_palindrom(word): 
	validated_word = list(map(str.lower, filter(str.isalnum, word)))
	if not validated_word: 
		return True
	return recursive_check(validated_word, 0)

def recursive_check(w, i): 
	if i > int(len(w)/2): 
		return True 

	if w[i] == w[-(i+1)]:
		return recursive_check(w, i+1)
	else: 
		return False 

print(check_valid_palindrom("ab b a"))
print(check_valid_palindrom("A man, a plan, a canal: Panama"))
print(check_valid_palindrom("rAce a Car"))
print(check_valid_palindrom("A"))
print(check_valid_palindrom(" "))