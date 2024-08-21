import json
import ast
from elasticsearch import Elasticsearch
import status


def load_api_key(file_path="key.json"):
    """
    Load API key information from a JSON file.
    """
    try:
        with open(file_path, "r") as read_file:
            return json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading API key: {e}")
        return None


def initialize_elasticsearch_client(
    api_key_data, local_ip="localhost", remote_ip="10.0.0.237", ca_cert="ca.crt"
):
    """
    Initialize and return an Elasticsearch client.
    """
    ip = local_ip if status.is_elastic_local() else remote_ip
    verify = status.is_elastic_local()  # Only verify SSL if running locally

    return Elasticsearch(
        f"https://{ip}:9200",
        ca_certs=ca_cert,
        verify_certs=verify,
        api_key=(api_key_data["id"], api_key_data["api_key"]),
    )


def create_query(rulia):
    """
    Create and execute a query on Elasticsearch based on the form data.
    """
    # Initialize rules for the query
    rules = []

    # If "match all" checkbox is not checked, build the query
    if not rulia.data["match_all"]:
        for rule in rulia:
            rule_label = rule.label.text
            rule_data = rule.data.strip()

            # Skip irrelevant form fields and wildcards
            if rule_data != "*" and rule_label not in [
                "Number of results",
                "Source Index",
                "Show all entries",
                "Search",
                "CSRF Token",
            ]:
                rules.append({"match": {rule.description: rule_data}})

    # Convert rules list to a dictionary for the query
    query_body = {"bool": {"filter": rules}} if rules else {"match_all": {}}

    # Execute the query and handle potential errors
    try:
        response = client.search(
            index=rulia.index.data, query=query_body, size=int(rulia.no_results.data)
        )
    except Exception as e:
        print(f"Error querying Elasticsearch: {e}")
        return False

    return response


# Load the API key data
api_key_data = load_api_key()

# Initialize the Elasticsearch client
client = initialize_elasticsearch_client(api_key_data)
