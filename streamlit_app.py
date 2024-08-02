import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Khởi tạo dataframe rỗng
data = pd.DataFrame(columns=['length', 'deepth', 'sex'])

# Tạo các công cụ nhập liệu
st.title("Data Entry Form")

length = st.slider("Select length", min_value=1, max_value=100, value=1)
deepth = st.slider("Select deepth", min_value=1, max_value=50, value=1)
sex = st.selectbox("Select sex", ["male", "female"])

# Nút để thêm dữ liệu vào dataframe
if st.button("Add Data"):
    new_row = pd.DataFrame({'length': [length], 'deepth': [deepth], 'sex': [sex]})
    data = pd.concat([data, new_row], ignore_index=True)
    st.success("Data added successfully!")
    st.write(data)

# Hiển thị dataframe
st.write("Current Data:")
st.dataframe(data)

