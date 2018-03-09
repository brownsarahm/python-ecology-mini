# split these and view the first few rows of each
surveys_df = pd.read_csv("data/surveys.csv",
                         keep_default_na=False, na_values=[""])
species_df = pd.read_csv("data/species.csv",
                         keep_default_na=False, na_values=[""])
