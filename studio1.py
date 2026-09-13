import pandas as pd
import matplotlib.pyplot as plt


# 1a
data = pd.read_csv("us-states.csv")
data["date"] = pd.to_datetime(data["date"])

print(data.head())
print(data.dtypes)
print(data.shape)


# 1b
ca = data[data["state"] == "California"].copy()
ca["daily_cases"] = ca["cases"].diff()

print(ca[["date", "cases", "daily_cases"]].head(10))

def plot_daily_cases(states):
    for state in states:
        state_data = data[data["state"] == state].copy()
        state_data["daily_cases"] = state_data["cases"].diff().fillna(0)

        plt.plot(
            state_data["date"],
            state_data["daily_cases"],
            label=state
        )

    plt.xlabel("Date")
    plt.ylabel("Daily New Cases")
    plt.title("Daily New Covid-19 Cases by State")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_daily_cases(["Washington", "California", "Connecticut", "New York"])

# 1c
def get_peak_date(state):
    state_data = data[data["state"] == state].copy()
    state_data["daily_cases"] = state_data["cases"].diff().fillna(0)

    peak_index = state_data["daily_cases"].idxmax()
    peak_date = state_data.loc[peak_index, "date"]

    return peak_date

print("Washington peak:", get_peak_date("Washington"))
print("Connecticut peak:", get_peak_date("Connecticut"))



# 1d

def compare_peak_dates(state1, state2):
    date1 = get_peak_date(state1)
    date2 = get_peak_date(state2)

    days_apart = abs((date1 - date2).days)

    if date1 < date2:
        first_state = state1
    elif date2 < date1:
        first_state = state2
    else:
        first_state = "Same day"

    return first_state, days_apart



first, days = compare_peak_dates("Washington", "Connecticut")

print(f"{first} reached its peak first.")
print(f"The peaks were {days} days apart.")


# 1e
fl = data[data["state"] == "Florida"].copy()
fl["daily_cases"] = fl["cases"].diff()

print(fl[["date", "cases", "daily_cases"]].sort_values(
    "daily_cases", ascending=False
).head(10))

plt.plot(fl["date"], fl["daily_cases"])
plt.xlabel("Date")
plt.ylabel("Daily New Cases")
plt.title("Florida COVID-19 Daily New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



print(fl[["date", "cases", "daily_cases"]].sort_values("daily_cases", ascending=False).head(10))

print(fl[["date", "cases", "daily_cases"]].sort_values("daily_cases").head(10))