import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import config

class GoogleDocsReader:
    def __init__(self):
        creds_file = os.path.join(os.path.dirname(__file__), 'credentials.json')
        self.credentials = service_account.Credentials.from_service_account_file(
            creds_file,
            scopes=['https://www.googleapis.com/auth/documents.readonly']
        )
        self.service = build('docs', 'v1', credentials=self.credentials)

    async def get_text(self, document_id: str) -> str:
        doc = self.service.documents().get(documentId=document_id).execute()
        text = []
        for elem in doc.get('body', {}).get('content', []):
            if 'paragraph' in elem:
                for para in elem['paragraph']['elements']:
                    if 'textRun' in para:
                        text.append(para['textRun']['content'])
        return ''.join(text).strip()