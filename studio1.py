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
    plt.figure(figsize=(14, 6))

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
    plt.savefig("daily_cases.png")
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


## Function to compare between multiple states just to get one more step further

def compare_multiple_peaks(states):
    peak_dates = {}

    for state in states:
        peak_dates[state] = get_peak_date(state)

    earliest_date = min(peak_dates.values())

    results = []

    for state, date in peak_dates.items():
        days_from_earliest = (date - earliest_date).days

        results.append({
            "state": state,
            "peak_date": date,
            "days_from_earliest": days_from_earliest
        })

    return pd.DataFrame(results).sort_values("peak_date")

states = ["Washington", "California", "Connecticut", "New York", "Florida", "Alaska", 
          "Pennsylvania", "Texas", "Illinois", "Georgia", "Arizona", "Oregon"]
peak_comparison = compare_multiple_peaks(states)
print(peak_comparison)

plt.bar(
    peak_comparison["state"],
    peak_comparison["days_from_earliest"]
)

plt.xlabel("State")
plt.ylabel("Days After Earliest Peak")
plt.title("COVID-19 Peak Timing Across States")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("peak_across_states.png")
plt.show()


## All states peak comparison
all_states = data["state"].unique().tolist()

all_peak_comparison = compare_multiple_peaks(all_states)

print(all_peak_comparison)

earliest_peak = all_peak_comparison["peak_date"].min()
latest_peak = all_peak_comparison["peak_date"].max()

overall_gap = (latest_peak - earliest_peak).days

print(f"Earliest peak: {earliest_peak.strftime('%Y-%m-%d')}")
print(f"Latest peak: {latest_peak.strftime('%Y-%m-%d')}")
print(f"Overall gap: {overall_gap} days")


# Count the number of regions whose peak occurred in each month

all_peak_comparison["peak_month"] = (
    all_peak_comparison["peak_date"].dt.to_period("M")
)

monthly_peak_counts = (
    all_peak_comparison["peak_month"]
    .value_counts()
    .sort_index()
)

print("\nNumber of regions by peak month:")
print(monthly_peak_counts)



# 1e
fl = data[data["state"] == "Florida"].copy()
fl["daily_cases"] = fl["cases"].diff()

print(fl[["date", "cases", "daily_cases"]].sort_values(
    "daily_cases", ascending=False
).head(10))

plt.figure(figsize=(14, 6))
plt.plot(fl["date"], fl["daily_cases"])
plt.xlabel("Date")
plt.ylabel("Daily New Cases")
plt.title("Florida COVID-19 Daily New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("fl_plot.png")
plt.show()


print(fl[["date", "cases", "daily_cases"]].sort_values("daily_cases", ascending=False).head(10))
print(fl[["date", "cases", "daily_cases"]].sort_values("daily_cases").head(10))