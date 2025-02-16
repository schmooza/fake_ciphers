def encode():
  import pandas as pd
  import math
  import random
  import copy
  
  message = " The money is in the big bank."
  print("orignial message: ", message)
  list_of_words = message.split()
  
  
  length_of_list = len(list_of_words)
  length_of_list_enum = length_of_list
  
  print("number of words in list:",length_of_list)
  
  # make a list of numbers based on how many words are in the sentence.
  indexList = []
  for n in range (0, length_of_list):
      indexList.append(length_of_list_enum)
      length_of_list_enum = length_of_list_enum - 1 # reduce by 1
  
  print ("shows original postions",indexList )
   # make a copy of the index list.
  
  
  indexList.reverse()
  deep_copy_index_list = copy.deepcopy(indexList)
  
  
  print("shows the reversed index list", indexList)
  print("shows the deep copy",deep_copy_index_list, ) # need a copy to mess with later. deep copy is not linked to original.
  
  shuffled_index_list = random.sample(deep_copy_index_list, len(deep_copy_index_list))
  
  print("Shows the shuffled list",shuffled_index_list) # this will be the key for the cipher.
  
  
  # Sort a using b
  shuffled_message = [val for _, val in sorted(zip(shuffled_index_list, list_of_words))]
  
  print(shuffled_message, "message has been shuffled using the random order of index locations")
  print("____________________________________________________________")
  
  
  ##############################################################################################
  
  
  
  
  
  cut_in_half = length_of_list / 2
  rounded = math.floor(cut_in_half)
  print("cut list at row: ",rounded)
  
  
  
  # Index where the list will be split
  n = rounded
  
  # Slice the list from the beginning to the nth index (not inclusive)
  first_slice = shuffled_message[:n]
  
  # Slice the list from the nth index to the end
  second_slice = shuffled_message[n:]
  
  reversed_second_slice = second_slice[::-1]
  
  
  # Print the first slice of the list
  print("First slice:", first_slice) 
  # Print the second slice of the list
  print("The second slice is reversed", reversed_second_slice)
  
  df = pd.DataFrame({'1': pd.Series(first_slice), '2': pd.Series(reversed_second_slice)})
  
  print(df)
  print("Copyright Mr. Simmonds 2025")
  return df, shuffled_index_list
df, key = encode()

def decode(df, key):
   print(df, key, "checking imports")

decode(df, key)
