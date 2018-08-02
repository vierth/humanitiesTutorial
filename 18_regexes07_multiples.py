# We've already seen how to match zero or more/one or more 
# times. You can also make this much more specific.
import re

# {3} will match something with exactly 3 occurences
result = re.search(r"a{3}","Will we match a or aaa?")
print(result)

# {1,4} will match something occuring at least once but
# as many as four times

# {,4} will match something up to four times

#{4,} will match something four or more times
