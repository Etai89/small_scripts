import os

def start():
    while True:
        # Prompt user to enter search directory and filename
        search_dir = input("Enter the search directory: ")
        file_name = input("Enter the file name (without extension): ")

        # Walk through the directory and its subdirectories to find files with the given filename
        results = []
        for dirpath, dirnames, filenames in os.walk(search_dir):
            for filename in filenames:
                if filename.startswith(file_name):
                    results.append(os.path.join(dirpath, filename))
        
        # Print the results of the search
        if len(results) > 0:
            while True:
                print("Found {} file(s) with name '{}' in directory '{}' and its subdirectories:".format(len(results), file_name, search_dir))
                for i, result in enumerate(results):
                    print("{}. {}".format(i+1, result))

                # Prompt user to choose a file location to open
                chosen_index = input("Enter the number of the file location you would like to open or press Enter to start a new search: ")
                if not chosen_index:
                    break

                try:
                    chosen_index = int(chosen_index)
                    chosen_file = results[chosen_index-1]

                    # Open the location folder of the chosen file
                    location_folder = os.path.dirname(chosen_file)
                    print("Opening location folder: {}".format(location_folder))
                    os.startfile(location_folder)
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")
        else:
            print("No files found with name '{}' in directory '{}' and its subdirectories.".format(file_name, search_dir))

start()
