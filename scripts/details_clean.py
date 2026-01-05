import pandas as pd

# load your messy file
df = pd.read_csv("zomato_details_final_clean.csv")

# keep ONLY these 3 columns (drop everything else)
df_small = df[["name", "rating", "cost_for_two"]]

# save the result
df_small.to_csv("restaurants_name_rating_cost.csv", index=False)

print("Done! Saved: restaurants_name_rating_cost.csv")
