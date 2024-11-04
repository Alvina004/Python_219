def read_file():
    while True:
        filename = input("Enter the name of the file you want to open: ")
        try:
            file = open(filename, 'r') 
            content = file.read()
            print(f"\nFile content:{content}")
            file.close() 
            return filename
        except FileNotFoundError:
            print("Error: The file doesn't exist. Please enter a valid filename.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid filename.")

def write_file(filename=None):
    if filename:
        choice = input("\nDo you want to write to the same file? (yes/no): ")
    else:
        choice = "no"

    if choice == "no":
        filename = input("Enter the name of the new file to write to: ")

    content = input("Enter the content you want to write to the file: ")

    try:
        file = open(filename, 'w')  
        file.write(content)    
    except FileNotFoundError:
        print("Error: Could not find or create the file. Please check the filename.")
    except Exception:  
        print("An unexpected error occurred.")
    else:
        print("Writing successful.")
    finally:
        file.close()  
        print("File operation completed.")

def main():
    filename = read_file()
    if filename:
        write_option = input("\nWould you like to write to a file? (yes/no): ")
        if write_option == "yes":
            write_file(filename)

if __name__ == "__main__":
    main()
