def is_prime(num):
   if num <= 1:
      return False
   for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
	 return False
   return True
prime_numbers = {num for num in range(1, 51) if is_prime(num)}
odd_numbers = {num for num in range(1, 21) if num % 2 != 0}
print("Prime Numbers:", prime_numbers)
print("Odd Numbers:", odd_numbers)
union_set = prime_numbers.union(odd_numbers)
print("Union:", union_set)
intersection_set = prime_numbers.intersection(odd_numbers)
print("Intersection:", intersection_set)
difference_set = prime_numbers.difference(odd_numbers)
print("Difference (Prime - Odd):", difference_set)
symmetric_difference_set = prime_numbers.symmetric_difference(odd_numbers)
print("Symmetric Difference:", symmetric_difference_set)
