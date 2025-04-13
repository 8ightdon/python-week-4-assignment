def read_and_process_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Process: Convert content to lowercase and add line numbers
        lines = content.splitlines()
        modified_lines = [f"{i + 1}: {line.lower()}" for i, line in enumerate(lines)]
        modified_content = "\n".join(modified_lines)
        
        # Write modified content to a new file
        output_filename = "modified_output.txt"
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"✅ Successfully read '{filename}' and wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_process_file()
