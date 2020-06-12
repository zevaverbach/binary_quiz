import sys

import click
from click import ClickException

from app.generate import generate_answers, generate_problems
from app.config import BEGIN_ANSWERS_TOKEN
from app.pdf import make_pdf


@click.command()
@click.argument("bits", type=click.INT)
@click.argument("num-problems", type=click.INT)
@click.option("--pdf", default=False, is_flag=True)
@click.option("--silent", default=False, is_flag=True)
@click.option("--include-answers", default=True, is_flag=True)
@click.option("--output-filepath")
def main(
    bits: int,
    num_problems: int,
    pdf: bool = False,
    silent: bool = False,
    include_answers: bool = True,
    output_filepath: str = None,
) -> None:

    if pdf and silent:
        raise ClickException(
            "please specify either `pdf` or `silent`, not both (otherwise there "
            "won't be any outcome of running the app!"
        )

    if pdf and output_filepath and not output_filepath.endswith("pdf"):
        raise ClickException("Please include an output filepath ending in '.pdf'")

    problems = generate_problems(bits, num_problems)
    answers = generate_answers(problems)

    problems_string = "\n\n".join(problems)
    answers_string = "\n\n".join(
        [f"{problem} | {answer} " for problem, answer in zip(problems, answers)]
    )

    if pdf:
        make_pdf(
            problems=problems_string,
            answers=answers_string,
            output_path=output_filepath or "problems.pdf",
            include_answers=include_answers,
        )

    if not silent:
        if include_answers:
            click.echo(BEGIN_ANSWERS_TOKEN.join((problems_string, answers_string)))
        else:
            click.echo(problems_string)
