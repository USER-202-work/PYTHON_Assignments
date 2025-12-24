
# ==========================
# STRINGS – Coding Questions
# ==========================

print("\n--- STRINGS ---")

# 1) Count vowels, consonants, digits, special characters
s = "Hello, World! 123"
vowels_set = set("aeiouAEIOU")
vowels = consonants = digits = specials = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        specials += 1

print("1) Counts for:", s)
print({"vowels": vowels, "consonants": consonants, "digits": digits, "specials": specials})

# 2) Reverse each word individually without changing word order
s2 = "I  love Python"
reversed_each_word = " ".join(word[::-1] for word in s2.split(" "))
print("\n2) Reverse each word (preserve order):")
print("Input: ", s2)
print("Output:", reversed_each_word)

# 3) Check palindrome using indexing and slicing
s3 = "racecar"
is_pal_slicing = (s3 == s3[::-1])

i, j = 0, len(s3) - 1
is_pal_indexing = True
while i < j:
    if s3[i] != s3[j]:
        is_pal_indexing = False
        break
    i += 1
    j -= 1

print("\n3) Palindrome checks for:", s3)
print("By slicing: ", is_pal_slicing)
print("By indexing:", is_pal_indexing)

# 4) Frequency of each character in a string
s4 = "banana"
freq = {}
for ch in s4:
    freq[ch] = freq.get(ch, 0) + 1
print("\n4) Character frequency for:", s4)
print(freq)

# 5) Demonstrate string immutability by attempting to modify a character
s5 = "Immutable"
print("\n5) String immutability demo:")
try:
    s5[0] = 'i'  # This will raise TypeError
except TypeError as e:
    print("Caught error:", e)


# ==========================
# LIST – Coding Questions
# ==========================

print("\n--- LISTS ---")

# 1) Remove duplicates from a list without using set (preserve order)
lst1 = [1, 2, 2, 3, 4, 4, 5, 1]
seen = []
unique = []
for item in lst1:
    if item not in seen:
        seen.append(item)
        unique.append(item)
print("1) Remove duplicates (preserve order):")
print("Input: ", lst1)
print("Output:", unique)

# 2) New list containing only even numbers using list comprehension
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in lst2 if isinstance(x, int) and x % 2 == 0]
print("\n2) Even numbers via list comprehension:")
print("Input: ", lst2)
print("Output:", evens)

# 3) Find the second largest element in a list (without sorting)
lst3 = [10, 20, 20, 8, 6, 4]
largest = None
second = None
for x in lst3:
    if largest is None or x > largest:
        second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        second = x
if second is None:
    raise ValueError("List must contain at least two distinct elements.")
print("\n3) Second largest in:", lst3)
print("Second largest:", second)

# 4) Create a nested list and calculate the sum of each inner list
nested = [[1, 2, 3], [10, 20], [5]]
sums = [sum(inner) for inner in nested]
print("\n4) Sum of each inner list:")
print("Input: ", nested)
print("Output:", sums)

# 5) Demonstrate shallow copy and deep copy with mutable elements
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)      # or original[:]
deep = copy.deepcopy(original)
original[0][0] = 99                # mutate inner list in original

print("\n5) Shallow vs Deep copy demo:")
print("Original:", original)       # [[99, 2], [3, 4]]
print("Shallow:", shallow)         # reflects inner mutation -> [[99, 2], [3, 4]]
print("Deep:   ", deep)            # unaffected -> [[1, 2], [3, 4]]


# ==========================
# TUPLE – Coding Questions
# ==========================

print("\n--- TUPLES ---")

# 1) Find the maximum and minimum elements in a tuple
tpl1 = (5, 2, 9, 9, 1)
mx = max(tpl1)
mn = min(tpl1)
print("1) Max & Min of", tpl1, "=>", (mx, mn))

# 2) Convert a list of tuples into a dictionary
pairs = [("a", 1), ("b", 2), ("a", 3)]
d = {}
for k, v in pairs:
    d[k] = v  # last value for duplicate keys wins
print("\n2) List of tuples to dict:")
print("Input: ", pairs)
print("Output:", d)

# 3) Count the occurrence of an element in a tuple without using built-in methods
tpl3 = (5, 2, 9, 9, 1)
target = 9
count = 0
for x in tpl3:
    if x == target:
        count += 1
print("\n3) Count occurrence without tuple.count():")
print("Tuple:", tpl3, "| Target:", target, "| Count:", count)

# 4) Create a tuple with mutable elements and modify the mutable data inside it
t = (1, [2, 3], "x")
t[1].append(4)  # allowed: modify the list inside the tuple
print("\n4) Tuple with mutable modified:", t)
# t[0] = 10  # This would raise TypeError (tuples are immutable)

# 5) Swap two tuples
a = (1, 2)
b = (3, 4)
a, b = b, a
print("\n5) Swapped tuples:", "a =", a, "| b =", b)


# ==========================
# SET – Coding Questions
# ==========================

print("\n--- SETS ---")

# 1) Union, intersection, difference, symmetric difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union_ = A | B
intersection_ = A & B
difference_ = A - B
symdiff_ = A ^ B
print("1) Set operations for A =", A, "and B =", B)
print({
    "union": union_,
    "intersection": intersection_,
    "difference_a_minus_b": difference_,
    "symmetric_difference": symdiff_
})

# 2) Remove common elements from two sets (from both)
common = A & B
A_no_common = A - common
B_no_common = B - common
print("\n2) Remove common elements from both:")
print("A without common:", A_no_common)
print("B without common:", B_no_common)

# 3) Check whether one set is a subset of another
subset_check = {1, 2}
is_subset = subset_check.issubset(A)
print("\n3) Is", subset_check, "a subset of", A, "?", is_subset)

# 4) Iterate over a set and print only elements greater than a given number
threshold = 3
print("\n4) Elements in A greater than", threshold, ":")
for x in A:
    if x > threshold:
        print(x)

# 5) Given a list with duplicates, convert to a set and back to a list with unique elements
dup_list = [1, 2, 2, 3, 1, 4, 3]
unique_set = set(dup_list)
unique_list = list(unique_set)  # order not preserved
unique_list_ordered = list(dict.fromkeys(dup_list))  # preserves original order
print("\n5) Unique elements from list:")
print("Input: ", dup_list)
print("Unordered unique:", unique_list)
print("Ordered unique:  ", unique_list_ordered)


