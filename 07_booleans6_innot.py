# in and not are useful boolean expressions for strings:
if "run" in "I run the team.":
    print("run found in the string")

if "yum" not in "I run the team.":
    print("yum not found")

# not can also be used by itself
pod = False
if not pod:
    print("Pod was false")