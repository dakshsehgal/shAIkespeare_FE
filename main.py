import streamlit as st
from streamlit.components.v1 import html
from PIL import Image

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

button_style = """<style>

.stApp {
    background-color: black;
}

.stButton > button {
color: white;

background: black;
border-color: black;
width: 100px;
}

.stButton > button:hover {
color: red;
border-color: black;
}

.stButton > button:focus {
border-color: black;
background: black;

}

.stButton > button:focus:not(:active) {
    background: black;
    border-color: black;
}

</style>

"""
st.markdown(button_style, unsafe_allow_html=True)
tempest = Image.open('images/macbeth_long.jpg')
# convert to href clickable image

st.image(tempest)

c1,c2,c3,c4,c5 = st.columns(5)

if c3.button("macbeth"):
    nav_page("macbeth")


image = Image.open('images/kinglear.jpg')
st.image(image)

d1, d2, d3, d4, d5 = st.columns(5)
# st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
if d3.button("The Tempest"):
    nav_page("tempest")