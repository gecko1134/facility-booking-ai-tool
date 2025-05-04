import pandas as pd

# Load past bookings and simulate AI suggestions based on usage patterns
def load_bookings(path="historical_data.csv"):
    return pd.read_csv(path)

def load_requests(path="new_requests.csv"):
    return pd.read_csv(path)

def check_conflict(existing_df, date, resource, start_time, end_time):
    overlaps = existing_df[
        (existing_df["Date"] == date) &
        (existing_df["Resource"] == resource) &
        (
            ((existing_df["Start Time"] <= start_time) & (existing_df["End Time"] > start_time)) |
            ((existing_df["Start Time"] < end_time) & (existing_df["End Time"] >= end_time)) |
            ((existing_df["Start Time"] >= start_time) & (existing_df["End Time"] <= end_time))
        )
    ]
    return not overlaps.empty

def suggest_slots(existing_df, requests_df):
    suggestions = []
    for _, row in requests_df.iterrows():
        date = row["Date"]
        resource = row["Resource"]
        preferred = row["Preferred Time"]
        start, end = preferred.split("-")
        if not check_conflict(existing_df, date, resource, start, end):
            status = "Available"
        else:
            status = "Conflict"
        suggestions.append({
            "User Group": row["User Group"],
            "Date": date,
            "Resource": resource,
            "Preferred Time": preferred,
            "Suggestion Status": status
        })
    return pd.DataFrame(suggestions)
