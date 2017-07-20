import re
def get_matching_words(regex):
  results = []
  words = [
    "baby",
    "basebal  l",
    "denver",
    "facetious",
    "issue",
    "mattress",
    "obsessive",
    "paranoia",
    "rabble",
    "union",
    "volleyball",
  ]

  for word in words:
    if re.search(regex, word):
      results.append(word)

  return results

my_expression = r="{(\w)\1,+(\w)\2}"
# my_expression = r"s"
# exclude = .{regex}
print get_matching_words(my_expression)

# What would our output be for this example? Predict the following:
# 1. r"v" = All words containing 'v'
# 2. r"^[aeiou]" = All words that begin with a vowel
# 3. r"(\w)\1" = All words that include an instance where a letter is repeated at least once
#
# Write regular expressions to find words that fit the following criteria, and use the above code to test your regex:
#
# 1. Contains "ss". Should match: ['issue', 'mattress', 'obsessive'] = r"ss"

# 2. Contains a "b", any character, then another "b". Should match: ['baby'] = r"b.b" 

# 3. Contains a "b", one or more characters, then another "b". Should match: ['baby', 'baseball'] = r"r+r"

# 4. Contains all five vowels in order, with any number of characters between them. Should match: ['facetious'] = r".*a.*e.*i.*o.*u"

# 5. Words ending in two vowels. Should match: ['issue', 'paranoia'] = r"[aeiou][aeiou]$"   or r"[aeiou]{2}$"

# 6. Words that only contain the letters in "regular expressions". Should match: ['issue', 'paranoia', 'union'] r="^[regular expression]+$"

# 7. Words that don't contain any of the letters in "regex". Try looking up the two meanings of "^" in regular expressions! Should match: ['baby', 'union']
# Look at the output below, and try to find a regex that will match those words and only those words:r"^[^regex]+$"
#
# 1. ['baby', 'baseball', 'rabble']
# my_expression = r="b.*b"
# 2. ['baby', 'rabble'] Hint: These should remind you of questions 2 and 3 above. What's the same? What's different?
# r="b.*b"
# 3. ['facetious', 'union']
# r="io"
# 4. ['issue', 'obsessive', 'rabble']
# r="" need to work on this
# 5. ['mattress', 'volleyball']
# r="(\w)\1" not quite there yet