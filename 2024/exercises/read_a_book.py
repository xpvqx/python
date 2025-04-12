# Read a Book

# Download a free text version of Pride and Predejudice from Project Gutenberg

with open('pride_and_prejudice.txt', encoding='utf-f8') as f:
    word_count = 0
    for row in f:
        line_lst = row.strip().split()
        word_count += len(line_lst)
    print('Number of words:', word_count)
    