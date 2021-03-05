"""The example of Context manager
"""
from contextlib import contextmanager


# regular open file
def regular_open_file(file_path):
    f = open(file_path, "w")
    try:
        f.write("maybe can write something that i not really understand.")
        pass
    except Exception:
        raise
    finally:
        f.close()


# used context manager to open file
def contextmanager_example1(file_path):
    with open(file_path, "w") as f:
        f.write("maybe can write something that related with contextmanager_example1.")


# handmade context manager
class File:
    def __init__(self, file_path, mode):
        self.fpath = file_path
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.fpath, self.mode)
        return self.open_file

    def __exit__(self, tpye, val, traceback):
        print(f"Closing file: {self.fpath}")
        self.open_file.close()


# another handmade context manager
@contextmanager
def open_file(fpath, mode):
    try:
        f = open(fpath, mode)
        yield f
        f.close()
    except Exception:
        raise

# example of handmade context manager 
def contextmanager_example2(file_path):
    with open_file(file_path, "w") as f:
        f.write("write to test context manager decorator.")
