def process(df):  # sourcery skip: avoid-builtin-shadow
    df.columns=df.columns.str.strip()
    df=df.drop_duplicates()
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(' ','_')
    objective=df.select_dtypes(['object'])
    df[objective.columns]=objective.apply(lambda x: x.str.strip())
    return df

