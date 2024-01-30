from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load the documents
documents = SimpleDirectoryReader('data').load_data()

# Build an index over the documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()


4
# Run a sample query
response = query_engine.query("Who is paul graham?")

# Print the result
print(response)
