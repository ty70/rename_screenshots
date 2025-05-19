# rename_screenshots.py
# ---------------------
# 概要:
# スクリーンショットのファイル名（例: スクリーンショット 2025-05-16 110952.png）を
# "2025-05-16_110952.png" の形式にリネームして出力ディレクトリへコピーするスクリプト。
#
# 使用法:
# python rename_screenshots.py --input_dir ./input --output_dir ./output
#
# 引数:
# --input_dir: リネーム対象のファイルが保存されているディレクトリ
# --output_dir: リネーム後のファイルを保存するディレクトリ

import os
import re
import argparse
import shutil

# 引数パーサの設定
parser = argparse.ArgumentParser(description="スクリーンショットのファイル名を日付+時間にリネーム")
parser.add_argument('--input_dir', required=True, help="入力ディレクトリのパス")
parser.add_argument('--output_dir', required=True, help="出力ディレクトリのパス")
args = parser.parse_args()

input_dir = args.input_dir
output_dir = args.output_dir

# 正規表現パターンの定義
pattern = re.compile(r'^スクリーンショット (\d{4}-\d{2}-\d{2}) (\d{6})\.png$')

# 出力ディレクトリの作成（存在しなければ）
os.makedirs(output_dir, exist_ok=True)

# 入力ディレクトリ内のファイルを処理
for filename in os.listdir(input_dir):
    match = pattern.match(filename)
    if match:
        date_part = match.group(1)
        time_part = match.group(2)
        new_filename = f"{date_part}_{time_part}.png"

        src_path = os.path.join(input_dir, filename)
        dst_path = os.path.join(output_dir, new_filename)

        shutil.copy2(src_path, dst_path)
        print(f"Renamed: {filename} -> {new_filename}")
