''' FileStats related classes'''

class FileStatsException(Exception):
    ''' Exception class for anything related to FileStats'''
    pass


class FileStats(object):
    ''' FileStats class calculates some metrics from a given file'''
    def __init__(self, curr_file):
        if not curr_file:
            raise FileStatsException
        self.curr_file = curr_file

    def count_lines(self):
        ''' returns the number of lines in the current file'''
        with open(self.curr_file) as open_file:
            contents = open_file.readlines()
        return len(contents)

    def count_chars(self):
        ''' returns the number of characters in the current file'''
        with open(self.curr_file) as open_file:
            contents = open_file.read()
        return len(contents)
