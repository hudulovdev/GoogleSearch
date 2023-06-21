from googlesearch import search

def search_google(query, num_results):
    search_results = []
    for result in search(query, num_results=num_results):
        search_results.append(result)
    return search_results

# Example usage
query = input("What Do you want to search? :")
num_results = int(input("Number of results you see"))

results = search_google(query, num_results)
for index, result in enumerate(results):
    print(f"Result {index+1}: {result}")