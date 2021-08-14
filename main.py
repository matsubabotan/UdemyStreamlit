import streamlit as st
import time

# セクション3
#	12. 

st.title('Streamlit 超入門')
st.write('プログレスバー')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)

'Done!!!'

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
	right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# git 初期化
# git init
# ローカルと紐付け
# git remote add origin https://github.com/matsubabotan/UdemyStreamlit.git

