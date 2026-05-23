import re

import streamlit as st


# ----------------------------
# App text
# ----------------------------

APP_TITLE = "TAMU Engineering FAQ Finder"
APP_DESCRIPTION = (
    "A student-made tool for finding the right TAMU Engineering resource. Type a question and the app "
    "will point you toward the best FAQ category or official website."
)

DISCLAIMER = (
    "Unofficial student project. Always confirm important academic information with official "
    "Texas A&M resources or an academic advisor."
)


# ----------------------------
# Resource data
# ----------------------------

# I keep all the websites in one dictionary so I only have to edit links in one place.
RESOURCES = {
    "etam_placement": {
        "title": "ETAM Placement Outcomes",
        "url": "https://engineering.tamu.edu/academics/undergraduate/entry-to-a-major/placement.html",
        "description": "Recent ETAM placement outcomes and major-by-major placement results.",
    },
    "etam_process": {
        "title": "ETAM Application Process",
        "url": "https://engineering.tamu.edu/academics/undergraduate/entry-to-a-major/application-preview.html",
        "description": "Official ETAM rules, required coursework, automatic entry, and application details.",
    },
    "registrar_reports": {
        "title": "TAMU Registrar Grade, GPA, and Cumulative GPA Reports",
        "url": "https://web-as.tamu.edu/gradereports/",
        "description": "Official university grade distribution, semester GPA, and cumulative GPA reports.",
    },
    "anex": {
        "title": "Anex Professor and Class Grade Distributions",
        "url": "https://anex.us/grades/",
        "description": "Use this to compare class grade distributions for different professors.",
    },
    "rate_my_professors": {
        "title": "Rate My Professors",
        "url": "https://www.ratemyprofessors.com/",
        "description": "Student reviews for specific professors.",
    },
    "catalog": {
        "title": "Texas A&M Undergraduate Catalog",
        "url": "https://catalog.tamu.edu/undergraduate/engineering/",
        "description": "Official degree plans, curriculum requirements, course descriptions, and catalog rules.",
    },
    "degrees": {
        "title": "TAMU Engineering Undergraduate Degrees",
        "url": "https://engineering.tamu.edu/academics/degrees/index.html",
        "description": "Current list of undergraduate engineering degree programs.",
    },
    "advisors": {
        "title": "TAMU Engineering Academic Advisors",
        "url": "https://engineering.tamu.edu/academics/undergraduate/academic-advisors.html",
        "description": "Official advising contacts for general engineering and department advising.",
    },
    "scholarships": {
        "title": "TAMU Engineering Scholarships",
        "url": "https://engineering.tamu.edu/admissions-and-aid/scholarships/index.html",
        "description": "Current engineering scholarship information, eligibility, and application guidance.",
    },
    "career_center": {
        "title": "Texas A&M Career Center",
        "url": "https://careercenter.tamu.edu/",
        "description": "Career advising, resume help, interview prep, internships, and employer events.",
    },
    "research": {
        "title": "TAMU Engineering Undergraduate Research",
        "url": "https://engineering.tamu.edu/academics/undergraduate/undergraduate-bridges.html",
        "description": "Undergraduate research pathways and official program information.",
    },
    "howdy": {
        "title": "Howdy / Aggie Schedule Builder",
        "url": "https://howdy.tamu.edu/",
        "description": "Scheduling, registration, section details, instructor listings, and syllabus links when available.",
    },
}


# ----------------------------
# FAQ matching categories
# ----------------------------

