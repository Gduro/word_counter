import nltk
from nltk.tokenize import word_tokenize
from colorama import Fore, Back, Style
ai = input(Fore.YELLOW+ "Podaj zdanie: ")
token = word_tokenize(ai)
print(Fore.GREEN + "Ilość słów w zdaniu wynosi: "+Fore.RED+ str(len(token)) + Fore.RESET)