def analyze_user_activity(log_file_path: str) -> dict:
    total_users = set()
    action_counts = {}
    user_activity_time = {}
    login_durations = []

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 4:
                continue

            date_time, user_id, action, duration_str = parts

            try:
                duration = float(duration_str)
            except ValueError:
                continue

            total_users.add(user_id)

            if action in action_counts:
                action_counts[action] += 1
            else:
                action_counts[action] = 1

            if user_id in user_activity_time:
                user_activity_time[user_id] += duration
            else:
                user_activity_time[user_id] = duration

            if action == "login":
                login_durations.append(duration)

    most_active_user = None

    if user_activity_time:
        most_active_user = max(
            user_activity_time,
            key=user_activity_time.get
        )

    if login_durations:
        average_session_time = (
            sum(login_durations) / len(login_durations)
        )
    else:
        average_session_time = 0.0

    action_counts = dict(sorted(action_counts.items()))

    return {
        "action_counts": action_counts,
        "average_session_time": average_session_time,
        "most_active_user": most_active_user,
        "total_users": len(total_users),
    }


if __name__ == "__main__":
    result = analyze_user_activity("activity.log")

    from pprint import pprint
    pprint(result)
