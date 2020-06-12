import os
import subprocess
import tempfile


def make_pdf(
    problems: str, answers: str, output_path: str, include_answers: bool
) -> None:
    if include_answers:
        pdf_jobs = (("problems", problems), ("answers", answers))
    else:
        pdf_jobs = ("problems", problems)

    for job_name, job in pdf_jobs:

        if job_name == "answers":
            path, filename = os.path.split(output_path)
            new_filename = f"{filename.split('.pdf')[0]}-answers.pdf"
            output_path = os.path.join(path, new_filename)

        with tempfile.NamedTemporaryFile(mode="w") as txt_file:
            txt_file.write(job)
            txt_file.flush()

            command = (
                f"enscript --columns=4 --no-header --output=tempfile.ps {txt_file.name}"
            )
            print(f"command: '{command}'")

            output = subprocess.check_output(command, shell=True)
            print(output)

            command = f"ps2pdf tempfile.ps {output_path}"
            print(f"command: '{command}'")

            output = subprocess.check_output(command, shell=True)
            print(output)
        print("made pdf", output_path)
        os.unlink("tempfile.ps")
