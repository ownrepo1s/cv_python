# What
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

# Why?
Interview task

# How?
1. Clone this repository with `git clone https://github.com/ownrepo1s/cv_python.git`
2. Open the root repository
3. Run the command `flask run`
4. You will get the output:
```
Welcome to my CV. You can access the following REST JSON in browser or with curl
1. http://127.0.0.1:5000/personal for personal information
2. http://127.0.0.1:5000/experience for experience information
3. http://127.0.0.1:5000/education for education information
 * Serving Flask app 'main.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
5. Browse the URLs or use `curl` to GET to access the endpoints

Have a nice day!
