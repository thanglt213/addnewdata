import streamlit as st
import pandas as pd

# Kiểm tra nếu 'data' chưa tồn tại trong session state thì tạo mới
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['A', 'B'])

# Hiển thị form để nhập dữ liệu mới
with st.form(key='data_entry_form'):
    input_a = st.text_input('Nhập giá trị cho A:')
    input_b = st.text_input('Nhập giá trị cho B:')
    submit_button = st.form_submit_button(label='Thêm vào bảng')

# Xử lý khi người dùng nhấn nút "Thêm vào bảng"
if submit_button:
    # Thêm dữ liệu vào dataframe
    new_data = pd.DataFrame({'A': [input_a], 'B': [input_b]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

# Hiển thị dataframe
st.write(st.session_state.data)
