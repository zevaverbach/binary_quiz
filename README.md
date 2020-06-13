# Binary Math Exercises

## Description

A command line application and Python library for generating binary numbers for a human to decode, as well as generating the integers they represent, to check the human's work.

## Compatibility

Currently only supported on MacOS and Linux

## Installation on MacOS or Linux
1) `git clone https://github.com/Averbach-Transcription/email_quote`
2) `ln -s <repo_fullpath>/app/get_quote /usr/local/bin/`
3) brew install ghostscript ([install homebrew](https://brew.sh) if needed)
4) brew install enscript

## Usage
```
binary [OPTIONS] BITS NUM_PROBLEMS

Options:
  --pdf
  --silent
  --include-answers
  --output-filepath TEXT
  --help                  Show this message and exit.

```

## Examples of Output

### PDF

```binary 8 100 --pdf```

👆👆 this command produces two PDFs like this 👇👇

[![example of problems.pdf output](https://github.com/zevaverbach/binary_quiz/blob/master/examples/problems.png)](https://github.com/zevaverbach/binary_quiz/blob/master/examples/problems.pdf)
[![example of problems-answers.pdf output](https://github.com/zevaverbach/binary_quiz/blob/master/examples/problems-answers.png)](https://github.com/zevaverbach/binary_quiz/blob/master/examples/problems-answers.pdf)

## TODO
- add nice spacing and typography for easy reading
- pdf options
  - problem numbers [true]
  - number of columns [auto]
  - font
  - include column labels
  - print
- addition
- subtraction
- mult? div?
- hex?

### Other Projects That Could Depend On This
- do the problems online/on computer
- a website to serve these up and let people use them for free
  - a web API that serves it, so people can do that programmatically
  - a snail mail service?
    - https://developers.lulu.com/price-calculator
  - if there's going to be exercises in the browser,
    - parseInt('0101', 2)
  - maybe re-implement in Javascript so all computation and rendering is done on the client
    - [PDF rendering in the browser](https://pspdfkit.com/blog/2018/render-pdfs-in-the-browser-with-pdf-js/)
