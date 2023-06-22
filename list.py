def flat_list(unflat_list):
    return [item for sublist in unflat_list for item in sublist]

def to_list(df, attribute):
    df_transcription = df[[attribute]]
    unflat_list_transcription = df_transcription.values.tolist()
    return flat_list(unflat_list_transcription)
