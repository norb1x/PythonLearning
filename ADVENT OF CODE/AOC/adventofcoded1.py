def open_input(location) -> list:
    """Reads lines from a file and returns them as a list of strings."""
    try:
        with open(location, 'r') as input_file:
            return input_file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {location}")
        return []
    
a_list = []
b_list = []
content = open_input(r'input.txt')

for line in content:
    try:
        
        a, b = map(int, line.strip().split())  
        a_list.append(a)
        b_list.append(b)
    except ValueError:
        print(f"Skipping invalid line: {line.strip()}")  


print("a_list before sorting:", a_list)
print("b_list before sorting:", b_list)

a_list.sort()
b_list.sort()
sum_dist = sum(abs(a - b) for a, b in zip(a_list, b_list))

print("Part I: Total distance between the lists =", sum_dist)
sim_score = sum(num for num in b_list if num in set(a_list))

print("Part II: Similarity score =", sim_score)
