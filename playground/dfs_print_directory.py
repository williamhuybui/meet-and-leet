
import os
def dfs(root_path, depth):
    if not os.path.exists(root_path) or not os.path.isdir(root_path) or root_path.split(os.sep)[-1].startswith('.git'):
        return
    indent = "  " * depth
    print(f"{indent}{os.path.basename(root_path)}")
    if os.path.isdir(root_path):
        for item in os.listdir(root_path):
            item_path = os.path.join(root_path, item)
            dfs(item_path, depth + 1)

# Example usage:
root_directory = "."  # Change this to your directory path
dfs(root_directory, 0)
