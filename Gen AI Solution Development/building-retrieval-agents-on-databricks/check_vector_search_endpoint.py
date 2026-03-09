from databricks.vector_search.client import VectorSearchClient

def check_vector_search_endpoint(endpoint_name: str):
    vsc = VectorSearchClient(disable_notice=True)
    try:
        endpoint = vsc.get_endpoint(endpoint_name)
    except Exception as e:
        raise RuntimeError(f"⛔️ ERROR: Vector search endpoint '{endpoint_name}' does not exist. Details: {e}")
    status = endpoint.get("endpoint_status", {}).get("state", "")
    if status != "ONLINE":
        raise RuntimeError(f"⛔️ ERROR: Vector search endpoint '{endpoint_name}' exists but is not ready.")
    
    print("✅ Vector Search endpoint is ready. ")
    print(f"\n✍️ Vector Search endpoint to use: {endpoint_name}")

vector_search_endpoint = "vs_endpoint_1"
check_vector_search_endpoint(vector_search_endpoint)
