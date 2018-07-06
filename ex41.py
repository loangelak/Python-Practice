#class | tell python to make a new kind of thing
#object | 2 meanings: the most basic kind of thing, and any instance of some thing
# instance | what you get when you tell python to create a class
# def | how you define a function inside a class
#self | inside the functions in a class, self is a variable for the instance/object being accessed
#inheritance | the concept that one class can inherit traits from another class, much like you and your parents
#composition | the concept that a class can be composed of other classes as parts, much like how a car has wheels
#attribute | a property classes have that are from composition and are usually variables.
#is-a | a phrase to say that something inherits from another, as a Salmon is-a Fish
#has-a | a phrase to say that somehting is composed of other things or has a trait, as in a Salmon has-a mouth.

import random 
from urllib import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
	"class ###(###)":
	"Make a class named ### that is-a ###.", 
	"class ###(object):\n\tdef __init__(self, ***)": 
	"class ### has-a __init__ that takes self and *** parameters.", 
	"class ###(object):\n\tdef ***(self, @@@)": 
	"class ### has-a function named *** that takes self and @@@ parameters.", 
	"*** = ###()":
	"Set *** to an instance of class ###.", 
	"***.***(@@@)": 
	"From *** get the *** function, and call it with parameters self, @@@.", 
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english": 
	PHRASE_FIRST = True

#load up the words from the website
for word in urlopen(WORD_URL).readlines(): 
	WORDS.append(word.strip())

def convert(snippet, phrases): 
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("###"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase: 
		result = sentence[:]

		#fake class names
		for word in class_names: 
			result = result.replace("###", word, 1)

		#fake other names
		for word in other_names: 
			result = result.replace("***", word, 1)

		#fake parameter lists
		for word in param_names: 
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

#keep going until they hit CTRL-D
try: 
	while True: 
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets: 
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST: 
				question, answer = answer, question

			print question 

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError: 
	print "\nBye"


