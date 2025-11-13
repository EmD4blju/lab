import chromadb
from pprint import pprint


collection = None

def main():
    global collection
    
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name='my-documents',
        metadata={'hnsw:space': 'l2'}
    )
    collection.add(
        documents=[
            'Swimming strengthens the entire body while providing a refreshing escape from daily stress.',
            'Running clears the mind and builds endurance with every rhythmic stride.',
            'Gaming connects people worldwide through strategy, creativity, and shared adventures.',
            'Food brings people together, offering comfort, culture, and creativity in every bite.',
            'Music speaks the language of emotion, connecting hearts through rhythm and melody.',
            'Sport teaches discipline, teamwork, and the thrill of striving toward greatness.',
            'Queen',
            'King',
            'Ace'
        ],
        metadatas=[
            {'topic': 'sport'},
            {'topic': 'sport'},
            {'topic': 'gaming'},
            {'topic': 'food'},
            {'topic': 'music'},
            {'topic': 'sport'},
            {'topic': 'people'},
            {'topic': 'people'},
            {'topic': 'people'}
        ],
        ids=['doc1', 'doc2', 'doc3', 'doc4', 'doc5', 'doc6', 'doc7', 'doc8', 'doc9']
    )
    
    # document_idx -> metadata_idx -> ids_idx
    # document -> llm (feed instructions) -> topic 
    
def query_db(text:str):
    global collection
    
    return collection.query(
        query_texts=[text],
        n_results=3
    )
    
    
    
if __name__ == "__main__":
    main()
    pprint(query_db(
        text='Let us play cards!'
    ))