from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from openai import AzureOpenAI
from config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_AI_ENDPOINT, AZURE_AI_KEY

class AzureAIClient:
    def __init__(self):
        self.text_analytics_client = TextAnalyticsClient(
            endpoint=AZURE_AI_ENDPOINT, 
            credential=AzureKeyCredential(AZURE_AI_KEY)
        )
        self.openai_client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2023-05-15",
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )

    def chunk_text(self, text):
        response = self.text_analytics_client.extract_key_phrases(documents=[text])
        # This is a simple approach. You might want to implement a more sophisticated chunking strategy.
        return response[0].key_phrases

    def get_embedding(self, text):
        response = self.openai_client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding