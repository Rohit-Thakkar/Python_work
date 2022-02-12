# MAde By 20CE147 Rohit Thakkar

#AIM: You are given n words. Some words may repeat. 
#  For each word, output its number of occurrences. 
#  The output order should correspond with the input order of appearance of the word. 
#  See the sample input/output for clarification. 

# Repo LinK: https://github.com/Rohit-Thakkar/python_assign_sem4/
n_ish = int(input())
counter_dict = {}
words_list = []

for i in range(n_ish):
  word = input()
  words_list.append(word)
  if word in counter_dict:
    counter_dict[word] += 1
  else:
    counter_dict[word] = 1
    
print(len(counter_dict))
print(' '.join([str(counter_dict[word]) for word in counter_dict]))
