"""Rewrite the bad prompts below so Copilot has a better chance of helping.

Exercise steps:
1. Read the bad prompt.
2. Read why it is weak.
3. Replace it with a clearer prompt that includes context, intent, and constraints.
4. Then try generating code from your improved version.
"""

# Bad prompt: too vague. What data? What processing? What output?
# Challenge: Rewrite this so it explains the input, desired transformation, and return value.
# process data
def process_order_data(data):
    pass


# Bad prompt: meaningless placeholder. It provides no intent at all.
# Challenge: Rewrite this to describe a real business action with success/failure behavior.
# do the thing
def do_the_thing(user_record):
    pass


# Bad prompt: there is no issue described, so Copilot has to guess.
# Challenge: Rewrite this comment to state the bug scenario and the expected fix.
# fix the issue
def load_settings(path):
    pass


# Bad prompt: “helper function” says nothing about purpose.
# Challenge: Rewrite this to explain what the helper should compute or format.
# helper function
def helper(value):
    pass
