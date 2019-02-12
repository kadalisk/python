quote = "\"Hello, I contain a \"single quote\""

multi_line_quote = '''and I'm 
                        multi line quote'''

print("%s %s %s" % ('Example of quotes',quote,multi_line_quote))

# STRINGS -------------
# A string is a series of characters surrounded by ' or "
long_string = "I'll catch you if you fall - The Floor"

# Retrieve the first 4 characters
print(long_string[0:4])

# Get the last 5 characters
print(long_string[-5:])

# Everything up to the last 5 characters
print(long_string[:-5])

# Concatenate part of a string to another
print(long_string[:4] + " be there")