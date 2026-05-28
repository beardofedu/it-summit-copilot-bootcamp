"""Reference examples for improving vague prompts.

These are not the only correct answers. The goal is to show how adding
context, intent, and constraints gives Copilot better direction.
"""

# Read a list of order dictionaries and return only the paid orders.
# Sort the results by created_at in descending order and return the total count.
def process_order_data(data: list[dict]) -> tuple[list[dict], int]:
    paid_orders = [order for order in data if order.get("status") == "paid"]
    paid_orders.sort(key=lambda order: order.get("created_at", ""), reverse=True)
    return paid_orders, len(paid_orders)


# Send a welcome email for a newly created user record.
# Return False if the user does not have an email address; otherwise return True.
def do_the_thing(user_record: dict) -> bool:
    email = user_record.get("email")
    if not email:
        return False
    print(f"Sending welcome email to {email}")
    return True


# Load settings from a JSON file.
# If the file does not exist, return an empty settings dictionary instead of crashing.
def load_settings(path: str) -> dict:
    import json
    from pathlib import Path

    settings_path = Path(path)
    if not settings_path.exists():
        return {}
    return json.loads(settings_path.read_text(encoding="utf-8"))


# Convert an integer number of minutes into a human-readable string like "1h 30m".
def helper(value: int) -> str:
    hours, minutes = divmod(value, 60)
    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes or not parts:
        parts.append(f"{minutes}m")
    return " ".join(parts)
