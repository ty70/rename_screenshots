# スクリーンショットファイル名変換スクリプト

このスクリプトは、macOS や一部の環境で生成される「スクリーンショット YYYY-MM-DD HHMMSS.png」形式のファイル名を「YYYY-MM-DD\_HHMMSS.png」に変換し、指定したディレクトリへコピーするユーティリティです。

---

## 📝 ファイル構成

* `scripts/rename_screenshots.py`: メインの実行スクリプト

---

## 🔧 必要な環境

* Python 3.6 以上

---

## 🚀 インストールと使用方法

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourname/rename-screenshots.git
cd rename-screenshots
```

### 2. スクリプトの実行

```bash
python scripts/rename_screenshots.py --input_dir ./input --output_dir ./output
```

### 引数の説明

| 引数             | 説明                    |
| -------------- | --------------------- |
| `--input_dir`  | 元のファイルが保存されているディレクトリ  |
| `--output_dir` | リネーム後のファイルを保存するディレクトリ |

---

## 📁 入出力例

### 入力ファイル名（例）

```
スクリーンショット 2025-05-16 110952.png
```

### 出力ファイル名（例）

```
2025-05-16_110952.png
```

---

## ⚠️ 注意事項

* 入力ファイルは `スクリーンショット YYYY-MM-DD HHMMSS.png` の形式に正確に一致している必要があります。
* 同名ファイルが出力ディレクトリに存在する場合は上書きされます。

---

## 📄 ライセンス

[MIT License](./LICENSE)

---

## 🙋‍♂️ 貢献

バグ報告・機能提案・プルリク歓迎です！
