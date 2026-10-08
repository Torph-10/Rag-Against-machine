import fire

def index(max_chunk_size: int = 2000):
    """Ingest data/raw/ and build the index under data/processed/."""
    print(f"Indexing with max chunk size {max_chunk_size}")

def search(query: str, k: int = 5):
    """Return the top-k sources for a single query."""
    print(f"Searching for '{query}' and returning top {k} results")

def search_dataset(dataset_path: str, k: int, save_directory: str):
    """Run search over a whole dataset and write a StudentSearchResults JSON file."""
    print(f"Searching dataset {dataset_path} with k={k} and saving to {save_directory}")

def answer(query: str, k: int = 5):
    """Answer a single query using the retrieved context."""
    print(f"Answering query '{query}' with k={k}")

def answer_dataset(student_search_results_path: str, save_directory: str):
    """Generate answers for a dataset, producing a StudentSearchResultsAndAnswer JSON file."""
    print(f"Generating answers from {student_search_results_path} and saving to {save_directory}")

def evaluate(student_search_results_path: str, dataset_path: str):
    """Report your own recall@k against a ground-truth dataset."""
    print(f"Evaluating {student_search_results_path} against {dataset_path}")

if __name__ == '__main__':
    fire.Fire()
