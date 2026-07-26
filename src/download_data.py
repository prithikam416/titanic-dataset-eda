import os
import urllib.request

def download_titanic():
    # Make data directory
    os.makedirs("data", exist_ok=True)
    
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    output_path = "data/titanic.csv"
    
    print(f"[INFO] Downloading Titanic dataset from {url}...")
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"[SUCCESS] Dataset saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to download dataset: {e}")

if __name__ == "__main__":
    download_titanic()
