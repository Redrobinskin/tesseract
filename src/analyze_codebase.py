```python
import os
import pipreqs

def analyze_codebase(project_directory):
    # Analyze the codebase and return a list of dependencies
    dependency_list = pipreqs.get_all_imports(project_directory)
    return dependency_list

def generate_requirements(dependency_list):
    # Generate requirements.txt file
    with open('./requirements.txt', 'w') as f:
        for dependency in dependency_list:
            f.write(f"{dependency}\n")

def write_readme(dependency_list):
    # Write README.md file
    installation_instructions = "\n".join([f"pip install {dependency}" for dependency in dependency_list])
    with open('./README.md', 'w') as f:
        f.write("# Project Installation Instructions\n")
        f.write("## Requirements\n")
        f.write("Install the following dependencies:\n")
        f.write(f"```\n{installation_instructions}\n```\n")

if __name__ == "__main__":
    project_directory = os.getcwd()
    dependency_list = analyze_codebase(project_directory)
    generate_requirements(dependency_list)
    write_readme(dependency_list)
```