import os
import yaml

# Path to the folder containing your YAML files
folder_path = './data'

# Initialize empty lists for intents, responses, actions, and slots
nlu = []
responses = {}
actions = []
slots = []
# Loop through the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    print(file_path)
    # Read YAML files
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        # print("Data: ", data)
        # Extract intents
        if 'nlu' in filename:
            nlu.extend(data)
        # Extract responses
        elif 'responses' in filename:
            responses.update(data)

        # Extract actions
        elif 'actions' in filename:
            actions.extend(data)

        # Extract slots
        elif 'slots' in filename:
            slots.extend(data)
    print("################################")

print("################################ TO BE DUMPED ################################")
print(nlu)
# Generate domain.yml file in Rasa NLU format
domain_data = {
    'nlu': nlu,
    'responses': responses,
    'actions': actions,
    'slots': slots
}

# Write domain.yml file
with open('domain.yml', 'w') as domain_file:
    yaml.dump(domain_data, domain_file, default_flow_style=False)

print("Domain file 'domain.yml' created successfully.")
