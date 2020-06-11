import sys

from app.generate import generate_answers, generate_problems
from config import BEGIN_ANSWERS_TOKEN


def main():
    if len(sys.argv) < 3:
        print(
            "please supply the number of bits and the number of exercises you'd like, "
            "space-separated, like so:\n\n    $ binary 8 100\n"
        )
        sys.exit()

    bits = int(sys.argv[1])
    num_problems = int(sys.argv[2])

    problems = generate_problems(bits, num_problems)
    answers = generate_answers(problems)

    problems_string = "\n\n".join(problems)
    answers_string = "\n\n".join(
        [f"{problem} | {answer} " for problem, answer in zip(problems, answers)]
    )

    sys.stdout.write(BEGIN_ANSWERS_TOKEN.join((problems_string, answers_string)))
    return problems_string, answers_string
