# Import necessary libraries
import base64
import streamlit as st

st.set_page_config(page_title="Resume", 
                page_icon=":wave:", 
                layout="wide")

# Header
st.title("Trideep Saha")

with open("image/trideep.jpg", "rb") as f:
    self_image = base64.b64encode(f.read()).decode(
        "utf-8"
    )
    
    st.sidebar.markdown(
        f"""
        <div style="display:table;margin-top:-20%;margin-left:20%;">
            <img src="data:image/trideep.jpg;base64, {self_image}" width="150" height="250">
        </div>
        """,
        unsafe_allow_html=True,
    )

# Personal Information
st.write("Location: Bolpur Sriniketan, West Bengal, India")
linkedin_link = "[LinkedIn](https://www.linkedin.com/in/trideep-saha-b90950216/)"
st.write("Email: trideepsaha009@gmail.com | Phone: +918670914733 | " + linkedin_link)

# Summary
st.header("Summary")
st.write("Self-motivated and proven track record as an Account Assistant at CS bottling plant cum warehouse,\
    demonstrating a commitment to work-driven decision-making. Physics Graduate with a passion for Python and data-driven solutions.\
    Currently pursuing a Data Science certification at AlmaBetter,\
    engaged in comprehensive Data Science training, gaining hands-on experience in Python, Machine Learning, \
    Analytics and Web Scraping. \
    Looking for immediate availability for new opportunities.")

# Skills
with st.sidebar:
    st.header("Skills")
    st.write("• Python")
    st.write("• Web Scraping")
    st.write("• Backend Development")
    st.write("• Machine Learning")
    st.write("• Data Analytics")
    
# Experience
st.header("Work Experience")

# with open("image/bottling.jpg", "rb") as f:
#     bottling_image = f.read().decode("utf-8")
st.subheader("Spirit Bottling Manufacturing Plant cum Warehouse (June 2016 - Nov 2023)")
st.image("image/bottling.jpg", width=200, use_column_width=False)
st.markdown("• Account Assistant")
st.markdown(
    "- Managed financial transactions and maintained accounts for Sarojit Kumar Dey CS bottling plant cum warehouse, ensuring accuracy and compliance with financial regulations.")
st.markdown(
    "- Implemented efficient production processes, contributing to the optimization of financial operations and enhancing overall workflow efficiency.")



st.header("Competency Challenge")
st.subheader("AlmaBetter - Data Science Certification (Jun 2023 - Present)")
st.markdown(
    "- Engaged in comprehensive Data Science training, acquiring proficiency in Python, Machine Learning, Analytics, and Web Scraping.")
st.markdown(
    "- Successfully completed the **Competency Challenge**, demonstrating problem-solving skills and mastery over core concepts.")

# Education
with st.sidebar:
    st.header("Education")
    st.write("• The University of Burdwan - Bachelor of Science (BS) in Physics")



# Projects
st.header("Projects")

# Project 1
st.subheader("Chat-With-Website Project: Conversational Web Experience")
st.markdown("#### Tech Stack:")
st.write("• **Streamlit** | **LangChain** | **Google Generative AI** 🤖")

st.markdown("#### Project Overview:")
st.markdown(
    "Imagine a dialogue with a website for instant answers! Our Chat-With-Website extracts information using LangChain and Google Generative AI. Users can interact, ask questions, and receive responses based on the website's content."
)
st.video("image/uploadlinked.mp4", format="video/mp4")
st.write("➡ Project Link: https://github.com/saha-trideep/Chat-With-Website")

# Project 2
st.subheader("Web Scraping LinkedIn Job Data and Analyze it with Python")
st.image("image/selenium.png", width=200, use_column_width=False)
st.markdown("• **Python** | **Selenium** | **BeautifulSoup** | **Pandas**")
st.markdown("• Forge a dynamic and robust **web scraping mechanism** capable of harvesting data science job postings from diverse online platforms.")
st.markdown("• Extract and cleanse key information such as job titles, company names, descriptions, qualifications, salaries, locations, and deadlines.")
st.write("➡ Project Link: https://colab.research.google.com/drive/1bBLaZc5GvQf-s7l8SottlWFaenhg_JG_?usp=sharing")

