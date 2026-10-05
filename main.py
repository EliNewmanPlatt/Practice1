# CS 1430 - Practice 1: Say It Again
#
# Ask for a whole number, then ask for a phrase, then print the phrase
# that many times. The steps are in README.md.
times = int(input("How many times?"))
question = input("What should I say?")
word = ""
# for i in range(times):
word = question * times
print(word)
# Write your code below this comment.
