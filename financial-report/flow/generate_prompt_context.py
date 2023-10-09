from typing import List
from promptflow import tool
from promptflow_vectordb.core.contracts import SearchResultEntity

@tool
def generate_prompt_context(search_result: List[dict]) -> str:
    def format_doc(doc: dict):
        return f"Content: {doc['Content']}\nSource: {doc['Source']}"

    SOURCE_KEY = "source"
    URL_KEY = "url"

    retrieved_docs = []
    for item in search_result:

        entity = SearchResultEntity.from_dict(item)
        content = entity.text or ""

        source = ""
        if entity.original_entity is not None:
           source = entity.original_entity["url"] or ""

        retrieved_docs.append({
            "Content": content,
            "Source": source
        })
    doc_string = "\n\n".join([format_doc(doc) for doc in retrieved_docs])
    return doc_string
