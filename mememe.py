import random
char_list=[]
words=[]
retry=0
max_retry=6
print("Welcome to Hangman!")
name=input("What is your name?")
print("Good Luck!", name)

def is_char(char):
	alphabet=('abcdefghijklmnopqrstuvwxyz')
	if ((char.upper()in alphabet) or (char.lower()in alphabet)):
		return True
	else :
		return False
def is_same (char,char_list):
	if char in char_list:
		return True
	else:
		return False
def random_word():
	with open ('answer.csv','r')as f:
		random_word=f.readline()
		print (random_word)
		words=[line for line in f]
		words=list(map(str, random_word.split()))
		print (random.choice(words))
		return words

def show_ans (words,char_list):
	show=list('_'*len(words))
	for i,c in enumerate(words):
		for char in char_list:
			if char == c:
				show[i]=c
	show=''.join(show)
	return show
while (retry<max_retry):
	win=False
	my_input=str(input("Guess the words :"))
	if (is_char(my_input)) and (not is_same(my_input,char_list)):
		char_list.append(my_input)
		print(char_list)
	else:
		print ('Sorry its wrong!!!:')
		continue
	if (my_input in words):
		ans:show_ans(words,char_list)
		print(ans,"Try again!!!", 6-retry)
	else:
		ans=show_ans(words,char_list)
		retry+=1
		print(ans,"Try again!!!", 6-retry)
	if ('_' not in ans):
		win=True
		break
if win==True:
	print ("con con! you win", words)
else:
	print ("sorry! something, try agian later", words)