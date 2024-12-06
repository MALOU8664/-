import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_infection_trend(df, threshold):
    total_cases = df.groupby('dateId')['confirmedCount'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(total_cases.index, total_cases.values, marker='o')
    plt.title('总感染趋势')
    plt.xlabel('日期')
    plt.ylabel('累计确诊人数')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()

def plot_city_infection_trend(df, threshold):
    plt.figure(figsize=(10, 6))
    for city in df['id'].unique():
        city_df = df[df['id'] == city]
        plt.plot(city_df['dateId'], city_df['confirmedCount'], label=city)
    plt.title('各城市感染趋势')
    plt.xlabel('日期')
    plt.ylabel('累计确诊人数')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()

def plot_high_risk_areas(df, threshold):
    high_risk_cities = df[df['confirmedCount'] > threshold]['id'].unique()
    plt.figure(figsize=(10, 6))
    for city in df['id'].unique():
        city_df = df[df['id'] == city]
        if city in high_risk_cities:
            plt.plot(city_df['dateId'], city_df['confirmedCount'], label=city, linestyle='--', linewidth=2, color='red')
        else:
            plt.plot(city_df['dateId'], city_df['confirmedCount'], label=city)
    plt.title('高风险区域')
    plt.xlabel('日期')
    plt.ylabel('累计确诊人数')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()