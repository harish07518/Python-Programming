def generate_pairs(input_list):
   result = []
   for number in input_list:
      result.append(number - 1)
      result.append(number + 1)
   return tuple(result)
# Test case 1
input1 = [500]
output1 = generate_pairs(input1)
print("Input: {i1} \nOutput: {o1}".format(i1=input1,o1=output1))

# Test case 2
input2 = [1, 2, 3]
output2 = generate_pairs(input2)
print("Input: {i2} \nOutput: {o2}".format(i2=input2,o2=output2))
