from app.generate import generate, generate_problems
from app.check import check


def test_generate():
    first_problem = generate(bits=5)
    assert len(first_problem) == 5
    assert all(char in ("1", "0") for char in first_problem)
    assert "1" in first_problem
    assert "0" in first_problem


def test_generate_problems():
    problems = generate_problems(bits=5, num_problems=100)
    first_problem = problems[0]
    assert len(problems) == 100
    assert len(first_problem) == 5
    assert all(char in ("1", "0") for char in first_problem)


def test_check():
    assert check("110") == 6
    assert check("000") == 0
    assert check("001") == 1
    assert check("011") == 3
    assert check("010") == 2
