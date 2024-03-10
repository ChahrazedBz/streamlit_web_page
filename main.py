import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="My First Webpage",
    page_icon="👾",
    layout="wide",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css
def local_css(file_name):
    with open(file_name) as f:

        st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)


local_css(r"C:\Users\luxis\OneDrive\Bureau\Python\streamlit.Dev\style\style.css")

lottie_coding = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
)
img_ressource_1 = Image.open(
    r"C:\Users\luxis\OneDrive\Bureau\Python\streamlit.Dev\images\tech.jpg"
)
img_ressource_2 = Image.open(
    r"C:\Users\luxis\OneDrive\Bureau\Python\streamlit.Dev\images\cod.jpeg"
)
with st.container():
    st.subheader("Hi, I am Amina 👋")
    st.title("A Computer Science student ")
    st.write(
        "I am passionate about learming ways to use Python and to write efficient code by learning from good ressources"
    )
    st.write("[Learn More >](https://elzero.org/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        My roadmap of learning was :
        - Learnt The basics of HTML
        - Learnt C from college beside data structure and Algorithms
        - Learnt Python from Youtoub and have some small projects beside tutoriols
        - Learnt Flask and creat my first web page using(Python,Flask,HTML,CSS,JS)
        - in the Process of Learning Streamlit
        """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/@ElzeroWebSchool)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    with st.container():
        st.write("---")
        st.header("Ressources :")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_ressource_1)
        with text_column:
            st.subheader("Tech With Tim")
            st.write(
                """
                Dive into the world of programming,
                software engineering, machine learning,
                and all things tech through my channel! I place a strong focus on Python and JavaScript,
                offering you an array of free resources to kickstart your coding journey and make your mark in the software engineering and programming fields.
                My mission is to deliver the finest quality tech and programming tutorials online,
                ensuring you receive top-notch education right at your fingertips."""
            )
            st.markdown(
                "[Watch Video...](https://youtu.be/OFrLs22MDAw?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm)"
            )
    with st.container():
        image_column1, text_column1 = st.columns((1, 2))
        with image_column1:
            st.image(img_ressource_2)
        with text_column1:
            st.subheader("Codezilla")
            st.write(
                """
                ان شاء الله تهدف قناة لتعليم البرمجة باللغة العربية، مقدمة اليكم من خبراء مجال التعليم و البرمجة، مجانا، و تناسب جميع الاعمار.
                تهدف القناة لتمكين شباب الوطن العربي و اعلاء مستواهم التقني البرمجي و ادراجهم في مجال التكنولوجيا حتى يتمكنوا من مواكبة سرعة التطور التكنولوجي بالعالم و نصبح وطن عربي قوي.
                تمكنك البرمجة من العمل من اي مكان و برواتب ممتازة نظرا لكثرة الطلب في سوق العمل و سرعة نموه.
                """
            )
            st.markdown(
                "[Watch Video...](https://www.youtube.com/redirect?event=channel_header&redir_token=QUFFLUhqbndfa25QRFRSdVJJZTJtZ2pFNzVKX2ZMZU9zd3xBQ3Jtc0trWFpGazl0RmVyb2sxWnlxcEF2dEFKTlRUazVuZGhCcHlSV0p5dmk0ZHhSODY2YmUxTGMybEpkYzVuQ0Ntb1h1N1lydTNheDR3dW5GQVY0ZE5hYlBqTUtSRGNUei1LODJPV2NaQ0sydUl0ODV0SGJ0SQ&q=https%3A%2F%2Fwww.codezilla.courses%2Fintroduction-to-programming)"
            )
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me")
        st.write("##")
        contact_form = """
    <form action="https://formsubmit.co/chahrazedamina191@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>"""

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
