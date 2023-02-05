Minimd
======

Minimal markdown parser.

https://pypi.org/project/minimd/

Tokenize some markdown tags from text files.

## Installation

Install `minimd` library by running `pip install minimd`.

## Usage

Extract token from a markdown file.

```pycon
>>> import minimd
>>> with open('docs/doc1.md') as f:
...     for token in minimd.tokenize_file(f):
...         print(token)
... 
Token.TITLE('# First title\n', level=1)
Token.AFTER_TITLE(level=1)
Token.LINE('\n')
Token.LINE('* Bullet point\n')
Token.LINE('\n')
Token.START_CODE('```python\n', language='python', skip=False)
Token.LINE('def example_function():\n')
Token.LINE("    print('foo')\n")
Token.END_CODE('```\n')
```

Or for an iterable of files (tokens are added to separate files).

```pycon
>>> import minimd
>>> with open('docs/doc1.md') as f1, open('docs/doc2.md') as f2:
...     for token in minimd.tokenize_files([f1, f2]):
...         print(token)
... 
Token.FILE()
Token.TITLE('# First title\n', level=1)
Token.AFTER_TITLE(level=1)
Token.LINE('\n')
Token.LINE('* Bullet point\n')
Token.LINE('\n')
Token.START_CODE('```python\n', language='python', skip=False)
Token.LINE('def example_function():\n')
Token.LINE("    print('foo')\n")
Token.END_CODE('```\n')
Token.AFTER_FILE()
Token.FILE()
Token.TITLE('# Second title\n', level=1)
Token.AFTER_TITLE(level=1)
Token.LINE('\n')
Token.TITLE('## Subtitle\n', level=2)
Token.AFTER_TITLE(level=2)
Token.LINE('\n')
Token.LINE('Hello World!\n')
Token.AFTER_FILE()
```

Test input files are saved in [docs](https://github.com/entwanne/minimd/tree/master/docs/) directory.

There is also a `minimd` entrypoint to see how is tokenized a set of files.

```shell
% minimd docs/*.md
Token.FILE()
Token.TITLE('# First title\n', level=1)
Token.AFTER_TITLE(level=1)
Token.LINE('\n')
Token.LINE('* Bullet point\n')
Token.LINE('\n')
Token.START_CODE('```python\n', language='python', skip=False)
Token.LINE('def example_function():\n')
Token.LINE("    print('foo')\n")
Token.END_CODE('```\n')
Token.AFTER_FILE()
Token.FILE()
Token.TITLE('# Second title\n', level=1)
Token.AFTER_TITLE(level=1)
Token.LINE('\n')
Token.TITLE('## Subtitle\n', level=2)
Token.AFTER_TITLE(level=2)
Token.LINE('\n')
Token.LINE('Hello World!\n')
Token.AFTER_FILE()
```

## Development

### Environment

Use `pip install -e '.[dev]'` to install `minimd` with development dependencies (tests & lint).

### Contributing

Code of the project is managed on <https://github.com/entwanne/minimd/> git repository.

### Building & deploying a new version

You need to install `twine` package (`pip install twine`) to be able to deploy a version of the library.

You can use `python setup.py sdist` to build the current version of the package.

Then you can deploy this version to PyPI by running `twine upload dist/*`.
