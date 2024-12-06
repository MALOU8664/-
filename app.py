import streamlit as st
import pandas as pd
from data_processing import load_data, clean_data, sort_data
from data_analysis import plot_total_infection_trend, plot_city_infection_trend, plot_high_risk_areas

def main():
    st.title('新冠病毒感染分析')
    st.markdown("本应用用于展示新冠病毒感染相关数据。用户可以上传CSV文件，并进行绘图分析。")

    uploaded_file = st.sidebar.file_uploader("上传CSV文件", type=['csv'])
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        df = clean_data(df)
        df = sort_data(df)

        start_date = st.date_input('开始日期', min_value=df['dateId'].min(), max_value=df['dateId'].max())
        end_date = st.date_input('结束日期', min_value=df['dateId'].min(), max_value=df['dateId'].max())
        if start_date > end_date:
            st.error('开始日期不能晚于结束日期！')
        else:
            filtered_df = df[(df['dateId'] >= start_date) & (df['dateId'] <= end_date)]

            threshold = st.slider('感染人数阈值', min_value=0, max_value=int(df['confirmedIncr'].max()), value=10)

            st.subheader('总感染趋势')
            plot_total_infection_trend(filtered_df, threshold)

            st.subheader('各城市感染趋势')
            plot_city_infection_trend(filtered_df, threshold)

            st.subheader('高风险区域')
            plot_high_risk_areas(filtered_df, threshold)

