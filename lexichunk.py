import os
import re
import numpy as np
from time import perf_counter

#The dictionary is unpacked from the dictionary.txt file and loaded into a NumPy array.

dictionary = np.loadtxt("dictionary.txt", dtype=str)


#The program asks the user for the number of columns and the words in each column.

column_numbers = int(input("How many columns are there?\n"))

os.system('cls' if os.name == 'nt' else 'clear')

all_columns = []

for i in range(column_numbers):
 shortened_words = input(f"What are the shortened words in Column {i+1}?\n").split()
 all_columns.append(shortened_words)
 os.system('cls' if os.name == 'nt' else 'clear')


#The search process starts here.

process_start = perf_counter()

potential_removed_groups = []
all_possible_answers = set()

for x in all_columns:
 
 all_possible_answers = set()

 for y in x:

  #Clears the terminal and informs of you the solving progress.

  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"Solving column {str(all_columns.index(x)+1)}...")
  print(f"Matching words to {y}...")


  #Creates a list of all possible regexes that can check for full words with missing chunks.
  #Also creates a separate list of those compilde patterns.
  #It checks for a word that has any amount of filler letters in any index of the word.

  possible_answers = set()
  regex_needed = []
  compiled_patterns = []
  for i in range(len(y)+1):
   r = f"^{y[:i]}.*{y[i:]}$"
   regex_needed.append(r)
   compiled_patterns.append(re.compile(r))


  #Searches the dictionary and checks for any words that match the given words in the column.
  #Via string slicing, the chunk word is then deduced.

  for z in dictionary:
   for pattern, r in zip(compiled_patterns, regex_needed):
    if y != z and pattern.search(z):
     chunk_start = r.index(".*")-1
     chunk_end = -len(r)+r.index(".*")+3
     if chunk_end != 0:
      removed_chunk = z[chunk_start:chunk_end]
     else:
      removed_chunk = z[chunk_start:]
     possible_answers.add(removed_chunk)


  #If this is the first word in the column, it sets the set all_possible_answers to the set of possible chunks.
  #If not, all_possible_answers is taken as the intersection between itself and possible_answers.

  if x.index(y) == 0:
   all_possible_answers = possible_answers
  else:
   all_possible_answers &= possible_answers


 #When it is done solving for every column, it generates a list of every possible chunk in each column.

 potential_removed_groups.append(all_possible_answers)


#Now, the program clears itself again and attempts every chunk combination.

os.system('cls' if os.name == 'nt' else 'clear')
print("Checking all combinations of chunks...")


#It constructs a regex query to check for chunk combinations, and compiles it.

combo_regex_query = "^" + "".join(f"({'|'.join(x)})" for x in potential_removed_groups) + "$"
pattern = re.compile(combo_regex_query)

valid_solutions = []


#It then finds words matching that pattern, and uses groups() to demarcate chunks with slashes, adding it to valid_solutions.

for w in dictionary:
 match = pattern.match(w)
 if match:
  chunks = match.groups()
  slashed_word = "/".join(chunks)
  valid_solutions.append(slashed_word)


#perf_counter is used here to calculate the time taken for the search.
process_end = perf_counter()


#When the search is completed, a quick overview of the search results is shown.

os.system('cls' if os.name == 'nt' else 'clear')

print("Lexichunk Solved!\n")
for x in all_columns:
 print(f'Column {str(all_columns.index(x)+1)}: {" ".join(x)}')

print('\nAll Possible Chunks:')
for x in potential_removed_groups:
 unslashed_list = [y.replace("/","") for y in x]
 print(f'Column {potential_removed_groups.index(x)+1}: {", ".join(unslashed_list)}')

print(f'\nAll Solutions ({len(valid_solutions)})\n{", ".join(valid_solutions)}')

print(f"\nSearch completed in {round(process_end-process_start,2)}s.")
