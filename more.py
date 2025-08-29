# File Read & Write Challenge with Error Handling
def process_file():
    # Ask user for input filename
    input_filename = input("Enter the input filename (e.g., input.txt): ")

    try:
        # Read the contents of the input file
        with open(input_filename, "r") as input_file:
            content = input_file.read()

        # Convert content to uppercase
        modified_content = content.upper()

        # Create output filename by appending '_modified' to the input filename
        output_filename = input_filename.rsplit(".", 1)[0] + "_modified.txt"

        # Write modified content to a new file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"Success! Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    process_file()