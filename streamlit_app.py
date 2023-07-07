import base64
import os
import streamlit as st

from pathlib import Path
from PIL import Image


# --- WIDTH SETTINGS ---
width_settings = """
<style>
    [data-testid="stMarkdownContainer"] {
        width: 850px
    }
</style>
"""


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'resume.pdf'
profile_pic = current_dir / 'assets' / 'profile.png'
page_icon = current_dir / 'assets' / 'icon.png'
linkedin_icon = current_dir / 'assets' / 'linkedin-icon.png'


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Serhan Sari"
PAGE_ICON = Image.open(page_icon)
NAME = "Serhan Sari"
DESCRIPTION = """
Software Engineer | Data Engineer | DevOps
"""
EMAIL = 'serhan.sari@yahoo.com'
LINKEDIN_URL = "https://www.linkedin.com/in/serhansari/?locale=en_US"

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" />

        </a>'''
    return html_code

gif_html = get_img_with_href(linkedin_icon, LINKEDIN_URL)


st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON,
    # layout="centered"
    )


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=290)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        use_container_width=True
    )
    st.write("📧", EMAIL)
    st.markdown(gif_html, unsafe_allow_html=True)    
    
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
     ✓ 10 Years experience on data-driven software development, testing and deployment\n
     ✓ Strong hands on experience and knowledge in Python and AWS\n
     ✓ Excellent team-player and displaying strong sense of initiative on tasks
    """
)


# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write(
    """
    🧑🏻‍💻 **Programming:** Python, NodeJS, GO, SQL, VBA, UNIX\n
    🖱️ **Front-End:** React, Streamlit, CSS, HTML\n
    🌐 **Restful:** Flask, Django, FastApi\n
    💿 **Databases:** Postgres, DynamoDB, Snowflake, Deta-Space-Cloud\n
    ☁️ **AWS:** EC2, Lambda, API Gateway, S3, SNS, SQS, CloudWatch\n
    🚚 **Deployment:** Terraform, CloudFormation, aws-cdk\n
    💻 **Other:** GrapfQL, Splunk, Git, Jenkins, Docker, New Relic, JIRA
    """
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write('---')

# --- Duke Energy
st.write("💼", "**:orange[Duke Energy] | :green[Software Engineer] | :blue[Jan 2023 - Apr 2023]**")
st.write("***Built reminder and snoozed notification email***")
st.write("""
- Created Kafka Sink and Source connectors for PostgreSQL
- Used splunk to check application logs
- Designed architectural frameworks solutions for SaaS that best suits client web application hosting demands in AWS cloud platform, leveraging AWS
services such as S3, Lambda, API Gateway, SQS, SNS
- Develop key application components using Python (Flask) and RESTful architecture.
- Worked with AWS environment ( Lambda / RDS / DynamoDB)
""")
st.text("")

# --- Capital One
st.write("💼", "**:orange[Capital One] | :green[Software Engineer] | :blue[Mar 2021 - Jan 2023]**")
st.write("***Personal Drive on S3 called userspaces***")
st.write("""
- Proficient with container systems like Docker and container orchestration with Kubernetes and worked with Terraform.
- Managed Docker orchestration and Docker containerization with Kubernetes
- Designed architectural frameworks solutions for SaaS that best suits client web application hosting demands in AWS cloud platform, leveraging AWS
services such as S3, Lambda, API Gateway, SQS, SNS
- Develop key application components using Python (Flask) and RESTful architecture.
- Worked in AWS environment (S3 / EC2 / ECS / Lambda / RDS)
- Developed CLI version of userspaces API
- Performed monitoring and security-related enhancement (New Relic)
- Worked on the CICD pipeline with Jenkins, Git, SonarQube, Eratacode, Checkmarx
- Worked with SQL database (Postgres) and Snowflake
- Used splunk to check application logs
- Integrated New Relic Monitoring into our applications (API, SCAN, PROCESSES)
""")
st.text("")

# --- Progressive
st.write("💼", "**:orange[Progressive] | :green[Data Engineer] | :blue[Jul 2020 - Mar 2021]**")
st.write("***Worked with Enterprise Data Pipeline***")
st.write("""
- Worked in AWS environment (S3 / EC2 / ECS / Lambda / RDS)
- Used PySpark to process batch data pipelines
- Fetched all the snowflake-config- repos in GitHub into a base repo with gitmodules and Automate the CICD pipeline with Jenkins API, Git, and Python
- Worked with Snowflake to clear old entitlements from snowflake via python and pandas
""")
st.text("")

# --- Volkswagen of America
st.write("💼", "**:orange[Volkswagen of America] | :green[Software Engineer] | :blue[Feb 2020 - Jul 2020]**")
st.write("***Developed Volkswagen’s ‘reservation platform’ for online buying called myVW portal***")
st.write("""
- Developed web app solutions using a variety of languages, frameworks, and platforms such as NODE JS, SQL, GraphQL, and HTML.
- Created a product report in CSV and sent it to Datalake in sftp format with NODE JS.
- Data Extracting, Validation, and Correction with Python - Pandas
- Worked on the CI/CD pipeline to deploy to AWS EC2 instances
- Worked with RESTful application on AWS Lambda with Python
- Worked with AWS (Lambda, Fargate, CloudWatch, S3 Buckets, API Gateway, etc..)
- Wrote unittest and integration test with pytest and moto
""")
st.text("")

# --- Capital One
st.write("💼", "**:orange[Capital One] | :green[Software Engineer] | :blue[Jan 2018 - Jan 2020]**")
st.write("***1.Intent Setup Platform Team Member: responsible for developing and deploying new features, legacy application enhancements, and production support under AMP - Acquisition Modernization Program for card***")
st.write("""
- Created serverless slack slash command application to help Segment Leads see campaign status with NODE JS and deployed to AWS - Lambda
- Created serverless Post-App Disclosures rendering with NODE JS, added SNS topic, and deployed to AWS
- Created serverless data comparison application with Python, added SNS topic, and deployed to AWS
- Created serverless campaign-monitoring application with GO, added SNS topic and deployed to AWS
- Wrote Unit and Integration test with GO, Node, and Python
- Implemented New Relic Performance Monitoring to eApis; brandedOffers, displayContents and SolMapping
- Implemented Cyberark Vault for M1-Cloud and ICatalyst DBs
- Performed AMI and storage type migration on AWS
- Worked on a new platform SPICE UI and legacy platforms ICatalyst and M1-Cloud
- Performed Rehydration for EC2 and ASG
- Helped to solve tickets opened by users (Segment Leads) (Production Support)
- Made necessary changes on CFT and Jenkins files
- Wrote python script to find differences in each table between two different databases
- Wrote python script to update database table from another database table
""")
st.write("***2. Investing Platform Conversion Team Member: was responsible for developing and validating data transformation processes from Capital One Investing platform to E*TRADE***")
st.write("""
- Responsible for converting 1.2 million Capital One Investing customers’ sensitive information to E*TRADE.
- Developed validation scripts with Python and Pandas for millions of rows of Capital One’s data
- Developed a time-saving method utilizing Pandas data frame with Python to find discrepancies in data migration during ETL jobs from the Sybase database.
- Used PySpark for real time processing
- Developed SQL queries to extract data from existing sources and transferred the accounts and related data to E*TRADE.
- Involved in processing the streaming data and batch data using Apache Spark
- Imported information from different sources such as AWS S3, and EC2 and converted them into Spark RDD for analyzing data.
- Developed spark scripts via pyspark by adhering to the client’s requirements for ensuring the effective operation
""")
st.text("")

# --- Fannie Mae
st.write("💼", "**:orange[Fannie Mae] | :green[Software Engineer] | :blue[Nov 2016 - Jan 2018]**")
st.write("***Worked in DevSecOPS Team***")
st.write("""
- Worked on DevSecOPS Team’s DAST(Dynamic Analysis Security Testing Scan), SAST(Static Application Security Testing) scan, SCA(Software Composition Analysis) scan, OPA(Open Policy Agent Docker Image and Scan Policies), Invicti(Web-Security Scan), Zeronorth, SSL scan, Eligible Scan, API Scan, SDElements scan, Compliance Scan, and Container Scan.
- Worked with AWS (Lambda, Fargate, CloudWatch, S3 Buckets, API Gateway, etc..)
- Wrote REST end-points and schemas to perform query scans for various scans
- Worked with AWS (Lambda, Fargate, CloudWatch, S3 Buckets, API Gateway, etc..)
- Used CFT(Cloudformation) to add AWS resources and deploy such as lambda, api gateway, etc..
- Worked on deploying applications to AWS environment with Jenkins and UCD
""")
st.text("")

# --- Ucar
st.write("💼", "**:orange[Ucar (University Corporation of Atmospheric Research)] | :green[Software Engineer] | :blue[Dec 2015 - Nov 2016]**")
st.write("***Built Ucar’s Website with Django and Automation with Python***")
st.write("""
- Worked with Grafana for analytics and monitoring of database and website
- Worked with RPM Package Manager on a Linux environment to build packages
- Worked with NGinx for web servicing
- Used Django/Python to build UCAR’s dashboard
""")
st.text("")

# --- Gate Gourmet
st.write("💼", "**:orange[Gate Gourmet] | :green[Business Intelligence Administration Analyst / Developer] | :blue[Oct 2013 - Nov 2015]**")
st.write("***Managed $10+ million/year in the airline’s inventory***")
st.write("""
- Automated Backorder notification application utilizing Python and VBA to notify 500+ hubs in North and South America daily shipment status, resulting in a considerable reduction in man-hours
- Assisted with the automation of the finance department’s manual processes by writing Python scripts to speed processes and maximize accuracy
- Data Migration of new inventory and additional item
- Wrote unittest and integration test with pytest and unittest
- Automated the Microsoft Outlook with VBA to send automated emails daily
""")
st.text("")

# --- LC Waikiki
st.write("💼", "**:orange[LC Waikiki] | :green[VBA Developer] | :blue[Jul 2012 - Aug 2013]**")
st.write("***Developed a customer registration system for a fashion retail company***")
st.write("""
- Create VBA programs to automatically update Excel workbooks, encompassing class & program modules and external data queries.
- Develop GUI interfaces using Open Database Connectivity (ODBC) to connect to Oracle (RDBMS).
- Extensively use Excel functions in development, focusing on read/write integration to databases.
""")


# --- EDUCATION & CERTIFICATION ---
st.write("#")
st.subheader("Education & Certification")
st.write('---')

st.markdown("👨🏻‍🎓 **:orange[Stratford University] | :green[Master of Science in Information Systems] | :red[Falls Church, VA] | :blue[2013-2015]**", unsafe_allow_html=True)
st.markdown(f'{width_settings}👨🏻‍🎓 **:orange[Isik University] | :green[Bachelor of Engineering in Industrial Engineering] | :red[Istanbul, Turkey] | :blue[2007 - 2013]**', unsafe_allow_html=True)
st.write("👨🏻‍🎓", "**:orange[SpringBoard] | :green[Data Science Certification Program] | :red[San Francisco, CA] | :blue[2017]**")
st.write("👨🏻‍🎓", "**:orange[Isik University] | :green[Advanced Excel Certification] | :red[Istanbul, Turkey] | :blue[2012]**")
st.write("👨🏻‍🎓", "**:orange[AWS Certification] | :green[AWS Developer Associate] | :red[Falls Church, VA] | :blue[2018]**")
st.write("👨🏻‍🎓", "**:orange[AWS Certification] | :green[AWS Solution Architect] | :red[Falls Church, VA] | :blue[2018]**")
st.write("👨🏻‍🎓", "**:orange[SCRUM Alliance] | :green[Certified SCRUM Master] | :red[Fort Washington, MD] | :blue[2023]**")


# --- PROJECTS ---
st.write("#")
st.subheader("Projects")
st.write('---')

# --- PROJECT 1 
st.write("📚", "**SpringBoard | Instacart - Kaggle Competition**")
st.write("***Instacart Future Order Analysis; Predicting the consumer’s next purchase order for Instacart. Predicting which item(s) will be in a user’s next order by looking at over 3 Million historical purchase orders from more than 200,000 anonymized Instacart users***")
st.write("""
- Python | Numpy | Pandas | Matplotlib | Seaborn | Statsmodels | Unix | Jupyter Notebook | Linux | Statistical Analysis | CDF & ECDF Functions | Linear Regression | Bayesian Model | Machine Learning
""")

# --- PROJECT 2
st.write("📚", "**Stratford University | Stratbook**")
st.write("***Stratbook is a campus social networking website for Stratford University, in the form of online social networks, are second nature for university students and aspiring young professionals today. Stratbook is a free service that allows you to create an online page to connect with Stratford University students and Professors. You can share Personal Information, education-related books, questions/answers, etc..***")
st.write("""
- JavaScript for front-end | HTML5 and CSS for the static page view | JavaScript library - flex slider | MySQL for database
""")

# --- PROJECT 3
st.write("📚", "**Işık University | Metaheuristic Algorithm Implementation for Vehicle Routing Problem with TABU SEARCH**")
st.write("***The heuristic and metaheuristic search algorithm brings a solution to the vehicle routing problem faced by delivery and collection vehicles. The optimal solution of a VRP instance is the shortest, quickest, or cheapest set of routes assigned to a group of vehicles that satisfies all customers' demands without contravening any instance-specific constraints***")
st.write("""
- MATLAB for coding | Excel for database | VBA for connecting Excel and MATLAB | ARENA for simulation
""")