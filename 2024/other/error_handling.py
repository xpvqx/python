# Error Handling
while True:
    try:
        file_name = input('file name: ')
        with open(file_name, 'r') as f:     # file must exist
            for row in f:
                pass                        # do the work here
        break
    except FileNotFoundError:
        print('File not found:', file_name)