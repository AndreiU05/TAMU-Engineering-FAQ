<p align="center"><strong>TAMU Engineering FAQ Finder</strong></p>

This is a small Streamlit project I made to help Texas A&M engineering students find the right resource for common questions.

A lot of the questions students ask are about things that can change, like ETAM results, GPA reports, degree plans, professor grade distributions, schedules, and scholarships. I think it is better for this app to send students to the official source instead of trying to guess an answer.

This project is student-made and is not endorsed, owned, or operated by Texas A&M University.

## What It Does

The app lets a student type a question. Then it checks for common words and phrases, picks the best FAQ category, and sends back useful links.
It also checks for some common student shorthand, like `prof`, `profs`, `gpa distr`, `grade dist`, `sched`, `reg`, `syl`, `mech e`, and `auto admit`.

Examples:

- ETAM questions -> ETAM application and placement pages
- GPA or grade distribution questions -> TAMU Registrar grade reports
- Professor or class difficulty questions -> Anex for grade distributions by professor/class and Rate My Professors for reviews
- Degree plan questions -> Texas A&M Undergraduate Catalog
- Schedule or registration questions -> Howdy / Aggie Schedule Builder
- Syllabus questions -> Howdy course or section details
- Advising questions -> TAMU Engineering academic advisors
- Internship or resume questions -> Texas A&M Career Center

If the app does not find a direct match, it shows a few broad starting points instead of guessing.

## Tech Used

- Python
- Streamlit
- Basic keyword and phrase matching

There are no keys or environment files needed for this version.

## Requirements

- Python 3
- Streamlit Library
- A terminal or command prompt to run the app

The only installed Python library listed in `requirements.txt` is:

```text
streamlit>=1.36,<2
```

The app also uses Python's built-in `re` module for simple word and phrase matching.

## How To Run It

Install the packages:

```powershell
py -m pip install -r requirements.txt
```

Start the app:

```powershell
py -m streamlit run app.py
```

Streamlit usually opens this local address:

```text
http://localhost:8501
```

## Questions I Tested

- What is ETAM?
- Median GPA for engineering students?
- Engineering class grade distributions?
- Where can I find ETAM placement outcomes?
- Mechanical engineering degree plan
- Where is the syllabus for ENGR 102?
- Can you build my fall schedule?
- Which professor should I take?
- Grade distributions for different professors?
- gpa distr for profs
- sched for next sem
- where syl for ENGR 102?
- Who do I talk to if I am behind?
- How do I get an internship?

## Important Notes

This is a prototype for a class/personal project. It is not an official advising tool.

The app does not scrape live data. It routes students to official websites and common student resources.

Students should still check official TAMU pages or talk to an advisor before making academic decisions.

## Limitations

- The routing is based on simple keyword checks.
- It can miss questions if the wording is too different.
- If the wording is too unclear, the app gives broad starting links instead of guessing.
- Some links may need to be updated later if websites change.
- It is focused on TAMU Engineering, not every TAMU topic.

## What I Learned

- How to build a simple app with Python
- How to use Streamlit for the web page UI
- How to list project libraries in `requirements.txt`
- How to use Python's built-in `re` module for basic text matching
- How to organize resource links
- How to use Python functions for routing logic
- How to use dictionaries and lists to store app data
- Why official sources matter for changing academic information

## TODO

- Add more TAMU Engineering links.
- Add more FAQ categories.
- Add tests for the routing rules.
- Improve the keyword lists so it understands more student wording.
- Expand this idea into a larger context situation with AI + learn SQL and Databases
