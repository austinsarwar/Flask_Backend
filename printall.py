import os

def print_directory_structure(rootdir, indent=0):
    for item in os.listdir(rootdir):
        path = os.path.join(rootdir, item)
        print(' ' * indent + '|-- ' + item)
        if os.path.isdir(path):
            print_directory_structure(path, indent + 4)

# Replace '.' with the path to your main application directory
print_directory_structure('.')
