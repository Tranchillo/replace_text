import os

# Current directory (the folder where the script is located)
directory = os.getcwd()

# Word or symbol to search for
old_text = "$"

# Word to replace the old text with
new_text = "USD"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()
        
        # Perform the replacement
        if old_text in file_data:
            file_data = file_data.replace(old_text, new_text)
            print(f"Modified file: {filename}")
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_data)

print("Operation completed.")
