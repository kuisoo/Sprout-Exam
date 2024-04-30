# Sprout-Exam
##### Requirements
Python
##### Clone repository
`git clone https://github.com/kuisoo/Sprout-Exam.git`
##### Go to the repository directory
`cd Sprout-Exam`
##### [OPTIONAL] Create a virtual environment to isolate installed packages
`python -m venv .venv`
##### [OPTIONAL] Activate virtual environment check https://docs.python.org/3/library/venv.html
For windows: `.\.venv\Scripts\activate` 
##### Install packages
`pip install -r requirements.txt`
##### Start uvicorn server 
`uvicorn main:app --reload`
##### Access the FastAPI endpoints documentation
`<uvicorn server address>/docs`
example: http://127.0.0.1:8000/docs
# Improvements priority
Added login security, token timeouts, etc.
Employee search and sort functionality.
Function to add employee type and corresponding attributes.
Function to add benefits on the list of available benefits.
