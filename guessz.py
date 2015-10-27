print("welcome to guess the number")
number = 10
guess = int(raw_input("Enter a guess"));

if guess < number:
	print "Too low"

elif guess > number:
	print "Too high"

elif guess == number:
	print "Correct"