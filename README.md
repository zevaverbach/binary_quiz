# Binary Math Exercises

## Description

A command line application and Python library for generating binary numbers for a human to decode, as well as generating the integers they represent, to check the human's work.

## Installation on MacOS or Linux
1) `git clone https://github.com/Averbach-Transcription/email_quote`
2) `ln -s <repo_fullpath>/app/get_quote /usr/local/bin/`

## Usage
```make_binary_problems <number_of_bits: integer> <number_of_problems: integer>```

## TODO
- add installation of ghostscript as a prereq
  - brew install ghostscript or...?
- add installation of enscript
- use click to make it a proper CLI, now that there will be multiple options
- make it produce printable sheets, probably as PDFs
  - add nice spacing for easy reading
  - "enscript --columns=4 --output=file --no-header ~/tempfile.ps ~/tempfile.txt"
  - "ps2pdf ~/tempfile.ps ~/problems_and_answers.pdf"

  - options
    - create_pdf
      - number of columns [auto]
      - font
      - include column labels

### Other Projects That Could Depend On This
- do the problems online/on computer
- a website to serve these up and let people use them for free
  - a web API that serves it, so people can do that programmatically
