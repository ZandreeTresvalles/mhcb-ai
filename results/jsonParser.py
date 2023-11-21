import json

# Load the JSON data from file
with open('precRec.json', 'r') as json_file:
    data = json.load(json_file)

# Convert the key-object array to an array of objects
new_data = []
for key, value in data.items():
    obj = {"title": key}
    if isinstance(value, dict):
        obj.update(value)
    else:
        obj["value"] = value
    new_data.append(obj)

# Save the modified data back to the JSON file
with open('precRec_parsed.json', 'w') as json_file:
    json.dump(new_data, json_file, indent=4)
