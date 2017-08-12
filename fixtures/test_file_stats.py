import os
import pytest

from file_stats import FileStats, FileStatsException

@pytest.fixture
def empty_file():
	filename = "empty_file.txt"
	open(filename, 'w').close()
	yield filename
	os.remove(filename)

@pytest.fixture
def lines2_chars4_file():
	filename = "non_empty_file.txt"
	with open(filename, "w") as open_file:
		open_file.write("1\n")
		open_file.write("2\n")
	yield filename
	os.remove(filename)
	

def test_no_given_file():
	with pytest.raises(FileStatsException):
		FileStats(None)

def test_lines_empty_file(empty_file):
	fs = FileStats(empty_file)
	assert fs.count_lines() == 0

def test_chars_empty_file(empty_file):
	fs = FileStats(empty_file)
	assert fs.count_chars() == 0

def test_lines_non_empty_file(lines2_chars4_file):
	fs = FileStats(lines2_chars4_file)
	assert fs.count_lines() == 2

def test_chars_non_empty_file(lines2_chars4_file):
	fs = FileStats(lines2_chars4_file)
	assert fs.count_chars() == 4
