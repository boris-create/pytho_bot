def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')
    print('Welcome to my "Shit Show"')


def remind_name():
    print('Please, remind me your name.')
    name = input("Your name please? ")
    print('What a great name you have, ' + name + '!')


def guess_age():
    print()
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input("Remainder 1? "))
    rem5 = int(input("Remainder 2? "))
    rem7 = int(input("Remainder 3? "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) +
          "; that's a good time to start programming!")
    print("Yes I know, this isn't very accurate.")


def count():
    print()
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input("What will you choose? "))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print()
    print("Let's test your knowledge.")
    print("""
  What is the most popular drink in the world that does not have alcohol?
  1. Water.
  2. Soda.
  3. Coffee.
  4. Tea.
  """)
    while input("Your answer? ") != "3":
        print("Please, try again.")
    print('Correct, good job sport!')


def end():
    print()
    print('Congratulations, have a nice day!')
    print('-End Shit Show-')


greet('Boris', '2020')
remind_name()
guess_age()
count()
test()
end()


# This function does nothing
def lazy_func(param):
    pass
