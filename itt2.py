def process_string(input_string):
   vowel_count = 0
   result_string = []
   vowels = set("aeiouAEIOU")

   for char in input_string:

      if char.isupper():
	 result_string.append(char.lower())
      else:
	 result_string.append(char.upper())

      # Count and remove vowels
      if char in vowels:
	 vowel_count += 1
	 result_string.pop()
   modified_string = ''.join(result_string)
   result_list = list(modified_string)	
   return modified_string, vowel_count, result_list
input_string = "Hello"
output1, output2, output3 = process_string(input_string)
print(output1)
print(output2)
print( ''.join(output3))
