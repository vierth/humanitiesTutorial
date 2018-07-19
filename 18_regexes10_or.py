# Finally we can match either or using | (a pipe)
import re

results = re.findall(r"cat|dog","Is this a cat or a dog?")
print(results)