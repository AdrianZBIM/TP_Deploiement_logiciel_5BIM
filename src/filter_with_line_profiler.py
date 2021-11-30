
words_to_remove = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by',
    'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
    'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with'
]


@profile
def filter_version1():
    for i in range(1000000): # To test the performance of the piece of code, we execute it many times.
        filtered_text = []
        for m in ['Mr.', 'Hat', 'is', 'feeding', 'the', 'black', 'cat', '.']:
            if m not in words_to_remove:
                filtered_text.append(m)


filter_version1()