# Each category has words and phrases that students might type.
# The app gives points for matches and uses the highest scoring category.
CATEGORIES = [
    {
        "name": "Syllabus",
        "intro": "For syllabi, start here:",
        "resources": ["howdy"],
        "example": "Where is the syllabus for ENGR 102?",
        "phrases": ["where is the syllabus", "find syllabus", "course syllabus", "section syllabus"],
        "words": ["syllabus", "syllabi"],
    },
    {
        "name": "Professor Info",
        "intro": "For professor or class difficulty questions, check these:",
        "resources": ["anex", "rate_my_professors"],
        "example": "Which professor should I take?",
        "phrases": [
            "which professor",
            "which instructor",
            "who should i take",
            "rate my professor",
            "class is hard",
            "course is hard",
            "grade distribution by professor",
            "grade distributions by professor",
            "different professors",
            "compare professors",
            "professor grade distribution",
            "professor grade distributions",
            "professor gpa",
            "professors gpa",
            "professor grades",
            "professors grades",
            "easy professor",
            "hard professor",
            "best professor",
            "good professor",
            "bad professor",
        ],
        "words": [
            "professor",
            "prof",
            "instructor",
            "teacher",
            "professors",
            "instructors",
            "rmp",
            "review",
            "reviews",
            "compare",
            "distribution",
            "distributions",
            "easiest",
            "hardest",
        ],
    },
    {
        "name": "Schedule",
        "intro": "For scheduling and registration, use Howdy:",
        "resources": ["howdy", "advisors"],
        "example": "Can you build my fall schedule?",
        "phrases": [
            "build my schedule",
            "fall schedule",
            "spring schedule",
            "open seat",
            "time slot",
            "who teaches",
            "class time",
            "course registration",
            "registration time",
        ],
        "words": [
            "schedule",
            "registration",
            "register",
            "section",
            "sections",
            "seat",
            "seats",
            "time",
            "howdy",
        ],
    },
    {
        "name": "Degree Plan",
        "intro": "For degree plans and curriculum requirements, start here:",
        "resources": ["catalog", "howdy", "advisors"],
        "example": "Mechanical engineering degree plan",
        "phrases": [
            "degree plan",
            "degree plans",
            "what classes do i need",
            "classes do i need",
            "course catalog",
            "degree progress",
            "classes for my major",
            "courses for my major",
        ],
        "words": [
            "degree",
            "plan",
            "plans",
            "curriculum",
            "catalog",
            "requirements",
            "requirement",
            "courses",
            "classes",
            "credits",
            "flowchart",
            "flowcharts",
        ],
    },
    {
        "name": "ETAM",
        "intro": "For ETAM questions, start with these official pages:",
        "resources": ["etam_placement", "etam_process"],
        "example": "What is ETAM?",
        "phrases": [
            "entry to a major",
            "get into my major",
            "getting into my major",
            "worried about getting into",
            "automatic entry",
            "etam placement",
            "etam stats",
            "etam results",
            "auto entry",
            "auto admit",
        ],
        "words": [
            "etam",
            "entry",
            "major",
            "placement",
            "placed",
            "automatic",
            "competitive",
            "cutoff",
            "chance",
            "chances",
            "outcome",
            "outcomes",
            "results",
            "stats",
            "aerospace",
            "biomedical",
            "chemical",
            "civil",
            "computer",
            "electrical",
            "industrial",
            "mechanical",
            "nuclear",
            "petroleum",
        ],
    },
    {
        "name": "GPA and Grade Reports",
        "intro": "For GPA or grade distribution questions, check these:",
        "resources": ["registrar_reports", "anex"],
        "example": "Median GPA for engineering students?",
        "phrases": ["grade distribution", "grade distributions", "median gpa", "average gpa", "gpa report"],
        "words": [
            "gpa",
            "grade",
            "grades",
            "distribution",
            "distributions",
            "median",
            "average",
            "stats",
            "statistics",
            "report",
            "reports",
        ],
    },
    {
        "name": "Advising",
        "intro": "For personal academic questions, use official advising contacts:",
        "resources": ["advisors"],
        "example": "Who do I talk to if I am behind?",
        "phrases": [
            "who do i talk to",
            "who should i talk to",
            "i am behind",
            "i'm behind",
            "falling behind",
            "academic help",
            "q drop",
            "drop a class",
            "drop a course",
        ],
        "words": ["advisor", "advisors", "advising", "contact", "help", "behind", "personal", "progress", "qdrop"],
    },
    {
        "name": "Career",
        "intro": "For internships, jobs, resumes, and interviews, start here:",
        "resources": ["career_center"],
        "example": "How do I get an internship?",
        "phrases": ["get an internship", "find an internship", "career fair", "resume help", "interview prep"],
        "words": ["career", "internship", "internships", "job", "jobs", "resume", "interview", "employer", "coop", "coops"],
    },
    {
        "name": "Research",
        "intro": "For undergraduate research options, start here:",
        "resources": ["research"],
        "example": "How do I join a research lab?",
        "phrases": ["undergraduate research", "research lab", "faculty research"],
        "words": ["research", "lab", "labs", "project", "projects", "faculty"],
    },
    {
        "name": "Scholarships",
        "intro": "For scholarship and financial aid information, start here:",
        "resources": ["scholarships"],
        "example": "Can I get a scholarship?",
        "phrases": ["financial aid", "pay for school", "scholarship application"],
        "words": ["scholarship", "scholarships", "aid", "financial", "money", "award", "awards", "tuition"],
    },
    {
        "name": "Majors",
        "intro": "For the current list of engineering majors, start here:",
        "resources": ["degrees", "catalog"],
        "example": "What engineering majors are there?",
        "phrases": ["what majors", "engineering majors", "degree programs", "undergraduate degrees"],
        "words": ["majors", "programs", "departments"],
    },
]


# ----------------------------
# Student shorthand
# ----------------------------

SLANG_WORDS = {
    "profs": "professors",
    "prof": "professor",
    "rmp": "rate my professor",
    "distr": "distribution",
    "dist": "distribution",
    "distro": "distribution",
    "diff": "different",
    "sched": "schedule",
    "reg": "registration",
    "syl": "syllabus",
    "sylabus": "syllabus",
    "syllbus": "syllabus",
    "syllabus?": "syllabus",
    "q drop": "qdrop",
    "q-drop": "qdrop",
    "intern": "internship",
    "interns": "internships",
    "co op": "coop",
    "scholly": "scholarship",
    "schollies": "scholarships",
    "fin aid": "financial aid",
    "adviser": "advisor",
    "advisers": "advisors",
    "auto admit": "automatic entry",
    "auto entry": "automatic entry",
    "mech e": "mechanical",
    "meche": "mechanical",
    "aero": "aerospace",
    "bmen": "biomedical",
    "chem e": "chemical",
    "chen": "chemical",
    "cven": "civil",
    "ecen": "electrical",
    "csce": "computer",
    "cs": "computer",
    "pet e": "petroleum",
}


