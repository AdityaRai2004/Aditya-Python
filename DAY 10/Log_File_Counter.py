## Log File Analyzer
def analyze_log_file(input_file="server.log", output_file="errors_only.log"):
    error_count = 0
    error_lines = []
    
    try:
        with open(input_file, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                    error_lines.append(line)
                    
        with open(output_file, 'w') as file:
            file.writelines(error_lines)
            
        print(f"Found {error_count} ERROR occurrences")
        print(f"Error lines written to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

analyze_log_file()
