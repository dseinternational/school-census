import os
import urllib.request
import zipfile

data_files = {
    "2023-24": "https://content.explore-education-statistics.service.gov.uk/api/releases/94886eb8-ba0e-45bc-a3a7-08dc65d0f8b2/files"
}

if not os.path.exists("data"):
    os.makedirs("data")

for name, url in data_files.items():
    filename = "data/" + name + ".zip"
    if not os.path.exists(filename):
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, filename)
    try:
        with zipfile.ZipFile(filename, mode="r", allowZip64=True) as archive:
            archive.extractall("data")
    except zipfile.BadZipFile as error:
        print(f"Error extracting {filename}: {error}")
        