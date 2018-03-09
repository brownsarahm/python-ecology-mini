# Create a plot of average weight across all species per sex and plot.

by_plot_sex = surveys_df.groupby(['',''])
plot_sex_weight = by_plot_sex['']
spc = plot_sex_weight.unstack() # try printing things out to learn what this does

s_plot = spc.plot(kind='',stacked=True,title="Mean weight by plot and sex")
s_plot.set_ylabel("")
s_plot.set_xlabel("");
