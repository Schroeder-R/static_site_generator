import os
import shutil

def copy_contents(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination) # Delete all contents of the destination directory
    os.mkdir(destination)

    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        if os.path.isdir(source_item):
            # Recursive call for directories
            copy_contents(source_item, destination_item)
        else:
            # Copy files
            shutil.copy(source_item, destination_item)
            print(f"Copied file: {source_item} to {destination_item}")

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_dir = os.path.join(root_dir, "static")
    destination_dir = os.path.join(root_dir, "public")
    copy_contents(source_dir, destination_dir)
    
if __name__ == "__main__":
    main()


