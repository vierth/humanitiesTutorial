# Variables save data for reuse later in our code. We create
# them with an "=" sign.

# You can name them almost anything you want as long you
# start with a letter. Make them intelligble, but avoid 
# reserved words. They cannot start with numbers, and capital
# letters are generally used for other constructs

# These work but aren't informative
a = "yum"
b = 5
c = 5.2

# These are better and in "camelcase"
feeling = "hungry"
currentYear = 2018
heightCm = 173.2

# You could use underscores instead or leave everything 
# lowercase
current_year = 2018
currentyear = 2019
# Python is case sensitive, so currentyear is not the same as
# currentYear

# do NOT do this:
str = "Friend"
# If you are using a program with syntax highlighting, most 
# reserved words will turn a different color

print(a)
print(b)
print(c)

# You can print multiple things easily:
print(feeling, currentYear, heightCm, str)