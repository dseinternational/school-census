"""
Download and extract source data
"""

import os
import urllib.request
import zipfile
import config

data_files = {
    "sen-2023-24": "https://content.explore-education-statistics.service.gov.uk/api/releases/94886eb8-ba0e-45bc-a3a7-08dc65d0f8b2/files"
}

if not os.path.exists(config.DATA_DIR_NAME):
    os.makedirs(config.DATA_DIR_NAME)

for name, url in data_files.items():
    filename = f"{config.DATA_DIR_NAME}/{name}.zip"
    if not os.path.exists(filename):
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, filename)
    try:
        with zipfile.ZipFile(filename, mode="r", allowZip64=True) as archive:
            archive.extractall(f"{config.DATA_DIR_NAME}/sen-2023-24")
    except zipfile.BadZipFile as error:
        print(f"Error extracting {filename}: {error}")
