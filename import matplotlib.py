import sys

def find_common_elements(set1, set2):
    # Create sets from the input lists for efficient lookup
    set_a = set(set1)
    set_b = set(set2)
    
    # Find the intersection
    common = set_a.intersection(set_b)
    
    # If no common elements found, return None
    if not common:
        return None
    
    # Convert to list and sort alpha-numerically
    # We'll use a custom sort key to handle both numbers and strings correctly
    result = sorted(list(common), key=lambda x: (str(x).zfill(20) if x.isdigit() else x))
    return result

# Read input using sys.stdin
lines = []
for line in sys.stdin:
    lines.append(line.strip())
    if len(lines) == 2:  # Once we have two lines
        # Process the sets
        set1 = lines[0].split()
        set2 = lines[1].split()
        result = find_common_elements(set1, set2)
        
        # Print result
        if result is None:
            print("NULL")
        else:
            print(" ".join(result))
        
        # Reset lines for next pair of input
        lines = []
