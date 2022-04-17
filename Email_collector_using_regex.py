# Email collector from given string
import re

str = """Skip to main content
Enable accessibility for
visually impaired
Open the accessibility
menu
Accessibility Widget
Fests 2022
Alumni
Insights
News & Events
Blog
Careers
Research
Conferences
Webinars
Publications
Library
Login
|
Contact Us
APPLY ONLINE
ABOUT US

ACADEMIC UNITS

FACULTY

PROGRAMMES

INTERNATIONAL
PLACEMENTS
CAMPUS LIFE
ADMISSIONS

Enquire Now
Contact Us
Alliance University
Central Campus
Chikkahagade Cross, Chandapura - Anekal Main Road, Anekal, Bengaluru – 562 106, Karnataka, India.

Get Route Map

Phone : +91 80 4619 9000 / 9100 / +91 80 4129 9200

Fax : +91 80 4619 9099

E-mail : enquiry@alliance.edu.in

City Campus 1
19th Cross, 7th Main, BTM 2nd Stage, N.S. Palya, Bengaluru – 560 076, Karnataka, India.

Get Route Map

Phone : +91 80 26786020 / 21 / +91 80 26789749

Office of Admissions
Undergraduate

+91 96200 09825

+91 91084 42143

Postgraduate

+91 98860 02500

+91 99002 29974



Executive Education

+91 96327 08676

City Campus 2
2nd Cross, 36th Main, Dollars Scheme, BTM 1st Stage, Bengaluru – 560 068, Karnataka, India

Get Route Map

Phone : +91 80 26681444 / 4372

Fax : +91 80 26782048

Enquiry
Feedback

Select Institute Applying For
Enter Full Name
Enter Email Address
Enter Mobile Number
Enter State
Enter City

Select Course
Type Your Enquiry Here
By clicking Submit, you agree to our Terms & Conditions, Privacy Policy and Disclaimer, including our Cookie Use.

Vice-Chancellor
Dr. Anubha Singh

Phone : +91 80 4619 9100 / +91 80 4129 9200

E-mail : vc@alliance.edu.in

Registrar
Dr. Nivedita Mishra

Phone : +91 80 4619 9100 / +91 80 4129 9200

E-mail : registrar@alliance.edu.in

Admissions
Phone : +91 80 4619 9010

E-mail : admissions@alliance.edu.in

Placements
Phone : +91 80 4619 9066

E-mail : placement@alliance.edu.in

International Affairs
Phone : +91 80 4619 9000 / 9100

E-mail : oia@alliance.edu.in

Human Resources Department
Phone : +91 80 4619 9083

E-mail : hrd@alliance.edu.in

Alumni Relations
Phone : +91 98451 17152

E-mail : alumni@alliance.edu.in

Student Verification
Office of Registrar (Examination & Evaluation)
Phone : +91 80 4619 9100 / +91 80 4129 9200

E-mail : edu.verify@alliance.edu.in

ABOUT
The UniversityRanking & AccoladesUniversity OfficersNews & Events
SCHOOLS
Alliance School of BusinessAlliance College of Engineering & DesignAlliance School of LawAlliance Ascent CollegeAlliance School of Liberal Arts
PROGRAMMES
UndergraduatePostgraduateDoctoralExecutive Education
ADMISSIONS
Admission ProcessCourse & Fee StructurePayment OptionsUniversity Brochures
Alliance University
IMPORTANT LINKS
AACSBAnti-Ragging PolicyContact UsCOVID-19 UpdatesDownloadsFaculty & Staff LoginIACBE
IMPORTANT LINKS
NIRF - EngineeringNIRF - ManagementResultsRoute MapStudent LoginStudent VerificationWebmail360° Campus Tour
OTHERS
SitemapDisclaimerPrivacy PolicyTerms & Conditions
Helpline
080 4619 9000 / 9100 / 080 4129 9200

FOLLOW US


 Alliance University

Designed and Developed by Sterco Digitex
"""

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)


def get_number_of_elements(list):
    count = 0
    for element in list:
        count = count + 1
    return count


f = open("tut96.txt", "w")
num = 1

for items in email:
    f.write(f"Email_{num}" + " " + "-" + " " + items + "\n")
    if num <= get_number_of_elements(email):
        num = num + 1
f.close()
