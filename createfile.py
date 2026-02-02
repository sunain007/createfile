import os
import random

def create_file(filename, size_mb):
    size_bytes = size_mb * 1024 * 1024
    with open(filename, 'wb') as f:
        # Write random bytes
        f.write(os.urandom(size_bytes))
    print(f"[+] Created file '{filename}' of size {size_mb} MB.")

if __name__ == "__main__":
    size_mb = int(input("Enter file size in MB: ").strip())
    ext = input("Enter file extension (e.g., pdf, jpg, php): ").strip().lstrip('.')
    filename = input("Enter file name (without extension): ").strip()

    full_filename = f"{filename}.{ext}"
    create_file(full_filename, size_mb)
