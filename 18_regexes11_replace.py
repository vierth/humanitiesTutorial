# Replacing values is an extremely important use of regexes
import re

# Replace multiple spaces with a single space:
myString = "This has a     few   spaces."
myString = re.sub(r"\s+"," ",myString)
print(myString)

# Change all cats and dogs to kapow!
myString2 = "cats and dogs and logs are dogs"
myString2 = re.sub(r"cats|dogs", "kapow!", myString2)
print(myString2)

# Add some markup:
myString3 = "Oh Captain, my Captain. Are you a General?"
myString3 = re.sub(r"(Captain|General)","<title>\g<1></title>", myString3)
print(myString3)


# Regular expressions are extremely flexible but can become 
# very complicated. If you want to learn more I encourage you 
# to check out regexone.com
