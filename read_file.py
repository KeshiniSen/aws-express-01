def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at {file_path}.")

# Replace 'sample.txt' with the path to your file
file_path = '/Users/keshinisen/Documents/GitHub/aws-express-01/sample.txt'
read_and_print_file(file_path)
