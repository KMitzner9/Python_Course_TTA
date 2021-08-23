# Python Challenges

## String Challenges
# Assign a string to a variable
string1 = "Programming Poetry"
print(string1)

# Assign a multiline string to a variable
poem = """There once was a language without direction,
It lacked thought, planning and any affection.
PHP was insane,
And to save you from your pain,
You'd need morphine in your SQL injection."""
print(poem)

# Return a range of characters by using the slice syntax
print(poem[28:55])

# Use the len() method
print(len(poem))

# Use the strip() method
string2 = "  Too much white in this space.  "
print(string2.strip())

# Use the upper() method
print(poem.upper())

# Use the in or not keyword to check whether a substring is present
print("SQL" in poem)
print("insane" not in poem)

# Concatenate a string
print(string1 + " is unimpressive.")

# Use an escape character
string3 = "They call this \"poetry\", hah!"
print(string3)


## Operator Challenges
# Use an arithmetic operator
num1 = 5
num2 = 7
print(num2 % num1)

# Use an assignment operator
num3 = 38
print(num3)

# Use a comparison operator
print(num3 == 40)

# Use a logical operator
print(num3 == 38 and num1 <= num2)

# Use an identity operator
print(num1 is 5)
print(num1 is not num2)

# Use a membership operator
print("8" in poem)

# Use a bitwise operator
print(num1 | num3)


## Lists Challenge
# Create a list
apparatuses = ["Lyra", "Fabric", "Sling", "Trapeze", "Rope", "Straps"]

# Loop through the list with a for loop
for a in apparatuses:
    print(a)

# Use the append() method
apparatuses.append("Cloud Swing")
print(apparatuses)

# Make a copy of a list using the method copy()
apparatuses_copy = apparatuses.copy()
print(apparatuses_copy)

# Concatenate two lists
groundskills = ["Handstands", "Tumbling", "Firedance"]
classes = apparatuses + groundskills
print(classes)

# Use the reverse() method on a list
classes.reverse()
print(classes)
