import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("bahramjannesarr/goodreads-book-datasets-10m")

print("Path to dataset files:", path)

# Create local data folder
os.makedirs("data", exist_ok=True)

# Copy the specific file you need
source_file = os.path.join(path, "book700k-800k.csv")
destination_file = os.path.join("data", "book700k-800k.csv")

shutil.copy(source_file, destination_file)

print("Dataset copied to project data folder.")
