# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    A streamlit app launches in the browser, with the header "Game Glitch Investigator" and the subtitle "An AI-generated guessing game. Something is off." A sidebar displays attempts allowed and the difficulty, the main panel asks you to make a guess between 1 and 100, there is a collapsible Developer Debug Info panel, an input field to "Enter your guess:", buttons for "Submit Guess," "New Game," and a checkbox for Show hint. The footer says "Built by an AI that claims this code is production-ready."
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    The hints were indeed backwards. For a secret number of 82, it kept telling me to go lower, even when I entered in the minimum value of 1.
    The number of attempts does not update after you submit a guess, only after you submit another guess, which is confusing as you will end the game with seemingly 1 attempt left. The starting number also deviates from the "Attempts allowed" in the sidebar by 1.
    Also, hitting New Game clears the status showing the correctness of your guess but does not clear the game completion status; you cannot submit new guesses and there is still a banner informing you to "Start a new game to play again."
    The textbox, when selected, informs you to "Press Enter to apply" but this does not submit a guess.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                     | Expected Behavior        | Actual Behavior    | Console Output / Error |
|---------------------------|--------------------------|--------------------|------------------------|
| guess below secret        | "Go HIGHER!" hint        | "Go LOWER!" hint   | none                   |
| guess above secret        | "Go LOWER!" hint         | "Go HIGHER!" hint  | none                   |
| press [ENTER] after guess | guess is submitted       | hint is cleared    | none                   |
| submit final guess        | Attempts left: 0         | Attempts left: 1   | none                   |
| difficulty changed        | number range changes     | range still 1-100  | none                   |
|                           | new game, attempts reset | attempts not reset | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
