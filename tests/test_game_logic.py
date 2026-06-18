from logic_utils import check_guess

#FIX: existing check_guess() outputs tuple yet tests expect a string, fixed with Claude
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and the
    # hint should tell the player to go LOWER (not contradictory).
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and the
    # hint should tell the player to go HIGHER (not contradictory).
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# Type checks: check_guess should return a (str, str) tuple and compare two
# ints without raising. These guard against the old bug where the secret was
# cast to str and comparisons fell back to lexicographic string ordering.
# Authored using Claude.
def test_return_types():
    result = check_guess(40, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2
    outcome, message = result
    assert isinstance(outcome, str)
    assert isinstance(message, str)

def test_int_inputs_do_not_raise():
    # With two ints, check_guess must compare cleanly without a TypeError.
    check_guess(40, 50)
    check_guess(50, 50)
    check_guess(60, 50)
