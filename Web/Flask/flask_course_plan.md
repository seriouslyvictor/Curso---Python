+-----------------------------------------------------------------------+
| **PYTHON WEB DEVELOPMENT**                                            |
|                                                                       |
| **Flask Course Plan**                                                 |
|                                                                       |
| *From First Route to Deployment*                                      |
+-----------------------------------------------------------------------+

12 Sessions · 6 Weeks · 36 Hours

3-hour blocks, twice a week

Mixed ages · Hands-on focus · VS Code + Terminal

Course Overview

This course takes students from zero web development experience to
deploying a fully functional Flask application. Students arrive with
approximately 40 hours of core Python and a brief HTML/CSS crash course.
Over 12 sessions, they will learn how Python and HTML/CSS connect
through Flask, building progressively more complex web applications.

Every session is designed with teenagers in mind: minimal lecture,
maximum hands-on coding. The format prioritizes learning by building
over learning by listening.

**Pedagogical Approach**

-   Each 3-hour session follows a consistent rhythm: demo, guided
    practice, free practice

-   Lecture and demos are capped at approximately 40 minutes, with
    mini-challenges embedded to maintain engagement

-   Students practice on self-contained exercises each session, building
    confidence incrementally

-   The course builds toward TCC (final project) readiness, where
    students will apply everything independently

**Session Map**

  ----------------------------------------------------------------------------
  **\#**   **Session Title**        **Key Topics**
  -------- ------------------------ ------------------------------------------
  1        Flask Foundations        First routes, dev server, request/response
                                    cycle

  2        Templates with Jinja2    render_template, variables, logic blocks

  3        Template Inheritance +   base.html, blocks, linking CSS/images
           Static Files             

  4        Forms & User Input (GET) HTML forms, query parameters, request.args

  5        Forms & User Input       POST method, request.form, two-route
           (POST)                   pattern, in-memory state

  6        Data Persistence         SQLite, Flask-SQLAlchemy, models, first
                                    queries

  7        Full CRUD: Create & Read Form to database to listing page

  8        Full CRUD: Update &      Edit forms, delete confirmation
           Delete                   

  9        User Feedback & Polish   Flash messages, redirect, PRG pattern

  10       Auth Part 1: Sessions &  Sessions, login/logout, route protection
           Login                    

  11       Auth Part 2: Password    werkzeug.security, data ownership
           Hashing                  

  12       Deployment               Render/Railway, env variables, going live
  ----------------------------------------------------------------------------

**Prerequisites**

-   Approximately 40 hours of core Python (variables, functions, loops,
    data structures, classes)

-   Basic HTML/CSS crash course completed (can write simple pages with
    tags, classes, selectors)

-   VS Code installed with Python extension, terminal comfort

-   Flask and pip already installed and working

