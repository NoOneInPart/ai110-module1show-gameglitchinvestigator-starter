# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    > A streamlit app launches in the browser, with the header "Game Glitch Investigator" and the subtitle "An AI-generated guessing game. Something is off." A sidebar displays attempts allowed and the difficulty, the main panel asks you to make a guess between 1 and 100, there is a collapsible Developer Debug Info panel, an input field to "Enter your guess:", buttons for "Submit Guess," "New Game," and a checkbox for Show hint. The footer says "Built by an AI that claims this code is production-ready."
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    > - The hints were indeed backwards. For a secret number of 82, it kept telling me to go lower, even when I entered in the minimum value of 1.
    > - The number of attempts does not update after you submit a guess, only after you submit another guess, which is confusing as you will end the game with seemingly 1 attempt left. The starting number also deviates from the "Attempts allowed" in the sidebar by 1.
    > - Also, hitting New Game clears the status showing the correctness of your guess but does not clear the game completion status; you cannot submit new guesses and there is still a banner informing you to "Start a new game to play again."
    > - The textbox, when selected, informs you to "Press Enter to apply" but this does not submit a guess.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                     | Expected Behavior        | Actual Behavior    | Console Output / Error |
|---------------------------|--------------------------|--------------------|------------------------|
|✔️guess below secret        | "Go HIGHER!" hint        | "Go LOWER!" hint   | none                   |
|✔️guess above secret        | "Go LOWER!" hint         | "Go HIGHER!" hint  | none                   |
|✔️press [ENTER] after guess | guess is submitted       | hint is cleared    | none                   |
|✔️submit final guess        | Attempts left: 0         | Attempts left: 1   | none                   |
|✔️difficulty changed        | number range changes     | range still 1-100  | none                   |
|✔️                          | new game, attempts reset | attempts not reset | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    > Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    > When fixing the contradictory hints and producing tests for them, Claude mentioned that the existing tests in test_game_logic.py would fail as the existing check_guess() function returns a tuple, while the existing tests expect a string, and suggested a fix. This was correct: the tests pass correctly and the program functions properly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    > Claude mentions that the TypeError fallback of check_guess() doesn't need to exist because both 'guess' and 'secret' could be cast to integer, but this isn't necessarily true because the secret should already be an int. This ended up exposing another bug where the secret is specifically cast to a string inside the Streamlit app but only on even-numbered attempts for some reason. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    > For game logic bugs, I tested them using both the existing pytest tests and manually by running the game with different inputs a few times. The existing tests, interestingly, required a bit of tweaking as it expected the output of check_guess to be a string, yet the codebase is coded to use and expect a tuple, so I let Claude tweak that a bit, verifying that the tests pass and the code still runs properly under Streamlit. \
    > For the Streamlit interface side, I had to test manually. I tried to trigger the known bugs, and if they didn't manifest, I considered it solved. I also played a few games normally to ensure no new bugs were introduced.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
    > After I had Claude take a crack at allowing the user to press Enter to submit a guess, it implemented it in such a way that a guess was submitted every time Streamlit recognized that there was a change in value. This worked when I manually tested the game, but I failed to realize that it would *also* submit a guess if the focus on the input box changed until later. After prompting Claude again it wrapped the input box in a form which had a specific Submit function that fixed the problem, but I learned that I have to be very vigilant when manually testing the code to ensure any changes don't introduce regressions.
- Did AI help you design or understand any tests? How?
    > For the existing tests in the repository, it turned out they expected different results (strings instead of tuples) from the check_guess function than it was actually supposed to give, and Claude proactively pointed this out when I asked it to build tests to check that the hints given by check_guess were no longer contradictory. I manually reviewed the changes to ensure it didn't mess with the core logic of the tests beyond unpacking the tuples, and then the tests worked. I also asked Claude to design tests to ensure that the results in the tuple are always (str, str) and no longer flip-flop around every other guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    > A Streamlit "rerun" basically re-renders the web interface. If you make changes to some text or how data is presented, or if you simply interact with the application, it will update accordingly, but it won't touch the session state, meaning all your variables stay exactly the same and you can pick up where you left off with the program. If you refresh the page, it will rerun AND clear the session state, so you're left with a completely new state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  > Maybe don't push every single commit immediately so I don't have to push an awkward revert when I realize one of the changes introduced a regression.
- What is one thing you would do differently next time you work with AI on a coding task?
    > I might try to make more use of the cheaper models like Sonnet instead of Opus. I only used about $5 in credits but that still isn't cheap considering I haven't accomplished that much with it.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    > It is no longer important to intimately know the syntax and quirks of a language, but one must still be the mastermind behind the design and function of a project because the LLM *can* and *will* make questionable decisions. Get good at reviewing code, essentially.