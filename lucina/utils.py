import contextlib


@contextlib.contextmanager
def open_files(filenames, *args, **kwargs):
    with contextlib.ExitStack() as stack:
        yield [
            stack.enter_context(open(filename, *args, **kwargs))
            for filename in filenames
        ]
