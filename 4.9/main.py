# Write a program that asks the user to enter a sentence, terminated
# by a full stop and the pressing of the Enter key.  The program should
# count the number of words and display the result.

# HINT: create a loop which looks at the string character by character,
# keeping a running total of words.  The word count is incremented when
# a space is detected.

Sentence = input("Please Enter A Sentence Terminating in a Full Stop and Hit Enter...")

SentenceLength = len(Sentence)

print("Your Sentence Was", SentenceLength, "Characters Long.")