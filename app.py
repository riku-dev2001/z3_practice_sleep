import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import streamlit as st

# 日本語フォントの設定（OS自動判定）
plt.rcParams["font.family"] = "MS Gothic" if os.name == "nt" else "AppleGothic"

# 実行ディレクトリの取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------
# 1. 画面のヘッダー・タイトル設定
# --------------------------------------------------
st.title("📊 睡眠時間ログ Dashboard")
st.write("CSVファイルをアップロードすると、自動で睡眠時間の集計とグラフ化を行います。")

# --------------------------------------------------
# 2. CSVファイルのアップロード機能
# --------------------------------------------------
uploaded_file = st.file_uploader("CSVファイルを選択してください", type=["csv"])

# ファイルが選択されていない場合は、デフォルトの data_sleep.csv を使う
if uploaded_file is None:
    default_path = os.path.join(BASE_DIR, "data_sleep.csv")
    if os.path.exists(default_path):
        target_file = default_path
        st.info("💡 デフォルトデータ (`data_sleep.csv`) を表示しています。")
    else:
        target_file = None
else:
    target_file = uploaded_file

# --------------------------------------------------
# 3. データの集計とグラフ描画
# --------------------------------------------------
if target_file is not None:
    try:
        # データ読み込みと前処理
        df = pd.read_csv(target_file)
        df["date"] = pd.to_datetime(df["date"], format='mixed')
        df = df.sort_values("date").reset_index(drop=True)

        # 指標（メトリクス）の計算
        mean_hours = df['hours'].mean()
        max_hours = df['hours'].max()
        min_hours = df['hours'].min()

        # --- 概要カードの表示 ---
        st.subheader("--- データ概要 ---")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("データ数", f"{len(df)} 件")
        col2.metric("平均睡眠時間", f"{mean_hours:.1f} 時間")
        col3.metric("最長睡眠時間", f"{max_hours:.1f} 時間")
        col4.metric("最短睡眠時間", f"{min_hours:.1f} 時間")

        st.divider() # 区切り線

        # --- Matplotlibでグラフを作成 ---
        st.subheader("📈 睡眠時間グラフ")
        fig, ax = plt.subplots(figsize=(9, 4.5))

        # 棒グラフ
        ax.bar(df.index, df["hours"], color="skyblue", edgecolor="navy", label="睡眠時間", zorder=2)
        ax.set_xticks(df.index)
        ax.set_xticklabels(df["date"].dt.strftime('%Y-%m-%d'), rotation=45)

        # 平均線
        ax.axhline(y=mean_hours, color="red", linestyle="--", label=f"平均：{mean_hours:.1f}時間", zorder=3)

        # Y軸目盛り
        y_max = int(max_hours)
        ax.set_yticks(np.arange(0, y_max + 3, 1))

        # 装飾
        ax.set_ylabel("時間 (h)", fontsize=11)
        ax.grid(True, linestyle=":", alpha=0.6, axis="y", zorder=1)
        ax.legend(loc="upper left", fontsize=10)
        plt.tight_layout()

        # Streamlit画面上にグラフを出力！
        st.pyplot(fig)

    except Exception as e:
        st.error(f"データの処理中にエラーが発生しました: {e}")
else:
    st.warning("`data_sleep.csv` が見つかりません。ファイルをアップロードしてください。")