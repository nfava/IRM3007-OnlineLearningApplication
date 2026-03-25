### IRM3007 
# Online Learning System
An online learning system focused on increasing transparency.

## Features
### Students can:
- View assignments, deadlines, and course materials.
- GPA converter (12.0 ↔ 4.0 ↔ Percentage).
- Final grade tracker with real-time updates.
- Visual progress indicators for assignments and grading status.
### Professors can:
- Create and manage assignments.
- Upload instructions and resources.
- View and grade student submissions.
- Update grading status (e.g. Not Started → In Progress → Reviewed → Released).
### Grade transparency:
- Real-time grading status visibility for students.
- Progress tracking (e.g. current stage of the grading process).
- Expected grading completion timelines.
- Display of grader (TA or Professor).
- Optional feedback and rubric-based comments.

<img width="1865" height="690" alt="image" src="https://github.com/user-attachments/assets/1c8c03ab-eb5a-4287-b676-704ec9843cbe" />

## Installation
1. **Make sure you have Python and Git installed.**
2. Clone this repository either by using the command line or using PyCharm's built in repository cloner:
`$ git clone https://github.com/nfava/IRM3007-OnlineLearningApplication.git`
3. Once you have properly installed the project, open it up in PyCharm and a pop-up should appear telling you to create a virtual environment, just click OK.
   
![create-virtual-environment](https://github.com/user-attachments/assets/3c2e0cdc-727b-455b-8097-291a44c62864)

4. Next, type `pip install -r requirements.txt` into the terminal to install the requirements of the project.
5. Create a file called `.env` in the top level directory (should be in the same folder as manage.py)
6. In the terminal, run `python manage.py migrate`
7. Run the server by clicking the play button or running `python manage.py runserver` in the terminal
8. Navigate to 127.0.0.1:8000! The project should be running in your web browser.
