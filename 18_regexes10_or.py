# Finally we can match either or using | (a pipe)
import re

results = re.findall(r"cat|dog","Is this a cat or a dog?")
print(results)

# Regular expressions are extremely flexible but can become 
# very complicated. If you want to learn more I encourage you 
# to check out regexone.com
