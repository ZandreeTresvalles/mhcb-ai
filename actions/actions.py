# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("I am edia mental health chatbot")
        dispatcher.utter_message(text="Hello!")

        return []


utterances = {
    'types_of_adhd': "ADHD, or Attention-Deficit/Hyperactivity Disorder, has several types...",
    'inattentive_adhd_type': "Inattentive ADHD, often referred to as ADHD without hyperactivity...",
    'hyperactivity_impulsivity_adhd_type': "Hyperactivity and Impulsivity ADHD is characterized by excessive energy...",
    'combined_adhd_type': "Combined type ADHD is when individuals exhibit both inattentive and hyperactive-impulsive symptoms...",
    'user_express_adhd_concerns': "It's essential to recognize these symptoms and seek the support you need...",
    'ask_coping_strategies_adhd': "Living with ADHD can be challenging...",
    'user_share_adhd_experience': "Thank you for opening up about your experiences with ADHD...",
    'helping_someone_with_adhd': "Supporting someone with ADHD is commendable...",
    'coping_with_adhd_alarms': "Using alarms can be incredibly helpful in managing ADHD...",
    'coping_with_adhd_schedule': "Creating a structured daily schedule is a fantastic strategy for managing ADHD...",
    'coping_with_adhd_task_lists': "Task lists are a great tool for managing ADHD...",
    'coping_with_adhd_minimizing_distractions': "Minimizing distractions can be a game-changer when dealing with ADHD...",
    'coping_with_adhd_mindfulness': "Practicing mindfulness and meditation can help calm the mind...",
    'ask_adhd_symptoms_inattentive_1': "Do you ever find it challenging to pay close attention to details...",
    # Add other utterance-text pairs here
    'positive_likelihood_adhd': "Based on the symptoms you've described, it's possible that you may be experiencing signs commonly associated with ADHD...",
    'negative_likelihood_adhd': "While the symptoms you've mentioned can be challenging, they may not necessarily indicate ADHD..."
}

slots = {
    "adhd_symptoms_inattentive_1": "yes",
    "adhd_symptoms_inattentive_2": "yes",
    "adhd_symptoms_inattentive_3": "no",
    "adhd_symptoms_inattentive_4": "no",
    "adhd_symptoms_inattentive_5": "yes",
    "adhd_symptoms_inattentive_6": "no",
    "adhd_symptoms_inattentive_7": "yes",
    "adhd_symptoms_inattentive_8": "no",
    "adhd_symptoms_hyperactive_impulsive_1": "yes",
    "adhd_symptoms_hyperactive_impulsive_2": "no",
    "adhd_symptoms_hyperactive_impulsive_3": "yes",
    "adhd_symptoms_hyperactive_impulsive_4": "no",
    "adhd_symptoms_hyperactive_impulsive_5": "yes",
    "adhd_symptoms_hyperactive_impulsive_6": "no",
    "adhd_symptoms_hyperactive_impulsive_7": "yes",
    "adhd_symptoms_hyperactive_impulsive_8": "no",
    # Add other slot-value pairs here
    "affirm_adhd_symptoms_inattentive_1": "yes",
    "affirm_adhd_symptoms_inattentive_2": "yes",
    "affirm_adhd_symptoms_inattentive_3": "yes",
    "affirm_adhd_symptoms_inattentive_4": "yes",
    "affirm_adhd_symptoms_inattentive_5": "yes",
    "affirm_adhd_symptoms_inattentive_6": "yes",
    "affirm_adhd_symptoms_inattentive_7": "yes",
    "affirm_adhd_symptoms_inattentive_8": "yes",
    "deny_adhd_symptoms_inattentive_1": "no",
    "deny_adhd_symptoms_inattentive_2": "no",
    "deny_adhd_symptoms_inattentive_3": "no",
    "deny_adhd_symptoms_inattentive_4": "no",
    "deny_adhd_symptoms_inattentive_5": "no",
    "deny_adhd_symptoms_inattentive_6": "no",
    "deny_adhd_symptoms_inattentive_7": "no",
    "deny_adhd_symptoms_inattentive_8": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_1": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_2": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_3": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_4": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_5": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_6": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_7": "no",
    "deny_adhd_symptoms_hyperactive_impulsive_8": "no",
}


def respond_to_input(input_text, slots):
    response = ""

    # Iterate through the utterances
    for utterance, text in utterances.items():
        # Check if the input text matches any of the utterances
        if input_text.startswith("utter_" + utterance):
            # Extract the slot name from the input text
            slot_name = utterance.replace("utter_", "")
            if slot_name in slots:
                # If the slot exists and has a value
                if slots[slot_name] == "yes":
                    response = text
                    break

    if response:
        print(response)
    else:
        print("No appropriate response found for the input.")


user_input = "utter_ask_adhd_symptoms_inattentive_1"
respond_to_input(user_input, slots)
