import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# This solution is O(n²) quadratic
# for name_1 in names_1:  # iterate through each name in name_1.txt one-by-one
#     for name_2 in names_2:  # iterate through each name in name_2.txt one-by-one
#         if name_1 == name_2:  # if name in name_1.txt is duplicate of name in name_2.txt
#             duplicates.append(name_1)  # append name_1.txt to duplicates list

# This solution is O(n) linear
for name in names_1:  # iterate through each name in name_1.txt one-by-one
    if name in names_2:  # check if name in name_1.txt is also in names_2.txt
        if name not in duplicates:  # check if name is not yet in duplicates list
            duplicates.append(name)  # append all found duplicate names to duplicates list

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