+-----------------------------------------------------------------------+
| **SESSION 1**                                                         |
|                                                                       |
| **Flask Foundations**                                                 |
|                                                                       |
| *\"Hello, Web!\" --- From Python script to running website*           |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students go from zero to a running
                          Flask app with multiple routes and understand
                          what happens when a browser visits a URL.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- -------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**   Opening hook, first app,
  0:40**                          request/response, routes

  **0:40 --  **Mini-Challenge**   Quick check: write a route without
  0:45**                          looking

  **0:45 --  **Break**            
  0:55**                          

  **0:55 --  **Guided Practice**  Personal Card site with teacher guidance
  1:25**                          

  **1:25 --  **Free Practice**    Mini Wikipedia project + stretch goals
  2:45**                          

  **2:45 --  **Wrap-up**          Show-and-tell, seed next session
  3:00**                          
  ---------- -------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[40 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Open a browser and visit any well-known website. Ask the class: \"What
just happened between your browser and that computer somewhere in the
world?\" Keep it brief and visual --- browser asks, server answers, that
is the entire model. Flask is the thing that lets their Python code be
the one answering.

**Live Coding --- First App**

*\[15 minutes\]*

-   Create the project folder together, show the minimal structure

-   Write the minimal app.py: import Flask, create the app instance, one
    route returning a string

-   Run flask run in the terminal --- the moment it works in the
    browser, pause and celebrate

-   Turn on debug mode: change the return string, save, refresh ---
    demonstrate the instant feedback loop

  -----------------------------------------------------------------------
  **Tip:** This is the single most important moment of the session. When
  their browser shows text that their Python code produced, the
  connection between back-end and front-end clicks. Do not rush past it.

  -----------------------------------------------------------------------

**The Request/Response Cycle --- Made Visible**

*\[10 minutes\]*

Open browser dev tools, go to the Network tab. Hit the route and watch
the request go out and the response come back. This is not a deep
lecture --- it is simply: \"Look at this tab, see these two things
talking.\"

-   Point out the status code (200) and content type

-   Change the route to something that does not exist --- see the 404
    appear in real time

-   The goal is demystification: the web is just messages going back and
    forth

**Adding More Routes**

*\[10 minutes\]*

-   Add /about and /contact routes, each returning different strings

-   Introduce dynamic routes: /hello/\<name\> using f-strings they
    already know from core Python

-   Show how the variable in the URL becomes a variable in the function
    --- this should feel familiar

⚡ **Mini-Challenge Before Break**

*\[5 minutes\]*

\"Without looking at my screen, add a route /secret that returns a fun
message. You have 2 minutes.\" This ensures every student has typed at
least one route themselves and that their setup is working before the
break.

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: \"Personal Card\" Site**

Students build a small site with teacher guidance. The teacher codes
along on the projector for the first route, then students continue on
their own while the teacher circulates.

**Requirements:**

-   At least 4 routes: home (/), about me, hobbies, and a fun secret
    page

-   Each route returns a different string --- HTML in the strings is
    fine if they want, but not required

-   At least one dynamic route (e.g. /hobby/\<hobby_name\> that responds
    differently per hobby)

-   Encouraged to peek at the Network tab to see their requests
    appearing

  -----------------------------------------------------------------------
  **Tip:** Circulate actively during this block. The students who
  struggle here are usually stuck on file saving, terminal issues, or
  typos in the decorator --- not conceptual problems. Quick fixes keep
  momentum high.

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: \"Mini Wikipedia\"**

Build a Flask app with at least 6 routes, each about a different topic
the student finds interesting (games, music, sports, anime --- whatever
they want). This gives them repetition with routes while keeping it
personal.

**Requirements:**

-   A home/index route (/) that lists what pages exist

-   At least 6 topic routes with actual content

-   At least one dynamic route

-   Debug mode on for fast iteration

**Stretch Goals (fast finishers):**

-   Add a /random route that uses random.choice() to pick and display a
    random topic

-   Return actual HTML in the strings --- headers, bold, paragraphs ---
    to start feeling the pain of writing HTML inside Python strings

-   Experiment: what happens if two routes have the same URL path?

  -----------------------------------------------------------------------
  **Tip:** The HTML-in-strings stretch goal is strategic. Students who
  try it will get frustrated with the messy code, which creates the
  natural \"aha\" moment for templates in Session 2. If they complain,
  tell them: \"Yeah, this is terrible. We fix it next class.\"

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   Quick show-and-tell: 2--3 volunteers show their routes in the
    browser

-   Acknowledge common struggles out loud --- normalizes the learning
    process

-   Seed the next class: \"Did anyone get annoyed writing HTML inside
    Python strings? Next class we fix that problem.\"

**Materials & Preparation**

-   **Cheat sheet:** Minimal Flask app boilerplate, \@app.route syntax,
    dynamic route syntax \<variable\>, and how to run the dev server

-   **Troubleshooting guide:** Common errors and fixes --- \"Address
    already in use\" (kill the other process or change port), forgot to
    save before refresh, running flask run from the wrong folder, typos
    in the decorator

-   **Pre-check:** Verify before class that Flask is installed and flask
    run works on at least one test machine. Have a backup plan if a
    student's setup is broken (pair programming with a neighbor).

+-----------------------------------------------------------------------+
| **SESSION 2**                                                         |
|                                                                       |
| **Templates**                                                         |
|                                                                       |
| *Stop Writing HTML in Python --- Jinja2 takes over presentation*      |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students move from returning strings
                          to rendering real HTML files, use Jinja2 to
                          inject Python data into pages, and understand
                          why this separation exists.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Hook, first template, variables,
  0:45**                         mini-challenge, logic blocks

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Dynamic Profile Card with teacher
  1:25**                         guidance

  **1:25 --  **Free Practice**   Top 5 Fan Page project + stretch goals
  2:45**                         

  **2:45 --  **Wrap-up**         Show-and-tell, seed next session
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Pull up a student's Mini Wikipedia from last class --- ideally one who
attempted the stretch goal of returning HTML in strings. Show the mess
on the projector: escaped quotes, no syntax highlighting, unreadable
code. Ask: \"Would you want to build a real website like this?\" The
answer sells the lesson.

**The Fix --- First Template**

*\[15 minutes\]*

-   Create the /templates folder --- emphasize this is a Flask
    convention, not optional

-   Move the home page HTML into home.html as a normal HTML file

-   Import render_template and change the route to return
    render_template(\'home.html\')

-   Refresh the browser --- same result, much cleaner code

-   Emphasize: Python does logic, HTML does presentation. They have
    different jobs.

  -----------------------------------------------------------------------
  **Tip:** Write the folder name on the board: templates (with the
  \'s\'). Forgetting the \'s\' or mistyping the filename is the #1 cause
  of TemplateNotFound errors in this session.

  -----------------------------------------------------------------------

**Variables in Templates**

*\[15 minutes\]*

-   Pass data to the template: render_template(\'home.html\',
    name=\'Alice\')

-   In the template: \<h1\>Hello, {{ name }}!\</h1\>

-   Pass multiple variables, including a list, to demonstrate
    flexibility

-   Make it explicit: {{ }} is just \"print this Python thing here\"

-   Live demo: pass current_time using datetime.now() --- students see
    their page update on refresh

⚡ **Mini-Challenge**

*\[5 minutes\]*

\"Create a route /greet/\<name\> that renders a template and shows a
personalized greeting. You have 3 minutes.\" Quick pulse check that
combines everything from Session 1 (dynamic routes) with the new
template concept.

**Logic Blocks**

*\[10 minutes\]*

-   Introduce {% for %} \... {% endfor %} --- loop over a list of
    hobbies

-   Introduce {% if %} / {% else %} / {% endif %} --- show different
    content based on a variable

-   Contrast clearly: {{ }} OUTPUTS, {% %} CONTROLS. Say it twice.

-   Show one gotcha live: forget {% endfor %} and let Jinja yell at them
    with a clear error message

  -----------------------------------------------------------------------
  **Tip:** The {{ }} vs {% %} distinction is the conceptual keystone of
  this session. Write both on the board and draw a line between \"shows
  stuff\" and \"controls stuff.\" Students who internalize this now will
  breeze through inheritance next class.

  -----------------------------------------------------------------------

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Dynamic Profile Card**

Students build a profile card system that hits every core Jinja concept
in one focused project. Teacher codes along on the projector for the
first profile, then students continue on their own while the teacher
circulates.

**Requirements:**

-   A route /profile/\<username\> that renders a profile template

-   The template receives: a name, an age, a list of hobbies, a favorite
    quote

-   Use {{ }} to display the simple variables

-   Use {% for %} to loop through the hobbies and display them as a list

-   Use {% if %} to show a different message if age is under 18 vs 18+

-   At least 3 hardcoded profiles stored as dicts in the Python file,
    selectable by username

  -----------------------------------------------------------------------
  **Tip:** Most common issues during circulation: forgot to import
  render_template, wrong folder name (\"template\" instead of
  \"templates\"), mixing up {{ }} and {% %}, or missing {% endfor %}/{%
  endif %}. Have these four on a printed cheat sheet ready to hand out.

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: \"Top 5\" Fan Page**

Build a Flask app about something the student loves --- a band, game,
show, sport, anything. Personal investment keeps motivation high while
they get repetition with templates and logic blocks.

**Requirements:**

-   A home route that renders home.html with a title and a list of 5
    items passed from Python

-   The template loops through the items and displays each one

-   A detail route /item/\<item_id\> that renders a separate template
    showing info about one item

-   At least one {% if %} block somewhere that changes what is displayed
    based on data

-   Items stored as a list of dicts in Python (name, description,
    rating, etc.)

**Stretch Goals (fast finishers):**

-   Add a rating to each item and use {% if %} + {% for %} to display N
    star emojis based on the rating

-   Add an is_favorite flag --- mark that item with special styling or a
    badge

-   Try {% else %} and {% elif %} for more nuanced conditionals

-   Pass the current date using datetime and display it somewhere in the
    template

  -----------------------------------------------------------------------
  **Tip:** If a student finishes the core challenge fast and is eyeing
  the stretch goals, nudge them toward the star-rating one first --- it
  forces them to nest a loop inside a conditional, which solidifies both
  concepts at once.

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   2--3 volunteers show their fan pages in the browser

-   Reinforce the two big ideas: (1) Python file stays clean, HTML file
    stays clean, (2) {{ }} for output, {% %} for logic

-   Seed next class: \"Your home and detail pages probably look really
    similar --- same header, same footer. Copy-pasting that everywhere
    would be painful with 20 pages. Next class we fix that, and we
    finally style everything with real CSS files.\"

**Materials & Preparation**

-   **Cheat sheet:** render_template syntax, passing variables, {{ }} vs
    {% %}, {% for %} and {% if %} syntax with closing tags highlighted

-   **Error reference:** What TemplateNotFound looks like and how to fix
    it (folder name, file name, typo)

-   **Common mistakes sheet:** Show {{%}} vs {%%} vs {{}} side by side
    --- teenagers mix these up constantly

-   **Pre-check:** Save a student Mini Wikipedia from Session 1 that
    used HTML in strings (with permission) to use as the opening hook

**Pedagogical Notes**

The biggest trap in this session is spending too long on the hook or
theory. The real learning happens when students are writing {{ variable
}} themselves and watching it appear on their page. If the lecture runs
long, cut the logic blocks demo shorter --- they will pick it up in the
guided practice anyway.

For mixed confidence levels: the guided practice is deliberately
structured so strugglers have a clear path, while the free practice is
open-ended so advanced students can push themselves with stretch goals.
This natural differentiation avoids anyone feeling stuck or bored.

Session 3 will introduce base.html and static files, which is why this
session ends with a deliberately unstyled, repetitive-feeling fan page.
The pain is the point --- it creates the motivation for template
inheritance.

+-----------------------------------------------------------------------+
| **SESSION 3**                                                         |
|                                                                       |
| **Template Inheritance + Static Files**                               |
|                                                                       |
| *Stop copy-pasting navbars --- and finally, real CSS*                 |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students eliminate duplication with
                          base.html and blocks, and link their HTML/CSS
                          knowledge into Flask by serving real
                          stylesheets and images from /static.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Inheritance, base.html, blocks, static
  0:45**                         files, url_for

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Refactor the Session 2 fan page with
  1:25**                         inheritance + CSS

  **1:25 --  **Free Practice**   Multi-page portfolio site from scratch
  2:45**                         

  **2:45 --  **Wrap-up**         Show-and-tell, seed next session
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Pull up a fan page from last session with the home and detail templates
open side by side. Highlight the duplicated parts --- the same \<head\>,
the same nav, the same footer. Ask: \"If you wanted to add one link to
your menu, how many files would you have to edit?\" Now imagine 20
pages. The pain is real --- and that is exactly what we are fixing
today.

**Template Inheritance --- The base.html Pattern**

*\[15 minutes\]*

-   Create base.html with the skeleton: \<!DOCTYPE html\>, \<head\>,
    \<body\>, nav, footer

-   Introduce {% block content %}{% endblock %} as a \"hole\" where
    child pages slot their content

-   Add {% block title %}My Site{% endblock %} inside \<title\> for
    per-page titles

-   Convert home.html to extend base: {% extends \'base.html\' %} and
    fill in {% block content %}\...{% endblock %}

-   Refresh --- same page, but now the header/footer lives in one place

-   Convert the detail page too --- watch how much smaller the files get

-   Live edit: add a link to the nav in base.html, refresh both pages,
    see both update --- this is the magic moment

  -----------------------------------------------------------------------
  **Tip:** Do not skip the live-edit moment. Editing base.html once and
  seeing two child pages update is what makes inheritance click. It is
  the payoff for the whole concept.

  -----------------------------------------------------------------------

⚡ **Mini-Challenge**

*\[5 minutes\]*

\"Add a new page /credits that extends base.html and just has a heading
inside the content block. You have 3 minutes.\" Quick confidence check
that they understand extends and block.

**Static Files --- Connecting CSS At Last**

*\[15 minutes\]*

-   Create the /static folder alongside /templates

-   Create static/css/style.css with something dramatic (big colored
    background) so the change is obvious

-   In base.html, link it: \<link rel=\"stylesheet\" href=\"{{
    url_for(\'static\', filename=\'css/style.css\') }}\"\>

-   Refresh --- the whole site is now styled

-   Explain url_for in one sentence: \"It is Flask\'s way of writing the
    correct path to a file without us guessing.\" Do not over-explain.

-   Show that images work the same way: put an image in static/images/,
    reference it with url_for

**The Key Insight**

*\[5 minutes\]*

Draw on the board or show on screen:

-   /templates → HTML files (Python\'s job to send these)

-   /static → CSS, images, JS (browser fetches these directly)

-   Two different pipelines, one project

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Refactor the Top 5 Fan Page**

Students take their fan page from Session 2 and refactor it with
inheritance and static files. The refactoring approach is deliberate:
they are not building something new, they are making something they
already built better. This reinforces that inheritance is a tool for
real-world cleanup, not an abstract concept.

**Requirements:**

-   Create base.html with a proper skeleton, nav bar (Home plus at least
    one other link), and footer

-   Add blocks for title and content

-   Refactor home.html and the detail template to extend base.html

-   Create static/css/style.css and link it in base.html

-   Add at least 5 CSS rules that actually change the page (background,
    font, spacing, nav styling, anything)

-   Add at least one image from static/images/ somewhere (logo, banner,
    background --- their choice)

  -----------------------------------------------------------------------
  **Tip:** Students who missed Session 2 should get a barebones fan page
  handout so they can jump straight into refactoring without having to
  rebuild from scratch. This keeps the whole class on the same exercise
  and avoids anyone falling further behind.

  -----------------------------------------------------------------------

Most common issues during circulation: forgetting to save the CSS file,
typos in url_for, missing quotes around \'css/style.css\', or the
browser caching the old CSS. Teach them Ctrl+Shift+R for a hard refresh
--- it will save hours across the rest of the course.

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: Multi-Page Portfolio Site**

Build a personal portfolio from scratch. This cements inheritance,
static files, and previous concepts (loops, variables, dynamic content)
into one cohesive piece --- and it is something they can actually show
to family and friends. Motivation matters.

**Requirements:**

-   At least 4 pages: Home, About, Projects, Contact

-   All pages extend a shared base.html with a nav bar linking to all
    four

-   A linked external CSS file in static/css/

-   At least one image served from static/images/

-   Each page uses {% block title %} to set its own browser tab title

-   The Projects page loops through a list of project dicts passed from
    Python (name + description + optional image)

**Stretch Goals (fast finishers):**

-   Add a second block like {% block extra_css %} for page-specific
    styles

-   Use {% if %} in the nav to highlight the current page (requires
    passing a current_page variable from each route)

-   Add a Google Font via a \<link\> in base.html and apply it in the
    CSS

-   Make the portfolio responsive with basic CSS (mobile-friendly nav,
    flex layouts)

  -----------------------------------------------------------------------
  **Tip:** Watch out for students who get too deep into CSS and spend the
  whole free practice tweaking colors without finishing all four pages.
  Gentle nudge: \"Get all four pages working first, then make them
  pretty.\"

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   2--3 volunteers show their portfolios --- celebrate the visual
    polish, this is the first session where results look like a \"real
    website\"

-   Reinforce: base.html + {% block %} is one of the most useful
    patterns in this course. They will use it in every Flask project,
    forever.

-   Seed next class: \"Right now your sites just SHOW stuff. Next class,
    your users will be able to TYPE stuff back to you --- we are
    building forms.\"

**Materials & Preparation**

-   **Cheat sheet:** base.html skeleton template, {% extends %} syntax,
    {% block %} syntax, url_for(\'static\', filename=\'\...\') with
    quotes highlighted

-   **Starter CSS file:** A few pre-written rules students can copy as a
    starting point --- especially helpful for students whose CSS
    confidence is shaky from the crash course

-   **Barebones fan page handout:** A minimal working Top 5 fan page for
    students who missed Session 2 or did not finish, so they can jump
    straight into refactoring without rebuilding from scratch

-   **Troubleshooting guide:** \"My CSS isn\'t showing up\" → check
    folder name, check url_for quotes, hard refresh with Ctrl+Shift+R

**Pedagogical Notes**

This is the first session where their work LOOKS like real websites,
which is a massive motivation boost. Do not undercut it with too much
lecture. If a student finishes everything, encourage them to spend time
actually designing (colors, spacing, images) rather than jumping to the
next conceptual thing. The aesthetic reward of CSS working is what
cements the session emotionally.

The url_for function will appear again and again throughout the course
(for linking routes, for static files, for redirects). Do not
over-explain it now --- treat it as \"the right way to reference things
in Flask\" and let familiarity build across sessions.

The hard-refresh tip (Ctrl+Shift+R) pays dividends for the rest of the
course. Teach it deliberately, write it on the board, and bring it up
again any time a student says \"my changes aren\'t showing up.\"

+-----------------------------------------------------------------------+
| **SESSION 4**                                                         |
|                                                                       |
| **Forms & User Input (GET)**                                          |
|                                                                       |
| *The browser URL is just data --- Python reads it*                    |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students understand how HTML forms
                          send data through the URL via GET, and how
                          Flask reads it with request.args.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Hook, first form, request.args, dropdown,
  0:45**                         mini-challenge

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Teacher demos one conversion, students
  1:25**                         add their own

  **1:25 --  **Free Practice**   Full Conversor Universal
  2:45**                         

  **2:45 --  **Wrap-up**         Show-and-tell, seed POST
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Open the browser on Google search. Type something and hit enter. Point
at the URL: ?q=flask+tutorial. Ask: "Where did that come from?" That
?q= is a form. The browser just put their input in the URL. Flask can
read that exact same thing --- and that is what today is about.

**First Form**

*\[15 minutes\]*

-   Write a plain HTML form: action="/", method="GET", one
    \<input name="value"\>, one submit button

-   Show what happens in the URL when you submit --- the input name
    appears as ?value=...

-   In the route: request.args.get("value") --- reads it right out of
    the URL

-   Return the value in the template. Refresh, change the input, see the
    URL change, see the page change

-   Open Network tab, show the request going out with the query string
    visible

  -----------------------------------------------------------------------
  **Tip:** The moment they see their typed value appear in the URL and
  then on the page is the whole concept. Do not rush past it. Ask a
  student to type something unexpected and watch the URL update live.

  -----------------------------------------------------------------------

**Adding a Dropdown**

*\[10 minutes\]*

-   Add a \<select name="type"\> with two options: celsius and kg

-   In Python: request.args.get("type") --- same pattern, different
    input element

-   Show that both values arrive together: args.get("value") and
    args.get("type")

-   Write the conditional: if type == "celsius": result = ..., elif type
    == "kg": result = ...

-   Emphasize: the form does not care what the dropdown means --- it
    just sends a string. Python decides what to do with it.

  -----------------------------------------------------------------------
  **Tip:** Write request.args.get("name") on the board and keep it there
  for the whole session. Every confusion in this session traces back to
  either the name attribute in HTML or the key passed to .get(). When
  students are stuck, point at the board.

  -----------------------------------------------------------------------

**Handling the Empty State**

*\[10 minutes\]*

-   What happens if someone visits the page with no form submission yet?
    request.args.get("value") returns None

-   Show the template crashing if you try to display None in a
    calculation

-   Fix: if "value" in request.args: --- only compute when the form has
    been submitted

-   Show the clean pattern: render the form, only show the result
    section when data exists

  -----------------------------------------------------------------------
  **Tip:** This "empty state" problem is not a gotcha --- it is a
  real-world habit. Any time they read from a form or URL, they should
  ask: "What happens if this isn't there yet?" Plant the habit now, it
  pays off for the rest of the course.

  -----------------------------------------------------------------------

⚡ **Mini-Challenge Before Break**

*\[5 minutes\]*

"Add a third option to the dropdown --- your choice. Add the conversion
logic in Python. 3 minutes." Quick test that they can extend a pattern
rather than just copy one.

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Celsius → Fahrenheit (together), then extend alone**

Teacher codes the full working Celsius → Fahrenheit converter on the
projector: the route, the form, the dropdown with one option, the
conditional, the result in the template. Students follow along. Then the
teacher steps back and gives the instruction:

"Now add at least two more conversion types on your own. You already
have the pattern."

**Requirements:**

-   One route /, one template converter.html

-   A \<select\> dropdown with at least 3 options total (Celsius is the
    one from the demo)

-   request.args.get() to read both the value and the selected type

-   A conditional block in Python that computes the correct result per
    type

-   The result displayed in the template only when a conversion has been
    submitted

-   Sensible placeholder text when the page first loads ("Enter a value
    above")

  -----------------------------------------------------------------------
  **Tip:** Students who get stuck after the demo are almost always stuck
  on one of two things: the name attribute mismatch, or forgetting to
  guard against the empty state. Check those two things first before
  reading their logic.

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: Conversor Universal**

Build a full multi-conversion tool with a clean interface. The dropdown
grows, the logic grows, but the file count stays exactly the same: one
route, one template.

**Suggested conversions to implement:**

-   Celsius ↔ Fahrenheit (from the demo)

-   Quilogramas → Libras

-   Centímetros → Polegadas

-   Quilômetros → Milhas

-   BRL → USD (use a fixed rate --- no API, no drama)

-   Hectares → campos de futebol (always gets a laugh)

**Requirements:**

-   At least 5 conversion types in the dropdown

-   Result only shown after submission (empty state handled)

-   Conversion type displayed in the result ("23°C = 73.4°F", not just
    "73.4")

-   A clear, readable template (student's choice of styling)

**Stretch Goals (fast finishers):**

-   Add a "swap direction" option --- e.g. Fahrenheit → Celsius as a
    separate dropdown entry

-   Show the formula used below the result ("Fórmula: (°C × 9/5) + 32")

-   Add input validation: what if the user types "banana"? Use
    try/except float() and show a friendly error message in the template

-   Style the result differently depending on the conversion type (a
    thermometer emoji for temperature, a scale for weight, etc.)

  -----------------------------------------------------------------------
  **Tip:** The BRL → USD conversion tends to spark a real conversation
  about exchange rates and why a fixed rate is a simplification. That is
  fine --- it takes 30 seconds and makes the exercise feel grounded. If
  a student asks "but what if the rate changes?" tell them: "Great
  question. That is an API. We are not there yet."

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   2--3 volunteers show their conversor in the browser --- ask them to
    try a few conversions live

-   Reinforce the key insight: GET forms just put data in the URL.
    request.args.get() reads it. That is the whole model.

-   Seed next class: "Today the URL changed every time you submitted.
    What if you didn't want that? What if you were sending a password,
    or a vote, or a prediction? Next class: POST."

**Materials & Preparation**

-   **Cheat sheet:** HTML form syntax with method="GET", \<input
    name=""\> and \<select name=""\>, request.args.get("key"), the
    empty-state guard pattern

-   **Conversion formulas reference:** A short list of the formulas for
    each suggested conversion --- saves students Googling mid-exercise

-   **Pre-check:** Confirm request is imported from flask in the demo
    starter file

**Pedagogical Notes**

The single-file constraint is intentional and worth enforcing. Every
conversion gets added to the same route and the same template ---
students feel the app grow without the cognitive overhead of new files.
This is the right scope for a first encounter with forms.

The empty-state handling is the most important habit introduced in this
session. It will reappear every time they read from request.args or
request.form for the rest of the course. Frame it as a professional
instinct, not a workaround.

GET is easier than POST precisely because the data is visible in the
URL. That visibility is a teaching asset --- use it deliberately. Point
at the URL constantly during the demo.

+-----------------------------------------------------------------------+
| **SESSION 5**                                                         |
|                                                                       |
| **Forms & User Input (POST)**                                         |
|                                                                       |
| *POST sends. GET shows.*                                              |
+-----------------------------------------------------------------------+

  ----------------------- -----------------------------------------------
  **Duration:** 3 hours   **Goal:** Students use a POST form to submit
                          players one at a time to an in-memory roster,
                          and a separate GET route to display the full
                          team --- experiencing the natural split between
                          the two methods.

  ----------------------- -----------------------------------------------

**Time Breakdown**

  ---------- ------------------- ----------------------------------------
  **0:00 --  **Demo & Lecture**  Hook, POST vs GET, two-route pattern,
  0:45**                         request.form, mini-challenge

  **0:45 --  **Break**           
  0:55**                         

  **0:55 --  **Guided Practice** Teacher builds /add together, students
  1:25**                         build /team alone

  **1:25 --  **Free Practice**   Full Dream Team for a country of their
  2:45**                         choice

  **2:45 --  **Wrap-up**         Show-and-tell, seed database
  3:00**                         
  ---------- ------------------- ----------------------------------------

🎬 **Block 1 --- Demo & Lecture**

*\[45 minutes\]*

**Opening Hook**

*\[5 minutes\]*

Pull up the Conversor from last class. Submit a conversion. Point at
the URL: all the data is right there --- value, type, everything
visible. Ask: "Would you want the player you're signing to appear in
the URL for everyone to see?" Now imagine a transfer form, a login, a
vote. Some data belongs in the request body, invisible, not in the
URL. That's POST. Same idea --- form sends data to Python --- different
lane.

**Two Routes, Two Jobs**

*\[5 minutes\]*

Draw on the board before writing a line of code:

-   /add → POST. The form. Where players get submitted.

-   /team → GET. The roster. Where the full team is displayed.

One route sends data. One route shows data. They share a single list
that lives on the server. This is the whole app.

**Building /add**

*\[15 minutes\]*

-   Declare team = [] at the top of app.py --- at module level, outside
    any function

-   Write the /add route with methods=["GET", "POST"]

-   Write the form template: three fields --- name (text), position
    (dropdown: Goalkeeper, Defender, Midfielder, Forward), image_url
    (text)

-   On GET: render the empty form

-   On POST: request.form.get("name"), request.form.get("position"),
    request.form.get("image_url") --- append a dict to team, then
    redirect to /team

-   Submit one player live. Nothing shows yet --- redirect lands on
    /team, which does not exist. Good. That is the next step.

  -----------------------------------------------------------------------
  **Tip:** Write request.args for GET and request.form for POST side by
  side on the board and leave them there. Students coming from Session 4
  will reach for request.args out of habit. When it returns None, point
  at the board.

  -----------------------------------------------------------------------

**Building /team**

*\[10 minutes\]*

-   Write the /team route: just render_template("team.html", team=team)

-   Write team.html: loop through team with {% for %}, display name,
    position, and the image with \<img src="{{ player.image_url }}"\>

-   Add the empty state: {% if team %} ... {% else %} "Nenhum jogador
    ainda."

-   Refresh --- the player submitted a moment ago appears on the roster

  -----------------------------------------------------------------------
  **Tip:** The redirect after POST is deliberate and worth naming
  explicitly: "We POST to /add, then immediately GET /team. The form
  and the display are separate. This is the clean pattern." Do not go
  deep on PRG yet --- just plant the habit.

  -----------------------------------------------------------------------

**The 11-Player Cap**

*\[5 minutes\]*

-   Show the guard in the POST handler: if len(team) < 11: append, else
    skip

-   This is a real constraint, not an exercise bolt-on. A football team
    has 11 players. The code enforces the rule.

⚡ **Mini-Challenge Before Break**

*\[5 minutes\]*

"Add a number field to the form --- shirt number, text input. Read it
in the route, store it in the dict, display it on the team page. 3
minutes." Ensures every student has written request.form.get() at
least once before the break.

☕ **Break**

*\[10 minutes\]*

🛠 **Block 2 --- Guided Practice**

*\[30 minutes\]*

**Project: Brazil Dream Team --- /add together, /team alone**

Teacher builds the full /add route and form template live on the
projector with the class: the route decorator, the form fields, the
POST handler, the redirect. Stops there. Students then build /team and
team.html on their own --- the route, the loop, the image display, the
empty state.

**Requirements:**

-   team = [] declared at module level

-   /add with methods=["GET", "POST"] --- form with name, position
    (dropdown), image URL, shirt number

-   On POST: append dict to team, redirect to /team

-   /team GET route rendering team.html

-   team.html loops through team, displays all four fields per player

-   Player image rendered with \<img src="{{ player.image_url }}"\>

-   Empty state message when no players have been added yet

-   11-player cap enforced in the POST handler

  -----------------------------------------------------------------------
  **Tip:** The most common bug here is team = [] declared inside the
  route function --- the list resets on every request and students think
  POST is not working. Check module-level placement first whenever a
  student says "my players keep disappearing."

  -----------------------------------------------------------------------

🚀 **Block 3 --- Free Practice**

*\[80 minutes\]*

**Core Challenge: Dream Team --- your country**

Students build their own dream team from scratch for any national team
they choose. Same two-route structure as the demo, fully their own
content. Personal investment in the team selection keeps motivation
high --- they will genuinely care which players make the cut.

**Requirements:**

-   Same two-route structure: /add (POST form) and /team (GET display)

-   Position dropdown with at least 4 options

-   Image URL field --- players must have images on the roster

-   11-player cap enforced

-   Empty state on the team page

-   At least basic styling: the roster should look like a roster, not a
    raw list

**Stretch Goals (fast finishers):**

-   Add a "Clear Team" button --- a second small POST form on /team that
    empties the list and redirects back (introduces the idea of multiple
    forms on one page)

-   Show a counter: "X/11 jogadores" on both pages so the user always
    knows how full the squad is

-   Add a captain flag --- a checkbox on the form, stored in the dict,
    displayed with a ⭐ badge on the roster

-   Validate that the same shirt number cannot be used twice --- check
    before appending and show an inline error if it is taken

  -----------------------------------------------------------------------
  **Tip:** Students will spend time finding good image URLs. Nudge them
  toward Wikipedia player pages or official federation sites --- the
  images are stable and usually direct links. If a student's image is
  not showing, check the URL in a browser tab first before debugging
  Flask.

  -----------------------------------------------------------------------

🎯 **Wrap-up**

*\[15 minutes\]*

-   2--3 volunteers show their rosters --- ask them to add a player live
    on the projector so the class sees the POST → redirect → GET flow
    in action

-   Reinforce the two-route split: POST is for sending, GET is for
    showing. One list, two doors.

-   Seed next class: "Right now the squad disappears the moment we
    restart the server. It lives in Python's memory, not on disk. Next
    class we fix that permanently --- we give our app a real database."

**Materials & Preparation**

-   **Cheat sheet:** methods=["GET", "POST"] on the decorator,
    request.method check, request.form.get("key"), the module-level
    list pattern, redirect syntax

-   **Starter image URLs:** 4--5 pre-tested working image URLs for
    well-known Brazilian players --- saves the first 10 minutes of the
    demo from becoming a Google Images session

-   **Pre-check:** Confirm request and redirect are both imported from
    flask in the demo file

**Pedagogical Notes**

The two-route structure is the session's main conceptual payload, not
just an exercise choice. GET and POST are not just different methods
--- they have different jobs, and splitting them into separate routes
makes that tangible. Students who see this pattern once will reach for
it instinctively in Sessions 7 and 8 when CRUD gets more complex.

The redirect after POST is introduced here as the natural thing to do
--- you submitted something, now go look at it. The formal name for
this pattern (Post/Redirect/Get) and why it matters (double-submit
prevention, browser back button behavior) comes in Session 9. Do not
front-load the theory --- let the habit form first.

The 11-player cap is a small but real moment of code reflecting a
real-world rule. Point it out explicitly: "The sport has a rule, the
code has a rule. They match." Students who connect domain logic to
conditional logic early build better instincts for the rest of the
course.
