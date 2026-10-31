def find_outliers(coloum,df):
    q1 = df [column].quantile(0.25)
    q3 = df [column].quantile(0.75)
    IQR Q3 -q1

    lower_limit = q1 - 1.5 * IQR
    uper_limit = q1 - 1.5 * IQR



    find_outlier("Age",df)

    plt.figure(figure= (6,4))
    plt.boxplot(df["Age"],dropna)

