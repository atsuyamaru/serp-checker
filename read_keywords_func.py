def read_keywords_by_line_from_file(filename):
    with open(filename, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]
    return keywords