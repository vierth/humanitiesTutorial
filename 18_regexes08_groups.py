# You can return just part of your match using groups:
import re

# groups are formed with ()
someHtml = "<a href='www.google.com'>"

result = re.search(r"<a href='(.+)'>", someHtml)
print(result)
# get the group:
print(result.group(1))

# You can also have multiple groups:
myString = "It occured from pages 336-7."
result = re.search('(\d+)-(\d+)',myString)

firstnumber = result.group(1)
secondnumber = result.group(2)

print(firstnumber, secondnumber)