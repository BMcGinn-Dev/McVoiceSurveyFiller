import re




validation_code = "ValidationCode_1010234"








def extract_and_save_numbers(input_string):
    """
    Extract numbers from a formatted string and save them to a file named 'ValidationCode_#######.txt'.
    
    Args:
        input_string (str): The string containing the validation code.
    """
    # Use regex to find the numbers in the string
    match = re.search(r"\d+", input_string)
    
    if match:
        numbers = match.group()  # Extract the matched numbers
        print(f"Extracted numbers: {numbers}")
        
        # Dynamically name the file based on the extracted numbers
        file_name = f"ValidationCode_{numbers}.txt"
        
        # Write the numbers to the dynamically named file
        with open(file_name, "w") as file:
            file.write(numbers)
        
        print(f"Numbers saved to {file_name}")
    else:
        print("No numbers found in the input string.")