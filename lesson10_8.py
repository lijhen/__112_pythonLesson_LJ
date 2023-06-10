import requests
import pandas as pd
import streamlit as st
#下載youbike的即時資料
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:
    print("連線成功")
    all_data = response.json()
    print(type(all_data))
else:
    print(f"連線失敗:{response.status_code}")

#將資料轉成dataFrame
dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
dataFrame.columns = ['站點','總車數','可借數','行政區',
                     '時間','地址','可還','狀態']
df1 = dataFrame.set_index('站點') #改了index，要有變數接收全新的資料
group_data = dataFrame.groupby('行政區').sum()
areas = df1['行政區'].unique()


min,max = st.slider('選擇可借數量：', 0, 100,(1,100))
mask =( df1['可借數'] <= max ) & (df1['可借數'] >= min )
mask_dataFrame = df1[mask]
count_sna = mask_dataFrame['可借數'].count()
options = st.selectbox('行政區：',areas)
st.write('下列符合條件的樣站共', count_sna,'站')
st.dataframe(mask_dataFrame)


