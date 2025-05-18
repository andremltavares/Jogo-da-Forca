# 🎮 Python Hangman Game

A complete Hangman implementation with robust validation and category system.

## ✨ Features
| Feature                | Status         |
|------------------------|----------------|
| Interactive menu       | ✅ Implemented |
| 3 word categories      | ✅ Implemented |
| 3 difficulty levels    | ✅ Implemented |
| Scoring system         | ✅ Implemented |
| Input validation       | ✅ Improved    |
| ASCII Hangman art      | ✅ Implemented |
| Game history           | ✅ New         |
| Detailed statistics    | ✅ New         |

## 🐛 Recent Fixes
```diff
+ Fixed main menu validation
+ Numeric option comparison
+ Clearer error messages
+ History persistence (fix)
```

## 📦 Project Structure
```
jogo-da-forca/
├── jogo_da_forca.py    # Main code
├── historico.py    # History management
├── historico.json    # Game data (auto-generated)
├── .gitignore    # Ignores temporary files
├── README.md           # Documentation
```

## 🚀 How to run
```bash
# 1. Clone repository
git clone https://github.com/andremltavares/Jogo-da-Forca.git

# 2. Enter folder
cd jogo-da-forca

# 3. Run game
python jogo_da_forca.py

🎮 Menu
Key	Action
1	Quick Start
2	Choose Category
3	Set Difficulty
4	View complete statistics
5	About Game
6	Exit
```

