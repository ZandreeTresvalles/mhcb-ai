import rasa


def evaluate_model(model_path, data_path):
    interpreter = rasa.model.get_model(model_path).get_interpreter()
    evaluation_data = rasa.utils.io.read_evaluation_file(data_path)

    intent_metrics = rasa.model.test.compare_nlu(interpreter, evaluation_data)
    intent_precision = intent_metrics.get("intent_evaluation").get(
        "report").loc["weighted avg", "precision"]
    intent_recall = intent_metrics.get("intent_evaluation").get(
        "report").loc["weighted avg", "recall"]

    entity_metrics = rasa.model.test.evaluate_entities(
        interpreter, evaluation_data)
    entity_precision = entity_metrics.get("precision")
    entity_recall = entity_metrics.get("recall")

    print(f"Intent Precision: {intent_precision}")
    print(f"Intent Recall: {intent_recall}")
    print(f"Entity Precision: {entity_precision}")
    print(f"Entity Recall: {entity_recall}")


model_path = "/models/20231118-200606-gilded-grid.tar.gz"
data_path = "/data/"

evaluate_model(model_path, data_path)
