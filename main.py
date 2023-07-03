from flask import Flask, Response, json

from cv_data import cv_text

MINIMUM_LINES_CV = 5


def print_message_before_app_run() -> None:
    print('Welcome to my CV. You can access the following REST JSON in browser or with curl'
          '\n1. http://127.0.0.1:5000/personal for personal information'
          '\n2. http://127.0.0.1:5000/experience for experience information'
          '\n3. http://127.0.0.1:5000/education for education information'
          )


# Create the Flask App
app = Flask(__name__)

# Print a welcome message
print_message_before_app_run()

sections = {
    'personal': [],
    'experience': [],
    'education': [],
}


def parse_cv_text(text: str) -> None:
    """
    Algorithm:
    Input: a Curriculum Vitae (CV) via a multi line string.
    Given the sections (private, experience, education), we iterate over each line of the CV,
    if one of the line is exactly a match to the sections - in lowercase, we mark as found the current section;
    the first section, by default, is "personal", any line after a section is the section string data
    - we append them as an array

    Assumptions:
    1. We have a string with multiple lines
    2. A section, by definition, is a word, in lower case, matching a full line
    2. The first section is assumed 'personal' by default
    3. There are optionally other sections in the string, different from 'personal'
    4. There are at least MINIMUM_LINES_CV lines in the CV

    Output:
    We alter a global Dict[section_name:Array] called sections

    :param text: Input CV data
    :exception If the number of lines in the CV is <= than the MINIMUM_LINES_CV constant, it throws
    :return: None
    """
    if len(text.split('\n')) <= MINIMUM_LINES_CV:
        raise Exception(f'The CV contains only {MINIMUM_LINES_CV} lines of text, are you sure this is a valid CV?')

    sections_keys = list(sections.keys())
    current_section = 'personal'  # default section

    # loop through the text by lines
    for line in text.split('\n'):
        # clean the line
        line = line.strip()

        if line.lower() in sections_keys:
            current_section = line.lower()
        elif line:
            sections[current_section].append(line)


# Parse the CV text
parse_cv_text(text=cv_text)


@app.route('/personal', methods=['GET'])
def personal():
    return Response(
        json.dumps({'Personal': sections['personal']}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )


@app.route('/experience', methods=['GET'])
def experience():
    return Response(
        json.dumps({'Experience': sections['experience']}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )


@app.route('/education', methods=['GET'])
def education():
    return Response(
        json.dumps({'Education': sections['education']}, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )


if __name__ == '__main__':
    """
    This app will create a REST JSON server on 127.0.0.1 with the following endpoints:
    
    /personal
    /experience
    /education
    
    Based on a Curriculum Vitae.
    
    The input for this script is a text string contained in the cv_text variable.
    
    By parsing the text with the parse_cv_text function, we get the following structure:
    1. For /personal : Dictionary["Personal":Array[strings]]
    2. For /experience : Dictionary["Experience":Array[strings]]
    3. For /education : Dictionary["Education":Array[strings]]
    
    For example:
    {
        "Personal": [
            "first_name last_name",
            "email telephone",
            "linkedin_url",
            "Summary",
            "summary_data"
        ]
    }
    """

    app.run(debug=True)
