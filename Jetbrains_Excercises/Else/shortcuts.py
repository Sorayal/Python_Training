
# Shortcuts

# The program below asks the user if they have slept enough, and suggests drinking either coffee or cocoa depending on the answer.

# print("Have you had enough hours of sleep today?")
# answer = input()
# if answer == "yes":
#     print("Let's drink cocoa!")
# else:
#     print("I'd recommend a coffee!")
# Now let's rewrite this if-else statement (note: do not include the first two lines of code in your answer). It should produce the same result but in one line.

# Your answer should look like this:

# print(...)
# where ... stands for the if-else statement, which does the same thing as the one presented in the example, but is written in one line.


print("Have you had enough hours of sleep today?")
answer = input()
print("Let's drink cocoa!" if answer == "yes" else "I'd recommend a coffee!")
