def open_input(location) -> list:
    """Reads lines from a file and returns them as a list of strings."""
    try:
        with open(location, 'r') as input_file:
            return input_file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {location}")
        return []

def is_safe_report(report):
    """Checks if a report is safe based on the original criteria."""
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences)

def is_safe_with_dampener(report):
    """Checks if a report is safe with the Problem Dampener applied."""
    # Check if the original report is already safe
    if is_safe_report(report):
        return True

    # Try removing each level and check if the modified report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True

    return False

def count_safe_reports_with_dampener(content):
    """Counts the number of safe reports with the Problem Dampener applied."""
    safe_count = 0
    for line in content:
        if line.strip():  # Ignore empty lines
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count

# Example usage
location = r'input.txt'
content = open_input(location)

if content:
    result = count_safe_reports_with_dampener(content)
    print(f"Safe Reports with Dampener: {result}")
else:
    print("No content to process.")
