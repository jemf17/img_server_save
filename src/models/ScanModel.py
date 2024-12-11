from uuid import UUID
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path
from fastapi.responses import FileResponse

class ScanModel():
    @classmethod
    def add(self, id_obra: UUID, scan: UUID, pags, portada):
        try:
            load_dotenv()
            scan_rute = os.getenv('SCAN_RUTE')
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def update(self, id_obra: UUID,scan: UUID, pags, portada):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def delete(self, id_obra: UUID, scan: UUID):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def get(self, id_obra: UUID, scan: UUID, page: int):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
        
