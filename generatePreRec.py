import json
import matplotlib.pyplot as plt

# Path to the Rasa NLU evaluation report JSON file
evaluation_report_path = 'results/precRec.json'

# Load the evaluation report
with open(evaluation_report_path, 'r') as report_file:
    evaluation_report = json.load(report_file)

# Extract precision and recall values for intents
intent_names = []
precisions = []
recalls = []

for intent_name, intent_metrics in evaluation_report.get('intent_evaluation').get('predictions').items():
    intent_names.append(intent_name)
    precisions.append(intent_metrics.get('precision'))
    recalls.append(intent_metrics.get('recall'))

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(intent_names, precisions, marker='o', label='Precision')
plt.plot(intent_names, recalls, marker='x', label='Recall')
plt.title('Precision and Recall for Intents')
plt.xlabel('Intents')
plt.ylabel('Score')
plt.legend()
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
