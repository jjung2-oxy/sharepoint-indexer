from microsoft_graph import GraphClient
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, SITE_ID

class SharePointClient:
    def __init__(self):
        self.client = GraphClient(tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    def get_folder_items(self, folder_id):
        return self.client.drives[SITE_ID].items[folder_id].children.get().value

    def get_file_content(self, file_id):
        return self.client.drives[SITE_ID].items[file_id].content.get().content

    def update_file_metadata(self, file_id, metadata):
        self.client.drives[SITE_ID].items[file_id].patch(body={
            "fields": {
                "ChunksAndEmbeddings": str(metadata)
            }
        })