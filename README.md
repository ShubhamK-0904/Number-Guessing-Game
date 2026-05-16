# 🎲 Number Guessing Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Game-FF6B6B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Console-000000?style=for-the-badge&logo=gnometerminal&logoColor=white" />
  <img src="https://img.shields.io/badge/Beginner%20Friendly-4CAF50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

## 🎲 Overview

**Number Guessing Game** is a simple yet engaging Python console game where players guess a random number between 1 and 100. Features attempt tracking (limited to 10 tries), real-time feedback on each guess (higher/lower hints), and win/loss messaging. Perfect for learning game logic, loops, conditionals, and user input handling in Python.

**Perfect for:** Learning Python basics, game logic, loops, conditionals, beginner programming.

---

## ✨ Key Features

- 🎯 **Core Gameplay**
  - Random number generation
  - Number range: 1-100
  - Player guesses number
  - Win/lose conditions

- 💭 **Smart Feedback**
  - "Too high" hints
  - "Too low" hints
  - Attempt tracking
  - Remaining tries display

- 📊 **Attempt Management**
  - Maximum 10 attempts
  - Attempt counter
  - Progress display
  - Game over detection

- 🏆 **Win/Loss Handling**
  - Victory message
  - Game over message
  - Option to replay
  - Score display

- 🎮 **User Experience**
  - Clear instructions
  - Friendly messages
  - Input validation
  - Replay option

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Core Libraries** | random, input |
| **Game Logic** | Conditionals, loops |
| **User Interface** | Console/Terminal |

---

## 📋 Requirements

```
Python 3.8 or higher
No external dependencies required
```

---

## 🚀 Quick Start

### 1. **Clone Repository**
```bash
git clone https://github.com/ShubhamK-0904/Number-Guessing-Game.git
cd Number-Guessing-Game
```

### 2. **Run Game**
```bash
python number_guessing_game.py
```

### 3. **Play!**
```
Welcome to Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it.

Attempt 1/10: Enter your guess: 50
Too high! Try a lower number.

Attempt 2/10: Enter your guess: 25
Too low! Try a higher number.
...
```

---

## 💻 Code Implementation

### **Basic Game**
```python
import random

def play_game():
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            # Check guess
            if guess == secret_number:
                print(f"\n🎉 You won! The number was {secret_number}.")
                print(f"You took {attempts} attempt(s)!")
                return True
            elif guess < secret_number:
                print("Too low! Try a higher number.\n")
            else:
                print("Too high! Try a lower number.\n")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
    
    print(f"\n😢 Game Over! The number was {secret_number}.")
    return False

def main():
    while True:
        result = play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
```

### **Advanced Version with Difficulty**
```python
import random

def play_game_with_difficulty():
    print("Select difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-1000, 5 attempts)")
    
    level = input("Choose (1/2/3): ").strip()
    
    if level == '1':
        max_num = 50
        max_attempts = 15
        difficulty = "Easy"
    elif level == '2':
        max_num = 100
        max_attempts = 10
        difficulty = "Medium"
    elif level == '3':
        max_num = 1000
        max_attempts = 5
        difficulty = "Hard"
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_num = 100
        max_attempts = 10
        difficulty = "Medium"
    
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    print(f"\n{difficulty} Mode - Guess a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            attempts += 1
            
            if guess < 1 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}.")
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You won in {attempts} attempt(s)!")
                return True
            elif guess < secret_number:
                remaining = max_attempts - attempts
                print(f"Too low! ({remaining} attempts left)")
            else:
                remaining = max_attempts - attempts
                print(f"Too high! ({remaining} attempts left)")
        
        except ValueError:
            print("Invalid input! Please enter a number.\n")
    
    print(f"\n😢 Game Over! The number was {secret_number}.")
    return False

def main():
    while True:
        result = play_game_with_difficulty()
        if input("\nPlay again? (yes/no): ").lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
```

### **Version with Hints**
```python
import random

def play_with_hints():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome! I'm thinking of a number 1-100.")
    print("You have 10 attempts and 3 hints.\n")
    
    hints_used = 0
    max_hints = 3
    
    while attempts < max_attempts:
        guess = int(input(f"Guess {attempts + 1}/10: "))
        attempts += 1
        
        if guess == secret:
            print(f"✅ Correct! It took {attempts} attempts!")
            return
        
        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        
        if attempts % 3 == 0 and hints_used < max_hints:
            hint = input("Want a hint? (yes/no): ").lower()
            if hint == 'yes':
                if secret % 2 == 0:
                    print("💡 Hint: The number is even!")
                else:
                    print("💡 Hint: The number is odd!")
                hints_used += 1
    
    print(f"❌ Game Over! The number was {secret}.")

play_with_hints()
```

---

## 📊 Game Flow

```
Start Game
    ↓
Generate Random Number (1-100)
    ↓
Player Makes Guess
    ↓
Check if Valid (1-100)
    ↓
Compare with Secret
    ├─→ Equal → Win!
    ├─→ Higher → "Too high" hint
    └─→ Lower → "Too low" hint
    ↓
Check Attempts Left
    ├─→ Yes → Repeat
    └─→ No → Game Over
```

---

## 🎯 Game Mechanics

| Element | Description |
|---------|-------------|
| **Range** | 1 to 100 |
| **Attempts** | 10 maximum |
| **Hints** | Higher/Lower |
| **Win Condition** | Guess = Secret number |
| **Lose Condition** | Attempts = 0 |

---

## 💡 Real-World Learning

✅ **Random Number Generation:** `random.randint()`  
✅ **Loops:** `while` loops  
✅ **Conditionals:** `if/elif/else`  
✅ **Input Handling:** `input()` function  
✅ **Error Handling:** `try/except`  
✅ **Variable Management:** Score/attempt tracking  

---

## 📊 Difficulty Levels (Optional)

| Level | Range | Attempts |
|-------|-------|----------|
| **Easy** | 1-50 | 15 |
| **Medium** | 1-100 | 10 |
| **Hard** | 1-1000 | 5 |

---

## 🎓 Learning Outcomes

Master these concepts:
- ✅ Random number generation
- ✅ Loop structures
- ✅ Conditional statements
- ✅ User input/output
- ✅ Error handling
- ✅ Game logic
- ✅ Variable scope
- ✅ Function design

---

## 🚀 Future Enhancements

- [ ] Score saving
- [ ] Leaderboard
- [ ] Difficulty levels
- [ ] Timed mode
- [ ] Multiplayer
- [ ] GUI version
- [ ] Sound effects
- [ ] Statistics tracking

---

## 🤝 Contributing

Contributions welcome!
1. Fork repository
2. Create feature branch
3. Add improvements
4. Submit pull request

---

## 📝 License

MIT License - see LICENSE file

---

## 👨‍💻 Author

**Shubham Kadam**
- GitHub: [@ShubhamK-0904](https://github.com/ShubhamK-0904)
- LinkedIn: [Shubham Kadam](https://www.linkedin.com/in/shubham-kadam-b8856031a/)
- Email: shubham85kadam@gmail.com

---

<p align="center">
  <strong>⭐ Did you enjoy the game? Give it a star! ⭐</strong>
</p>

<p align="center">
  Made with ❤️ by Shubham Kadam | Last Updated: May 2026
</p>
