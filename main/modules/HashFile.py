"""
This module creates a SHA256 hash for files or whole directories.
A hash is like a unique fingerprint for a file.

Why it's useful:
Checking file hashes helps:

identify whether files have been modified

detect tampering by attackers

preserve evidence integrity for forensic analysis

Example real-world use:

Check if critical system files were changed

Confirm that collected evidence files were not altered

Detect modified binaries or scripts

"""


import hashlib
from pathlib import Path

class HashFile:
    # This module creates SHA256 hashes for files.

    def hash_file(self, file_path):
        file_path = Path(file_path)

        if not file_path.exists():
            return "File not found"

        h = hashlib.sha256()

        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                h.update(chunk)

        return h.hexdigest()

    def hash_folder(self, folder_path):
        folder_path = Path(folder_path)
        results = {}

        for f in folder_path.rglob("*"):
            if f.is_file():
                results[str(f)] = self.hash_file(f)

        return results