# Project 3
st.subheader("Breast Cancer Diagnosis App: Virtual Assistant for Medical Professionals")
st.markdown("#### Tech Stack:")
st.markdown("• **Python** | **Streamlit** | **Scikit-learn**")
st.markdown("#### Project Overview:")
st.markdown("Here's the gist: you input some measurements, and the app uses fancy machine learning tricks to predict if the lump is harmless or might need some attention. It even shows a radar chart with the data and tells you the chances of it being either good or not-so-great.")
st.image("image/regressor.png", width=500, use_column_width=True)
st.write("➡ Demo Link:[Streamlit Community Cloud](<https://8vcndpz6vixttytx7bdcny.streamlit.app/>).")
st.write("➡ Project Link: https://github.com/saha-trideep/Regression-Model-App-Streamlit/blob/main/README.md")


# Project 4
st.subheader("Clean Blog Project: Empowering Content Creation with Python and Flask")
st.image("https://i0.wp.com/abitofpopmusic.com/wp-content/uploads/2014/10/taylor-swift-1989-album-cover.png?ssl=1",
        width=200, use_column_width=False)
st.markdown("#### Tech Stack:")
st.markdown('• **Python** | **Flask** | **Bootstrap** | **SQLite** | **SQLAlchemy**')
st.markdown("#### Project Overview:")
st.markdown(
    "Our Clean Blog project, built with Python and Flask, offers a dynamic content creation platform. The front-end design, implemented using Bootstrap, provides an engaging user experience. Data is efficiently stored in an SQLite database, with SQLAlchemy handling database operations. Passwords are hashed and salted for enhanced security, ensuring user data protection."
)
st.markdown(
    "visiting this link: [Clean Blog Demo](https://clean-blog-c7g3.onrender.com)"
)
st.write("➡ Project Repository Link: https://github.com/saha-trideep/trideep-blog/blob/master/README.md")

# Project 5

############################################
# Licenses & Certifications
with st.sidebar:
    st.header("Licenses & Certifications")
    # JSON data
    #     "@context":"https://w3id.org/openbadges/v2",
    #     "type":"Assertion",
    #     "id":"https://api-lb.appfurther.io/v2/ims/09158917428417",
    #     "badge":"https://api-lb.appfurther.io/v2/ims/badgeClass/09158917428417",
    #     "image":"https://api-lb.appfurther.io/v2/ims/image/09158917428417",
    #     "verification":{
    #     "type":"HostedBadge"
    #     },
    #     "issuedOn":"2023-09-29",
    #     "recipient":{
    #     "type":"email",
    #     "hashed":False,
    #     "identity":"trideepsaha009@gmail.com"
    #     },
    #     "evidence":[]
    # }
    license_data2={
    "@context":"https://w3id.org/openbadges/v2",
    "type":"Assertion",
    "id":"https://api-lb.appfurther.io/v2/ims/23902806792796",
    "badge":"https://api-lb.appfurther.io/v2/ims/badgeClass/23902806792796",
    "image":"https://api-lb.appfurther.io/v2/ims/image/23902806792796",
    "verification":{
    "type":"HostedBadge"
    },
    "issuedOn":"2024-02-21T00:00:00.000Z",
    "recipient":{
    "type":"email",
    "hashed":False,
    "identity":"trideepsaha009@gmail.com",
    },
    "evidence":[]
    }
# Display license details
    st.subheader("CodeStrom Challenge (AlmaBetter)")
    st.write(f"Issued on: {license_data2['issuedOn']}")
    st.write(f"Recipient: {license_data2['recipient']['identity']}")
    st.image(license_data2['image'], caption='Badge Image', use_column_width=True)