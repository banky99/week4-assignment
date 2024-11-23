def read_and_modify_file():
    # prompt to  input filename
    filename = input("Enter the filename to read from: ")

    try:
        # Try to open the input file
        with open(filename, 'r') as file:
            # Read the file content
            content = file.read()
            
            # Example modification: Convert content to uppercase
            modified_content = content.upper()
            
            # Ask for the output filename
            output_filename = input("Enter the filename to write the modified content to: ")
            
            # Write the modified content to a new file
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                
            print(f"Content successfully read from '{filename}' and written to '{output_filename}'.")
    
    except FileNotFoundError:
        # Error handling for a file that doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        # General error handling for file reading issues
        print(f"Error: Unable to read from the file '{filename}'.")

# Call the function
read_and_modify_file()
