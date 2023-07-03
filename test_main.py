import pytest

from main import sections, parse_cv_text, MINIMUM_LINES_CV


def test_parse_cv_text():
    # Set up
    sections.clear()
    sections.update({'personal': [], 'experience': [], 'education': []})
    input_text = 'John Doe\n25 years old\nexperience\nDeveloper at XYZ\neducation\nB.S. in Computer Science'

    # Call function
    parse_cv_text(input_text)

    # Asserts
    assert sections['personal'] == ['John Doe', '25 years old']
    assert sections['experience'] == ['Developer at XYZ']
    assert sections['education'] == ['B.S. in Computer Science']


def test_parse_cv_text_few_lines():
    # Set up
    sections.clear()
    sections.update({'personal': [], 'experience': [], 'education': []})
    input_text = 'John Doe\n25 years old'

    # Call function and check exception
    with pytest.raises(Exception) as excinfo:
        parse_cv_text(input_text)

    assert str(
        excinfo.value) == f'The CV contains only {MINIMUM_LINES_CV} lines of text, are you sure this is a valid CV?'


def test_parse_cv_text_skip_empty_lines():
    # Set up
    sections.clear()
    sections.update({'personal': [], 'experience': [], 'education': []})
    input_text = 'John Doe\n\n\nexperience\nDeveloper at XYZ\n\neducation\nB.S. in Computer Science'

    # Call function
    parse_cv_text(input_text)

    # Asserts
    assert sections['personal'] == ['John Doe']
    assert sections['experience'] == ['Developer at XYZ']
    assert sections['education'] == ['B.S. in Computer Science']
