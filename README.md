# **__112_pythonLesson_LJ**
112年致理科大Python大數據資料探勘實務班

安裝 

     python3.10.11 (不要選最新版的)
     vs_code
     github_desktop

vscode開啟專案，不用安裝extention(git、dev container)

    pip install requests pandas streamlit

命令選擇區>display>configue display language選擇改變語言(繁中)\
設定>設定>after delay 自動存檔

- 下載資料 requests (open source)
- 整理資料 pandas
- 顯示、互動資料
     上傳資料 streamlit
          *st.write()* 
---
雲端>github>repo>codespace> \
本地端要下載vs code 

     設定>open in VScode desktop

下次可直接開啟VS code

     左下角><codespace
     重新連接codespace 選取之前連過的即可
---
檔案更新不同步相互衝突

     >>解決衝突方法
     >>直接砍掉原本codespace
     >>重建一個新的codespace
     >>要重新安裝套件 pip list 檢視目前安裝套件
     >>pip install requests pandas streamlit
     >>紀錄 過去安裝的套件 pip freeze >requirements.txt
---
     >>dev container
     >>隱藏檔 (.json)
     >>刪掉 「//」 打開 
     "postCreatCommand":"pip3  install -- user -r requirement.txt" 
