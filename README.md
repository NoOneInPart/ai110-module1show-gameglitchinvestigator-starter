# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   > Make the user guess numbers until they either win or lose.
- [ ] Detail which bugs you found.
   > Contradictory hints, "attempts left" does not update correctly, difficulty changes don't apply correctly, New Game doesn't work, the Enter key does not submit a guess (not necessarily a bug)
- [ ] Explain what fixes you applied.
   > The hints were corrected and an underlying bug where the secret changed types with every other guess was fixed, the "attempts left" message was reconfigured to update after a guess was submitted rather than before, changing the difficulty now takes the new range into account when picking a new secret, the game correctly starts with all attempts available, the New Game button properly resets the game state completely, the text entry box is wrapped in a form to allow handling the Enter key.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select a difficulty from the sidebar
2. Enter a guess into the box
3. Press Enter or "Submit Guess"
4. Enter new guesses as needed depending on the given hint
5. Win or lose.
6. Press New Game
7. GOTO 1.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
![Screenshot](/Screenshot%20(250).png)

## 🧪 Test Results

```
> python -m pytest
========= test session starts =========
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\t0mbu\Desktop\ai110-module1show-gameglitchinvestigator-starter\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                      

tests\test_game_logic.py .....   [100%]

========== 5 passed in 0.03s ==========
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
