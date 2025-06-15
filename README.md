# Screenshot Filename Conversion Script

This script is a utility that converts filenames in the format "Screenshot YYYY-MM-DD HHMMSS.png," which are commonly generated on macOS and some other environments, into the format "YYYY-MM-DD\_HHMMSS.png," and copies them into a specified directory.

---

## 📝 File Structure

* `scripts/rename_screenshots.py`: Main execution script

---

## 🔧 Requirements

* Python 3.6 or higher

---

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/rename-screenshots.git
cd rename-screenshots
```

### 2. Run the Script

```bash
python scripts/rename_screenshots.py --input_dir ./input --output_dir ./output
```

### Argument Description

| Argument       | Description                                   |
| -------------- | --------------------------------------------- |
| `--input_dir`  | Directory where the original files are stored |
| `--output_dir` | Directory to save the renamed files           |

---

## 📁 Input/Output Example

### Example Input Filename

```
Screenshot 2025-05-16 110952.png
```

### Example Output Filename

```
2025-05-16_110952.png
```

---

## ⚠️ Notes

* Input filenames must exactly match the format `Screenshot YYYY-MM-DD HHMMSS.png`.
* Files in the output directory with the same name will be overwritten.

---

## 📄 License

[MIT License](./LICENSE)

---

## 🤝 Contributions

Bug reports, feature suggestions, and pull requests are welcome!
