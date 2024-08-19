from sharepoint_client import SharePointClient
from azure_ai_client import AzureAIClient

class SharePointIndexer:
    def __init__(self):
        self.sharepoint_client = SharePointClient()
        self.azure_ai_client = AzureAIClient()

    def process_folder(self, folder_id):
        items = self.sharepoint_client.get_folder_items(folder_id)
        
        for item in items:
            if hasattr(item, 'file'):
                self.process_file(item.id)

    def process_file(self, file_id):
        content = self.sharepoint_client.get_file_content(file_id)
        text_content = content.decode('utf-8')
        
        chunks = self.azure_ai_client.chunk_text(text_content)
        embeddings = [self.azure_ai_client.get_embedding(chunk) for chunk in chunks]
        
        metadata = {
            "chunks": chunks,
            "embeddings": embeddings
        }
        
        self.sharepoint_client.update_file_metadata(file_id, metadata)