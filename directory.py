import os

# Create a directory
def create_dir(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")

# Change directory
def change_dir(dir_name):
    os.chdir(dir_name)
    print(f"Current directory changed to: {os.getcwd()}")

# List directory contents
def list_dir():
    print(os.listdir())

# Remove a directory
def remove_dir(dir_name):
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")

# Get current working directory
def get_cwd():
    print(os.getcwd())

# Example usage
create_dir("my_dir")
change_dir("my_dir")
list_dir()
get_cwd()
# change_dir("..")  # Move back to parent directory
# remove_dir("my_dir")