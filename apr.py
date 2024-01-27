import re
from collections import defaultdict
import json

line_regex = r"^(\d{2}:\d{2}).*(\d{2}:\d{2}).*?\d{4}"
date_regex = r"^\d{2}-\d{2}-\d{4}"
hour_regex = r"^\d{1,2}$"

regex_patterns = [hour_regex, date_regex, line_regex]

nested_dict = defaultdict(list)
# nested_dict = defaultdict(lambda: defaultdict(list))

# Open the file ans.txt and read it line by line
with open('all_text_data.txt', 'r') as file:
    # for line in file:
    last_date = ''
    for line_number, line in enumerate(file, start=1):
            for idx, pattern in enumerate(regex_patterns, start=1):
                match = re.match(pattern, line)
                if match:
                    # print("First matching pattern:", pattern)
                    if idx == 2:
                        date = match.group()
                        last_date = date
                        nested_dict[date].append([])
                        print(f"Last Date: {last_date}")
                    if idx == 3:
                        value = match.group()
                        [from_min, to_min, price] = [item for item in value.split(' ') if item != '-']
                        filtered_list = [from_min, to_min, price]
                        nested_dict[last_date].append(filtered_list)
        # print("data:", nested_dict[last_date])

# print(json.dumps(nested_dict, indent=4))
print("Number of keys:", len(nested_dict))

out_file = "data.json"

# Write dictionary to file
with open(out_file, "w") as file:
    json.dump(nested_dict, file)