# ----------------------------
# Question matching logic
# ----------------------------

def get_words(text):
    # This turns a question into lowercase words so matching is easier.
    return set(re.findall(r"[a-zA-Z0-9]+", normalize_question(text)))


def normalize_question(text):
    # Students type shorthand a lot, so this changes common slang into normal words.
    text = text.lower()

    for slang, normal_word in SLANG_WORDS.items():
        text = re.sub(rf"\b{re.escape(slang)}\b", normal_word, text)

    return text


def score_category(question, category):
    # Phrases get more points than single words because they are usually more specific.
    question_lower = normalize_question(question)
    question_words = get_words(question_lower)
    score = 0

    for phrase in category["phrases"]:
        if phrase in question_lower:
            score += 5
            break

    for word in category["words"]:
        if word in question_words:
            score += 1

    # Professor grade questions should go to Anex, not the general GPA reports.
    if category["name"] == "Professor Info":
        has_professor_word = bool(question_words & {"professor", "professors", "prof", "instructor", "instructors"})
        has_grade_word = bool(question_words & {"grade", "grades", "distribution", "distributions"})

        if has_professor_word and has_grade_word:
            score += 4

    return score


def pick_category(question):
    # Go through every category and keep whichever one has the best score.
    best_category = None
    best_score = 0

    for category in CATEGORIES:
        score = score_category(question, category)

        if score > best_score:
            best_category = category
            best_score = score

    return best_category


# ----------------------------
# Answer building
# ----------------------------

def build_resource_answer(category):
    # This formats the links in a way that Streamlit can display nicely.
    lines = [category["intro"], ""]

    for number, resource_key in enumerate(category["resources"], start=1):
        resource = RESOURCES[resource_key]
        lines.append(f"{number}. {resource['title']}")
        lines.append(f"   {resource['url']}")
        lines.append(f"   {resource['description']}")
        lines.append("")

    if category["name"] in ["Schedule", "Degree Plan", "Advising"]:
        lines.append("For personal academic decisions, it is safest to ask an academic advisor.")

    if category["name"] in ["ETAM", "GPA and Grade Reports", "Scholarships"]:
        lines.append("Because this information can change, use the official page for the current details.")

    return "\n".join(lines).strip()


def build_not_sure_answer():
    # If nothing matches, these are broad starting points that are still useful.
    starter_links = {
        "intro": "I could not confidently match that question. These are good starting points:",
        "resources": ["etam_process", "advisors", "catalog", "degrees"],
        "name": "Not Sure",
    }

    return build_resource_answer(starter_links)


def answer_question(question):
    # First try the main categories. If that fails, show broad starter links.
    category = pick_category(question)

    if category:
        return build_resource_answer(category)

    return build_not_sure_answer()


# ----------------------------
# UI functions
# ----------------------------

def apply_theme():
    # This is just a simple dark/maroon style so the app looks TAMU themed.
    st.markdown(
        """
        <style>
        .stApp {
            background: #180c10;
            color: #f7eeeb;
        }

        [data-testid="stSidebar"] {
            background: #26141a;
        }

        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #f7eeeb;
        }

        [data-testid="stHeaderActionElements"],
        .stHeadingActionButton,
        [title="Copy link to this heading"] {
            display: none;
        }

        [data-testid="stMarkdownContainer"] a {
            color: #d9a5b1;
            font-weight: 600;
        }

        .app-subtitle {
            color: #d2bbb5;
            max-width: 780px;
            margin-bottom: 1rem;
        }

        .message-label {
            color: #d9a5b1;
            font-size: 0.78rem;
            font-weight: 700;
            margin: 1rem 0 0.35rem;
            text-transform: uppercase;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #241219;
            border-color: #5b303d;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_message(label, message):
    st.markdown(f'<div class="message-label">{label}</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(message)


def show_sidebar():
    # The sidebar is for ideas and summary
    with st.sidebar:
        st.header("FAQ Categories")

        for category in CATEGORIES:
            st.write(f"- {category['name']}")

        st.divider()
        st.caption("The app routes questions to official pages when possible.")


# ----------------------------
# Main app
# ----------------------------

def main():
    # Streamlit reruns this function whenever the user submits a new question.
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    apply_theme()

    st.title(APP_TITLE)
    st.markdown(f'<p class="app-subtitle">{APP_DESCRIPTION}</p>', unsafe_allow_html=True)
    st.caption(DISCLAIMER)

    show_sidebar()

    question = st.chat_input("Ask about ETAM, GPA reports, professors, schedules, degree plans, advising, or careers")

    if not question:
        st.info("Try: What is ETAM? Where can I find GPA distributions? Which professor should I take?")
        return

    render_message("You", question)

    with st.spinner("Finding the best FAQ category..."):
        answer = answer_question(question)

    render_message("FAQ Finder", answer)


if __name__ == "__main__":
    main()
