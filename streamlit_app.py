import streamlit as st
import pandas as pd
import os

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Đường dẫn tệp CSV
DATA_FILE = 'data.csv'

# Hàm khởi tạo dataframe hoặc tải dữ liệu từ tệp
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=['Height', 'Weight', 'Sex'])

# Hàm lưu dữ liệu vào tệp
def save_data(data):
    data.to_csv(DATA_FILE, index=False)

# Hàm thêm dữ liệu vào dataframe
def add_data(height, weight, sex):
    global data
    new_data = pd.DataFrame({'Height': [height], 'Weight': [weight], 'Sex': [sex]})
    data = pd.concat([data, new_data], ignore_index=True)
    save_data(data)

# Tải dữ liệu từ tệp hoặc khởi tạo dataframe mới
data = load_data()

# Widget nhập liệu
st.title("Nhập liệu nhân khẩu học")

height = st.slider("Chiều cao (cm)", min_value=110, max_value=200)
weight = st.slider("Cân nặng (kg)", min_value=20, max_value=120)
sex = st.selectbox("Giới tính", options=["Male", "Female"])

# Nút thêm dữ liệu
if st.button("Thêm dữ liệu"):
    add_data(height, weight, sex)
    st.success("Dữ liệu đã được thêm!")

# Hiển thị dữ liệu hiện tại
st.write("Dữ liệu hiện tại:")
st.write(data)
