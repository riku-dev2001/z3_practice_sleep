import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# 文字設定
plt.rcParams["font.family"] = "MS Gothic" if os.name == "nt" else "AppleGothic"

# CSVファイルのパスを設定する
BASE_DIR = os.path.dirname(__file__) # pyファイルの場所
file_path = os.path.join(BASE_DIR, "data_sleep.csv") # pyファイルの場所+CSVファイル名でパスを設定

# 引数でファイル名が指定されない場合は、同ディレクトリのデフォルトCSVを読み込む
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = file_path

try:
    # グラフ用データ
    df = pd.read_csv(filename)
    # dateの調整
    df["date"] = pd.to_datetime(df["date"], format='mixed')
    df = df.sort_values("date").reset_index(drop=True)

    # データの情報をターミナルに表示
    print("--- データ概要 ---")
    print(f"データ数 : {len(df)}件")
    print(f"平均睡眠時間 : {df['hours'].mean():,.1f}時間")
    print(f"最長睡眠時間 : {df['hours'].max():,.1f}時間")
    print(f"最短睡眠時間 : {df['hours'].min():,.1f}時間")
    print("--------------------")

    # グラフ描画
    plt.bar(df.index, df["hours"], color="skyblue", edgecolor="navy", label="睡眠時間(時間)", zorder=2)
    plt.xticks(df.index, df["date"].dt.strftime('%Y-%m-%d'), rotation=45)

    # フラフの調整
    # グラフに平均を表示
    mean = df['hours'].mean()
    plt.axhline(y=mean, color="red", linestyle="--", label=f"平均：{mean:,.1f}時間")

    #縦軸目盛りの調整
    y_max = df["hours"].max()
    # 最小値から最大値の「＋1」の範囲まで、1刻みで目盛りを作る
    plt.yticks(np.arange(0, y_max + 3, 1))
    
    # グラフの説明
    plt.grid(True, linestyle=":", alpha=0.6, axis="y")
    plt.legend(loc="upper left", fontsize=10) # 左上に説明を出す
    plt.tight_layout() # 文字のレイアウト調整
    
    # グラフの表示
    save_path = os.path.join(BASE_DIR, "graph.png") # 保存先
    plt.savefig(save_path) # 保存
    plt.show() # 表示（show()でバッファがクリアされるから、保存後にやる）

except Exception as e:
    # エラー内容を表示
    print(f"データの処理中に予期せぬエラーが発生しました: {e}")