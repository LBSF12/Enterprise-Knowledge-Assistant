from backend.retrieval import search_documents


question = "How many annual leave days do employees receive?"


print("\nQUESTION:")
print(question)

print("\nRETRIEVED CHUNKS:\n")


results = search_documents(question)


for number, result in enumerate(results, start=1):

    print(f"----- RESULT {number} -----")

    print("Source:", result["source"])
    print("Department:", result["department"])
    print("Score:", result["score"])

    print("\nText:")
    print(result["text"])

    print()