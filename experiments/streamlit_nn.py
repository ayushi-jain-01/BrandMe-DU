import streamlit as st
import time as t

# image
st.image("download.png")

# title- used to add the title of an app
st.title("this  si the title")

# header
st.header("this is the header")

# sub-header
st.header("this is the sub-header")

# info message
st.info("info details")

# warning message 
st.warning("This is the warning message")

# error message
st.error("This is  the error  message")

# success message 
st.success("this si the success message")

# write
st.write("writeeeeeeee")
# this is diff
st.write("Range(50)")
# this is diff from above
st.write(range(50))

# markdown
# here the diff is as soon as we add # with space to statement the font size changes and # without space nothing changes andddd as we increase the no. of # with space the size decreases gradually.
st.markdown("this is markdown")
st.markdown("# this is markdown")
st.markdown("##this is markdown")
st.markdown("## this is markdown")
st.markdown("### this is markdown")
# can get any emoji too
st.markdown(":moon:")

# text
st.text("this  si the text function")

# caption
st.caption("This is the caption")

# mathematical expression
st.latex(r''' a+b x^2+c''')

# widget

# checkbox
st.checkbox("checkbox")

# button
st.button("button")

# radio widget
st.radio("radio widget",["Male","female","trans"])

# select box
st.selectbox("select box",["apple","banana","mango"])

# multiselect
st.multiselect("select box",["apple","banana","mango"])

# selectslider
st.select_slider("Rating",["bad","good"])

# slider
st.slider("Pick no.",0,30)

# number_input
st.number_input("Pick a no",0,30)

# text inout 
st.text_input("e-mail")

# date input
st.date_input("opening date")

# time input
st.time_input("time enter")

# text area
st.text_area("text area")

# upload_file
st.file_uploader("upload  your file/folder")

# color_picker
st.color_picker("pick")

# progree
st.progress(50)

# spinner function
# this  will load the timer till 10sec
with st.spinner("Just wait"):
    t.sleep(2)
#  after 2 seconds only the next program statement will be executed or any other time specified not before that

# balloon
st.balloons()

# sidebar
st.sidebar.title("WELCOME")
st.sidebar.text_input("Enter e-mail")
st.sidebar.text_input("Enter password")
st.sidebar.button("Submit")

# Data Visualization
# using library panda
import pandas as pd
import numpy as np
st.title("BarChart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("LineChart")
st.line_chart(data)
st.title("AreaChart")
st.area_chart(data)