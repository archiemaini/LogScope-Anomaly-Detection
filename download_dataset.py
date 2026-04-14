import urllib.request
import os

def download_hdfs_dataset():
    url = "https://raw.githubusercontent.com/logpai/loghub/master/HDFS/HDFS_2k.log_structured.csv"
    filename = "HDFS_2k.log_structured.csv"
    
    print(f"Downloading {filename} from {url}...")
    try:
        urllib.request.urlretrieve(url, filename)
        if os.path.exists(filename):
            print(f"Successfully downloaded {filename}.")
        else:
            print("Download failed.")
    except Exception as e:
        print(f"An error occurred during download: {e}")

if __name__ == "__main__":
    download_hdfs_dataset()
