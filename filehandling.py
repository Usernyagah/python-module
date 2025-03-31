filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except IsADirectoryError:
    print(f"Error: '{filename}' is a directory, not a file.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
else:
    # Modify the content (convert to uppercase)
    modified_content = content.upper()
    
    # Create new filename manually
    last_dot = filename.rfind('.')
    if last_dot == -1:
        base_name = filename
        extension = ''
    else:
        base_name = filename[:last_dot]
        extension = filename[last_dot:]
    
    new_filename = f"{base_name}_modified{extension}"
    
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content successfully written to '{new_filename}'")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
