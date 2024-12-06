import pandas as pd

def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"数据加载失败: {e}")
        return None

def clean_data(df):
    if df is not None:
        df = df.dropna()
        return df
    return None

def sort_data(df):
    if df is not None:
        df = df.sort_values(by=['dateId'])
        return df
    return None