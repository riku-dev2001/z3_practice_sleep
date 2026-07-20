# 📊 睡眠時間ログ Dashboard (Streamlit App)

Pandasによるデータ集計とMatplotlibによる可視化ロジック（`main.py`）をベースに、Streamlitを用いて構築した睡眠時間ダッシュボードアプリです。

CSVファイルをアップロードすることで、平均・最長・最短睡眠時間の算出およびグラフ描画・保存を行います。

---

## 🌟 主な機能

* **データ自動集計**: データ件数、平均・最長・最短睡眠時間を集計し、ダッシュボード上にカード表示
* **インタラクティブなグラフ描画**: 
  * 日付飛びによる描画崩れを防ぐインデックスベースの棒グラフ配置
  * 平均睡眠時間の基準線を自動描画
  * レイヤー（`zorder`）制御による見やすいデザイン構成
* **グラフ自動保存（`main.py`）**: スクリプト実行時、生成したグラフを画像ファイル（PNG）としてローカルに保存
* **CSVファイルのダイレクトアップロード**: CSVをドラッグ＆ドロップして即座に集計可能
* **フォールバック機能**: ファイル未選択時はローカルのデフォルトデータ（`data_sleep.csv`）を自動読込

---

## 🛠 使用技術（Tech Stack）

* **Language**: Python 3.13.9
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Matplotlib
* **Web Framework**: Streamlit

---

## 📁 構成ファイル

* `app.py`: Streamlitで構築したWebダッシュボードアプリ
* `main.py`: データ集計およびグラフ生成・画像保存を行うベーススクリプト
* `data_sleep.csv`: デフォルトの睡眠ログデータ

---

## 🚀 起動方法（Local Execution）

1. **リポジトリのクローン**
    ```bash
    git clone https://github.com/riku-dev2001/z3_practice_sleep.git
    cd z3_practice_sleep
    ```

2. **必要なライブラリのインストール**
    ```bash
    pip install pandas matplotlib numpy streamlit
    ```

3. **アプリの起動**
    * **Webアプリとして起動（Streamlit）**
      ```bash
      streamlit run app.py
      ```
    * **スクリプト単体で実行（グラフ保存）**
      ```bash
      python main.py CSVファイル
      ```

---

## 📄 CSVデータのフォーマット

アップロードするCSVファイルは、以下の形式（ヘッダー：`date`, `hours`）に対応しています。

```csv
date,hours
2026-07-01,7.5
2026-07-02,6.0
2026-07-03,8.0
```