import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('🎈 Hello world app')

st.write('Hello world!')

with st.sidebar:
  st.header("About app")
  st.write("This is my first app")

st.subheader("st.columns")
col1,col2 = st.columns(2)
with col1:
  x = st.slider("Choose an x value",1,10)
with col2:
  st.write("The value of :blue[x]",x)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

st.title("JSONPlaceholder API Viewer")

# エンドポイント選択
endpoint = st.selectbox("取得したいデータタイプを選んでください", [
    "posts", "comments", "albums", "photos", "todos", "users"
])

# ID入力（任意）
item_id = st.text_input("IDを指定（空欄なら全件）", "")

# APIリクエスト
if st.button("APIを実行"):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}/{endpoint}"
    if item_id.strip():
        url += f"/{item_id.strip()}"

    with st.spinner("データ取得中..."):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            st.success("取得成功！")

            # 整形表示
            st.subheader("JSONデータ")
            st.json(data)

        except requests.exceptions.RequestException as e:
            st.error(f"API取得に失敗しました: {e}")

st.title("🐶 ランダム犬画像を表示（Dog API）")

num = st.slider("画像の枚数", min_value=1, max_value=10, value=3)

# 複数枚取得
images = []
for _ in range(num):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    images.append(data["message"])

# 表示
for idx, url in enumerate(images, 1):
    st.image(url, caption=f"Dog #{idx}", use_container_width=True)
