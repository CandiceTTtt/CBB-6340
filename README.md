# CBB-6340
Xintong Chen

NetID: xc463

# Exercise 1: Analyzing COVID-19 Case Data
## Repository Files

- `studio1.py`: Main Python script containing the data loading, visualization, peak-date analysis, and Florida anomaly analysis.
- `us-states.csv`: COVID-19 case data from The New York Times.
- `daily_cases.png`: Visualization of daily new COVID-19 cases for selected states.
- `fl_plot.png`: Visualization of daily new COVID-19 cases for Florida.


These data are obtained from [The New York Times COVID-19 Data repository](https://github.com/nytimes/covid-19-data)


## Key Outputs, Figures, and Visualizations
### 1a. Data Acquisition & Loading
The dataset contains **61942 observations and 5 columns**:

- `date`
- `state`
- `fips`
- `cases`
- `deaths`

The dataset contains **56 geographic entities**, including U.S. states, Washington D.C., and several U.S. territories.

The `date` column was initially stored as strings and was converted to pandas datetime objects using `pd.to_datetime()`.

### 1b. Visualization of Daily New Cases
The original `cases` column contains cumulative reported case counts rather than daily new cases. Daily reported cases were calculated by taking the difference between consecutive cumulative case counts.

The `plot_daily_cases()` function accepts a list of state names and creates an overlaid line plot showing their daily reported cases over time.

### Figure

![Daily New COVID-19 Cases](daily_cases.png)

### Key Observations

The four states show similar overall waves of COVID-19 cases, but the timing and magnitude of these waves differ across states.

California has the largest reported daily case counts in the later part of the dataset, with particularly large spikes around late 2021 and early 2022. New York also shows several pronounced increases, especially during late 2020 and early 2021. Washington and Connecticut generally have lower daily reported case counts compared with California and New York.

Across all four states, the largest increases occur around the end of 2021 and the beginning of 2022, corresponding to a major wave of reported cases. However, the exact timing and size of the peaks vary between states.

The plot also shows substantial day-to-day variation, including sharp individual spikes. Because these values are calculated from cumulative reported cases, some of these spikes may reflect reporting delays, backlogs, or data revisions rather than cases occurring entirely on that specific day. Therefore, the plot is useful for comparing reported case patterns over time, but individual daily peaks should be interpreted with caution.


### 1c. Identifying Peak Case Dates
The `get_peak_date()` function identifies the date on which a state experienced its highest calculated number of daily reported cases.

Example outputs:

```text
Washington peak: 2022-01-18
Connecticut peak: 2022-01-10
```


### 1d. Comparing Peak Dates Between States

The `compare_peak_dates()` function compares the peak dates of two states and calculates the exact number of days between their peaks.

Example output:

```text
Connecticut reached its peak first.
The peaks were 8 days apart.
```

### Extension: Comparing Peak Timing Across Multiple Regions

I extended the two-state comparison to multiple regions to explore differences in the timing of reported COVID-19 case peaks across geographic areas. The function calculates the peak date for each region, identifies the earliest and latest peaks, and calculates the number of days between them.

I first tested the extension using a selected group of 12 states. Their peak dates were concentrated within a relatively short period, which was smaller than I initially expected. To determine whether this pattern was representative of the broader dataset, I then extended the analysis to all regions included in the dataset.

### Example Output

For all regions in the dataset:

    Earliest peak: 2021-01-04
    Latest peak: 2022-09-28
    Overall gap: 632 days

The earliest reported peak occurred in New Jersey on January 4, 2021, while the latest reported peak occurred in Hawaii on September 28, 2022.

To further examine the distribution of peak dates, I also counted how many regions had their reported peak in each month.

    Number of regions by peak month:
    2021-01     1
    2021-03     1
    2022-01    47
    2022-02     3
    2022-04     1
    2022-07     2

### Key Observation

The results provide a more nuanced view of the differences in peak timing across regions. The overall gap between the earliest and latest reported peaks was 632 days, which is much larger than the 19-day gap observed in my initial selection of 12 states.

However, the monthly distribution shows that 47 of the regions had their reported peak in January 2022. This means that although the overall range was very large, most regions were actually highly concentrated around the same period. The very early and late peaks therefore appear to be relatively uncommon compared with the large cluster around January 2022.

This changed my initial interpretation of the selected-state comparison. The small gap among the 12 initially selected states did not represent the full range of the dataset, but the January 2022 concentration also shows that the selected states were not completely unusual. Instead, both the overall range and the concentration of peaks are important for understanding the data.

### Limitations

There are several limitations to this comparison. The analysis relies on reported case counts rather than the exact dates when infections occurred. Differences in testing, reporting practices, reporting delays, backlogs, and data collection across regions may introduce bias into the reported daily case counts.

The earliest and latest peak dates may also be influenced by unusual reporting patterns or data revisions, so the 632-day range should not be interpreted as meaning that COVID-19 infections peaked 632 days apart across these regions. The results should instead be interpreted as differences in the timing of the highest reported daily case counts. The comparison with all regions helps provide broader context, but the results are still limited by the quality and consistency of the underlying reported data.


### 1e. Florida Anomaly Analysis

The Florida data contain several unusually large changes in reported daily cases.

### Largest Positive Changes

| Date | Daily Reported Cases |
|---|---:|
| January 4, 2022 | 193,786 |
| January 10, 2022 | 125,996 |
| January 18, 2022 | 111,621 |
| January 6, 2023 | 80,749 |

### Largest Negative Change

| Date | Daily Reported Cases |
|---|---:|
| June 4, 2021 | -40,527 |

### Figure

![Florida Daily New COVID-19 Cases](fl_plot.png)

### Key Observations

Florida's largest calculated daily increase was **193,786 cases on January 4, 2022**, which is substantially larger than the surrounding daily values.

The data also contain a negative daily value of **-40,527 cases on June 4, 2021**. Because daily cases were calculated from changes in cumulative reported cases, this negative value does not represent a real decrease in infections.

Instead, it likely reflects a revision, correction, or other adjustment to previously reported cumulative case totals.

The unusually large positive spikes may similarly reflect reporting delays or backlogged cases being added to the cumulative total on a later reporting date.




---

## Code Evolution

I started by reading the exercise instructions and developing an overall plan for the analysis. I explored The New York Times GitHub repository to understand the dataset structure, variables, and size, then broke the assignment into smaller steps.

I used Codex to help generate initial versions of the code and then reviewed, tested, and refined the generated code based on the intermediate results. Rather than running the entire script at once, I checked the outputs from each step and used them to guide the next step.

For the extension, I initially selected 12 states to compare their peak dates. When I found that their peaks were concentrated within a 19-day window, I extended the analysis to all regions to determine whether this pattern was representative of the broader dataset. I also added a monthly count of peak dates to better understand the distribution.

---

## Design Choices & Trade-offs

Most of the code in this exercise uses relatively basic Python and pandas operations, so there were not many complicated technical choices. The part that required the most consideration for me was the visualization.

The instructions asked for an overlaid line plot of daily new cases for multiple states. However, the dataset contains a very large number of dates, so plotting every daily value over the full time period makes the figure quite dense and sometimes difficult to read. In particular, California has much larger reported case counts than some of the other selected states, which makes its line much more prominent and can make smaller changes in other states harder to notice. When several states have similar values, their lines can also overlap and become difficult to distinguish. I have not yet found a better way to make the visualization clearer while still following the requested format, so for now I kept the required overlaid line plot and made the figure wider to improve readability.

For the extension, I chose to compare peak dates across multiple states because I wanted to take the analysis one step further and see whether there was a noticeable pattern in the timing of reported COVID-19 peaks across different regions. The selected states showed a smaller gap between peaks than I initially expected. This made the extension useful not only as an additional analysis, but also as a way to compare my initial expectation with what the data actually showed.

There are also limitations in how the peak dates should be interpreted. The peak is defined based on the highest reported daily case count in the dataset, so it represents a peak in reported cases rather than necessarily the true peak in infections. Reporting delays, backlogs, revisions, and differences in reporting practices may affect the timing and magnitude of these reported peaks.

Finally, the states used in the extension were selected by me rather than being a systematic or representative sample of all states. Therefore, the observed differences, or lack of large differences, may not reflect the overall pattern across the United States.

---

## Key Findings

The analysis shows substantial differences in reported COVID-19 case patterns across regions. Some states experienced much larger daily increases than others, while the timing and magnitude of peaks also varied considerably. The daily case plots also show that some regions experienced multiple distinct peaks, suggesting repeated waves of increased reported cases rather than a single sustained peak.

The all-region peak analysis showed that although the overall range between the earliest and latest reported peaks was large, most regions were concentrated around January 2022. Specifically, 47 regions had their highest reported daily case count in January 2022. This suggests that the overall range was driven partly by a smaller number of regions with unusually early or late peaks.

The Florida analysis revealed particularly unusual reporting patterns, including a very large positive daily case count of 193,786 on January 4, 2022 and a negative daily case count of -40,527 on June 4, 2021. These values suggest that changes in reported cumulative case counts can reflect data revisions, reporting backlogs, or other reporting practices rather than actual changes in infections on a single day.

Overall, the results demonstrate that reported COVID-19 data can contain substantial differences across regions and unusual reporting patterns. Looking at both visual trends and summary statistics is therefore important before interpreting the data or drawing conclusions about actual infection patterns.