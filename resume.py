import base64
from collections import namedtuple
from datetime import datetime


NAME = "Lukasz Madon"
EMAIL = base64.b64decode("bHVrYXN6Lm1hZG9u") + "@gmail.com"


class JobMixin(object):

    def __repr__(self):
        return "{0} - {1}, {2}, {3}, {4}\n{5}\n{6}".format(
            self.started.strftime("%B %Y"),
            self.left if isinstance(self.left, str) else self.left.strftime("%B %Y"),
            self.company,
            self.location,
            self.title,
            "\n".join(self.description),
            "=" * 20
        )


# Experience
class GMG(JobMixin):
    company = "RolePoint"
    location = "London, United Kindom"
    title = "Full Stack Developer"
    started = datetime(2015, 11, 11)
    left = "Current"
    description = [
        "Integrated multiple Application Tracking Systems for a single unified API gateway (Python 3, asyncio, REST)",
        "Implemented job recommendation engine for matching candidates based on seniority levels, location and profile",
        "Create a new website for referrals (React, CoffeeScript, Bacon.js)",
        "Created email editor with custom templeting and autocomplete (Backbone)"
    ]


class GMG(JobMixin):
    company = "Green Man Gaming Ltd"
    location = "London, United Kindom"
    title = "Full Stack Developer"
    started = datetime(2014, 9, 1)
    left = datetime(2015, 11, 11)
    description = [
        "Extending bespoke e-commerce solution (Python, Django).",
        "Integrating third-party API (Python, Cellery).",
        "Scraping infrastructure for Xbox API (Go, CouchDB).",
        "Building a new e-commerce platform in EPiServer (C#, ASP.Net) - Developing e-commerce frontend (AngularJS, Grunt, Node)."
    ]


class Firestartr(JobMixin):
    company = "Firstartr.co"
    location = "London, United Kindom"
    title = "Full Stack Developer"
    started = datetime(2013, 12, 1)
    left = datetime(2014, 9, 1)
    description = [
        "Building a custom CRM tool for managing dealfow (Python + Angular, REST, app.frestartr.co).",
        "Real time searching for investors graph (Angular integration github.com/lukasz-madon/algolia- angular-example)."
    ]


class Lyst(JobMixin):
    company = "Lyst.com"
    location = "London, United Kindom"
    title = "Python Dev"
    started = datetime(2013, 6, 1)
    left = datetime(2014, 10, 1)
    description = [
        "Developing infrastructure for Sift Science card fraud detection (Django, Python).",
        "Building spiders for scraping products (Python, scrapyd)."
    ]


class Caplin(JobMixin):
    company = "Caplin Systems Ltd"
    location = "London, United Kindom"
    title = "Web developer"
    started = datetime(2013, 2, 1)
    left = datetime(2014, 5, 1)
    description = [
        "Performance testing (Scala)",
        "HTML5 trading application for SPOT trading (Kanban process).",
        "Mock server for testing trading platform based on FIX protocol (Java)."
    ]


class MorganStanley(JobMixin):
    company = "Morgan Stanley"
    location = "London, United Kindom"
    title = "Summer Technology Analyst"
    started = datetime(2011, 7, 1)
    left = datetime(2011, 9, 1)
    description = [
        "I solved scalability issues of a SOAP-based messages system for the initial margin calculation (Java and Perl). The new solution uses fle-based method with a batch mode process.",
        "QA (Regression testing, Unit testing) and performance optimization."
    ]


class ABB(JobMixin):
    company = "ABB Corporate Research Center"
    location = "Krakow, Poland"
    title = ".Net Developer (C#)"
    started = datetime(2010, 5, 1)
    left = datetime(2010, 9, 1)
    description = [
        "Developing Import Wizard for TDM/TDMS fles as a part of internal system (C++, C#, WPF).",
        "Designing intuitive UI for quick import."
    ]


class WP7(JobMixin):
    company = "Windows Phone 7 Developer"
    location = ""
    title = ""
    started = datetime(2010, 1, 1)
    left = datetime(2012, 1, 1)
    description = [
        "Creating applications for Windows Phone 7. Publisher name: Lukas M (create.msdn.com).",
        "Developing games using C#, Silverlight and XNA.",
        "Blogging about WP7 (soonstudios.wordpress.com)",
    ]


class SchoolMixin(object):

    def __repr__(self):
        return "{0} - {1}, {2}, {3}, {4}\n{5}\n{6}".format(
            self.started.strftime("%B %Y"),
            self.left if isinstance(self.left, str) else self.left.strftime("%B %Y"),
            self.name,
            self.location,
            self.course,
            "\n".join(self.description),
            "=" * 20
        )

# Education
class Master(SchoolMixin):
    name = "AGH University of Science and Technology in Krakow"
    location = "Poland"
    course = "Master in Computer Science"
    started = datetime(2011, 1, 1)
    left = datetime(2012, 10, 1)
    description = [
        "Thesis topic: Visualisation of difusion and ordering processes in intermetallic alloys.",
        "Developed a tool for physicists that constructs 3D models of beta-Mg2Al3 atoms from simulation (WPF 3D and C#).",
        "Source code at alloysvisualisation.codeplex.com",
    ]

class Bsc(SchoolMixin):
    name = "AGH University of Science and Technology in Krakow"
    location = "Poland"
    course = "Applied Computer Science BSc"
    started = datetime(2007, 9, 1)
    left = datetime(2011, 1, 1)
    description = [
        "Thesis topic: Object technologies implemented in relational databases.",
    ]


Project = namedtuple("Project", "name description")


if __name__ == "__main__":
    experience = [GMG(), Firestartr(), Lyst(), Caplin(), MorganStanley(), ABB()]
    print NAME
    print EMAIL
    print "Experience:"
    for exp in experience:
        print exp

    print "Education:"
    eduction = [Master(), Bsc()]
    for edu in eduction:
        print edu

    print "Projects & Interests:"
    projects = [
        Project("soundly.io", "web tool for adding music to the video (under rewrite form plain js to React and ES6)"),
        Project("Stackoverflow account", "stackoverfow.com/users/336186/lukas"),
        Project("Github account", "github.com/lukasz-madon"),
        Project("Linkedin profle", "https://www.linkedin.com/in/lukaszmadon")
    ]
    for pro in projects:
        print pro

    print "Languages: Python (profcient), Java (profcient), JavaScript (profcient), C# (profcient), C++ (intermediate), C (intermediate), Scala (prior experience), Perl (prior experience), SQL (basic)"
    print "Technologies:    Git, AWS, Heroku, Redis, Angular, React, Django, Flask, PostgresSQL, ASP.Net"
    print "Awards: Semifnalist of Imagine Cup 2012 competition in Game Design track."
    print "Summary: Hacker who started programming at the age of 10. Profcient in Python, C#, JavaScript and other programming languages. Excited to work on open-source."
