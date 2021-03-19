

def make_barplot(dataframe, x_series, y_series):

    import matplotlib.pyplot as plt 
    from helper_funct import insert_thousands_commas
    import seaborn as sns
    from matplotlib.pyplot import figure
    fig = figure(figsize=(35,25))  # define the figure window
    ax1  = fig.add_subplot(111)   # define the axis
    sorted_df = dataframe.sort_values(y_series, ascending=False)[:10]
    graph = sns.barplot(data=sorted_df, x=x_series, y=y_series)
    #label x,y axes
    plt.title('Newest Artists Trending on Tiktok (1-Month on Chart)', size=40)
    plt.xticks(rotation=90)
    plt.ylabel('Total IG Followers - Before Tiktok', size=40)
    plt.xlabel('Artists', size=40)
    plt.ticklabel_format(style='plain', axis='y') #change xaxis from sci to plain style
    plt.tick_params(axis='both', which='major', labelsize=35)
    plt.grid(axis='y', which='major')
    #annotate bars
    oldheight=0
    for bar in graph.patches:
        currentheight = bar.get_height()
        if currentheight > oldheight:

            graph.annotate(insert_thousands_commas(bar.get_height()), (bar.get_x() + bar.get_width()/2, bar.get_height()), 
                           size=40, xytext=(bar.get_x() + bar.get_width()/10, currentheight+3000000), 
                           arrowprops={'arrowstyle':'wedge'})
            oldheight = bar.get_height()
        else:
            graph.annotate(insert_thousands_commas(bar.get_height()), (bar.get_x() + bar.get_width()/2, bar.get_height()), 
                           size=40,xytext=(bar.get_x() + bar.get_width()/10, currentheight+oldheight/2), 
                           arrowprops={'arrowstyle':'wedge'})
            oldheight = bar.get_height()     

    plt.tight_layout()
    plt.savefig('/home/bull/Documents/bull-analytics/dash_project/visuals/top10_artistsIG.jpeg')
    plt.show()