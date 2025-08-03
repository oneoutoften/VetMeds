from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = r'D:\VetMeds\vetbot\app\google_parser\credentials.json'

def authenticate():
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

class GoogleDocsReader:
    def __init__(self):
        self.creds = authenticate()
        self.service = build('docs', 'v1', credentials=self.creds)

    def get_text(self, document_id: str) -> str:
        print(f"Попытка получить текст из документа с ID: {document_id}")
        try:
            doc = self.service.documents().get(documentId=document_id).execute()
            text = []
            for elem in doc.get('body', {}).get('content', []):
                if 'paragraph' in elem:
                    for para in elem['paragraph']['elements']:
                        if 'textRun' in para:
                            text.append(para['textRun']['content'])
            print('Success')
            return ''.join(text).strip()
        except HttpError as error:
            print(f"Ошибка при получении текста: {error}")
            raise
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            raise