# How many recorded individuals are female `F` and how many male `M`?
grouped_data

# What happens when you group by two columns using the following syntax and
#    then grab mean values:
grouped_data2 = surveys_df.groupby(['plot_id','sex'])
grouped_data2.mean()
# Summarize weight values for each plot in your data. HINT: you can use the
#  following syntax to only create summary statistics for one column in your data
by_plot =
by_plot['weight'].describe()
