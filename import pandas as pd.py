import pandas as pd

file_path = "/content/Drug_clean.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")

df["Sensitivity"] = df["Effective"] / 5
df["Specificity"] = df["Satisfaction"] / 5
df["Prevalence"] = df["Reviews"] / df["Reviews"].max()

def calculate_posterior(sensitivity, specificity, prevalence):
    positive_given_drug = sensitivity
    positive_given_no_drug = 1 - specificity

    positive_total = (positive_given_drug * prevalence) + \
                     (positive_given_no_drug * (1 - prevalence))

    posterior = (positive_given_drug * prevalence) / positive_total
    return posterior

df["Posterior_Probability"] = df.apply(
    lambda row: calculate_posterior(
        row["Sensitivity"],
        row["Specificity"],
        row["Prevalence"]
    ), axis=1
)

print("\nPosterior Probabilities:")
print(df["Posterior_Probability"])
