import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr
from rpy2.robjects import globalenv

# Activate the pandas2ri conversion
pandas2ri.activate()

# Load the dataset
data = pd.read_excel('Digdata Step Up Meta dataset.xlsx')

print("------------------------------------------------------------------")

# Check total number of rows (advert entries)
total_adverts = data.shape[0]
print(f'Total number of advert campaigns in the dataset: {total_adverts}')

duplicate_ads = data.duplicated(subset=['study_id']).sum()
print(f'Total number of duplicate adverts before removal: {duplicate_ads}')

# Clean the data by removing null values (if applicable for initial analysis)
data = data.dropna(subset=['ad_objective_str', 'num_ad_ids'])

# Remove duplicate entries based on 'study_id'
data = data.drop_duplicates(subset=['study_id'], keep='first')

# Check total number of rows (advert entries)
total_adverts = data.shape[0]
print(f'Total number of usable adverts in the dataset: {total_adverts}')

print("------------------------------------------------------------------")

# Inspect the first few rows of the dataset
print("\nSample of the advert data:")
print(data.head())

print("------------------------------------------------------------------")

# Check for duplicate ad entries (after removal)
duplicate_ads = data.duplicated(subset=['study_id']).sum()
print(f'Duplicate advert campaigns found: {duplicate_ads}')

print("------------------------------------------------------------------")

# ---- Customer Segment Optimization Test ----
# Create Group A for customer segment optimization
group_A_1 = data[
    (data['is_tgt_using_interests'] == True) & 
    (data['is_tgt_using_custom_audience_inclusion'] == True) & 
    (data['is_tgt_using_lookalikes'] == True)
].copy()

# Create Group B for customer segment optimization
group_B_1 = data[
    ~(data['is_tgt_using_interests'] == True) & 
    ~(data['is_tgt_using_custom_audience_inclusion'] == True) & 
    ~(data['is_tgt_using_lookalikes'] == True)
].copy()

# Define success criteria and calculate success rate for Group A
if not group_A_1.empty:
    group_A_1['success'] = group_A_1['num_ad_ids'] > 5
    success_A_1 = group_A_1['success'].sum()
    total_A_1 = group_A_1.shape[0]
    success_rate_A_1 = (success_A_1 / total_A_1) * 100  # Success rate in percentage
else:
    success_A_1 = 0
    total_A_1 = 0
    success_rate_A_1 = 0

# Define success criteria and calculate success rate for Group B
if not group_B_1.empty:
    group_B_1['success'] = group_B_1['num_ad_ids'] > 5
    success_B_1 = group_B_1['success'].sum()
    total_B_1 = group_B_1.shape[0]
    success_rate_B_1 = (success_B_1 / total_B_1) * 100  # Success rate in percentage
else:
    success_B_1 = 0
    total_B_1 = 0
    success_rate_B_1 = 0

# Perform the z-test if both groups have entries
if total_A_1 > 0 and total_B_1 > 0:
    count = [success_A_1, success_B_1]
    nobs = [total_A_1, total_B_1]
    
    stat, p_value = proportions_ztest(count, nobs)
    
    confidence_level = 1 - p_value
    print(f'\nCustomer Segment Optimisation Test:')
    print("Comparing whether ads that target customer's interests, a specific target audience, and lookalike/similar audiences increase the ads' success.")
    print(f"Group A Success Rate: {success_rate_A_1:.2f}% ({success_A_1}/{total_A_1})")
    print(f"Group B Success Rate: {success_rate_B_1:.2f}% ({success_B_1}/{total_B_1})")
    print(f'z-statistic: {stat:.4f}, p-value: {p_value:.4f}, Confidence Level: {confidence_level:.2%}')

    # Adjusted logic for declaring a winner
    if confidence_level > 0.65:
        if success_rate_A_1 > success_rate_B_1:
            print("Group A is a winner!")
        else:
            print("Group B is a winner!")
    else:
        print("Not enough evidence to declare a winner.")
else:
    print("One or both groups are empty. Cannot perform the z-test.")

print("------------------------------------------------------------------")

# ---- Ad Formatting / Interactivity Test ----
group_A_2 = data[
    (data['is_video'] == True) & 
    (data['is_interactive_ad'] == True)
].copy()

group_B_2 = data[
    ~(data['is_video'] == True) & 
    ~(data['is_interactive_ad'] == True)
].copy()

# Calculate success rate for Group A
if not group_A_2.empty:
    group_A_2['success'] = group_A_2['num_ad_ids'] > 5
    success_A_2 = group_A_2['success'].sum()
    total_A_2 = group_A_2.shape[0]
    success_rate_A_2 = (success_A_2 / total_A_2) * 100
else:
    success_A_2 = 0
    total_A_2 = 0
    success_rate_A_2 = 0

# Calculate success rate for Group B
if not group_B_2.empty:
    group_B_2['success'] = group_B_2['num_ad_ids'] > 5
    success_B_2 = group_B_2['success'].sum()
    total_B_2 = group_B_2.shape[0]
    success_rate_B_2 = (success_B_2 / total_B_2) * 100
else:
    success_B_2 = 0
    total_B_2 = 0
    success_rate_B_2 = 0

# Perform z-test for Ad Formatting/Interactivity Test
if total_A_2 > 0 and total_B_2 > 0:
    count = [success_A_2, success_B_2]
    nobs = [total_A_2, total_B_2]
    
    stat, p_value = proportions_ztest(count, nobs)
    
    confidence_level = 1 - p_value
    print(f'\nAd Formatting / Interactivity Test:')
    print("Comparing whether ads that are videos and are interactive increase the ads' success.")
    print(f"Group A Success Rate: {success_rate_A_2:.2f}% ({success_A_2}/{total_A_2})")
    print(f"Group B Success Rate: {success_rate_B_2:.2f}% ({success_B_2}/{total_B_2})")
    print(f'z-statistic: {stat:.4f}, p-value: {p_value:.4f}, Confidence Level: {confidence_level:.2%}')

    # Adjusted logic for declaring a winner
    if confidence_level > 0.65:
        if success_rate_B_2 > success_rate_A_2:
            print("Group B is a winner!")
        else:
            print("Group A is a winner!")
    else:
        print("Not enough evidence to declare a winner.")
else:
    print("One or both groups are empty. Cannot perform the z-test.")

print("------------------------------------------------------------------")

# ---- Automatic Placement Test ----
group_A_3 = data[data['is_automatic_placement'] == 1].copy()
group_B_3 = data[data['is_automatic_placement'] == 0].copy()

# Calculate success rate for Group A
if not group_A_3.empty:
    group_A_3['success'] = group_A_3['num_ad_ids'] > 5
    success_A_3 = group_A_3['success'].sum()
    total_A_3 = group_A_3.shape[0]
    success_rate_A_3 = (success_A_3 / total_A_3) * 100
else:
    success_A_3 = 0
    total_A_3 = 0
    success_rate_A_3 = 0

# Calculate success rate for Group B
if not group_B_3.empty:
    group_B_3['success'] = group_B_3['num_ad_ids'] > 5
    success_B_3 = group_B_3['success'].sum()
    total_B_3 = group_B_3.shape[0]
    success_rate_B_3 = (success_B_3 / total_B_3) * 100
else:
    success_B_3 = 0
    total_B_3 = 0
    success_rate_B_3 = 0

# Perform z-test for Automatic Placement Test
if total_A_3 > 0 and total_B_3 > 0:
    count = [success_A_3, success_B_3]
    nobs = [total_A_3, total_B_3]
    
    stat, p_value = proportions_ztest(count, nobs)
    
    confidence_level = 1 - p_value
    print(f'\nAutomatic Placement Test:')
    print("Comparing whether ads that are automatically placed on the best platform (Instagram/Facebook) by Meta increase the ads' success.")
    print(f"Group A Success Rate: {success_rate_A_3:.2f}% ({success_A_3}/{total_A_3})")
    print(f"Group B Success Rate: {success_rate_B_3:.2f}% ({success_B_3}/{total_B_3})")
    print(f'z-statistic: {stat:.4f}, p-value: {p_value:.4f}, Confidence Level: {confidence_level:.2%}')

    # Logic for declaring a winner based on confidence level
    if confidence_level > 0.65:
        print("Group B is a winner!")
    else:
        print("Not enough evidence to declare a winner.")
else:
    print("One or both groups are empty. Cannot perform the z-test.")


print("------------------------------------------------------------------")

# Convert problematic columns to strings before conversion to R
data['cell_id'] = data['cell_id'].astype(str)
data['campaign_id'] = data['campaign_id'].astype(str)


# Convert problematic ID columns to strings before conversion to R
data['study_id'] = data['study_id'].astype(str)

# Convert data to R data frame
data_r = pandas2ri.py2rpy(data)

# Load necessary R libraries
dplyr = importr('dplyr')
ggplot2 = importr('ggplot2')

# Add to the R function to plot the success rates (%) for Group A and B for each test
plot = robjects.r('''
    function(data, success_rate_A_1, success_rate_B_1, success_rate_A_2, success_rate_B_2, success_rate_A_3, success_rate_B_3) {
        library(dplyr)
        library(ggplot2)

        # Create a data frame for the 3 tests' Group A and Group B success rates
        test_data <- data.frame(
            Test = rep(c('Customer Segment Optimisation', 'Ad Formatting/Interactivity', 'Automatic Placement'), each = 2),
            Group = rep(c('Group A', 'Group B'), times = 3),
            SuccessRate = c(success_rate_A_1, success_rate_B_1, success_rate_A_2, success_rate_B_2, success_rate_A_3, success_rate_B_3)
        )

        # Create a bar plot comparing Group A and Group B success rates for each test
        plot = ggplot(test_data, aes(x = Test, y = SuccessRate, fill = Group)) +
            geom_bar(stat = "identity", position = "dodge", color = "white", size = 0.5) +  # Add white outline to bars
            theme_minimal(base_family = "sans") +  # Ensure minimal theme with a base family
            labs(title = "Comparison of Success Rates (%) in Group A and Group B", x = "Test", y = "Success Rate (%)") +
            theme(
                axis.text.x = element_text(angle = 45, hjust = 1, color = "white"),  # Set x-axis text color to white
                axis.text.y = element_text(color = "white"),  # Set y-axis text color to white
                axis.title.x = element_text(color = "white"),  # Set x-axis title color to white
                axis.title.y = element_text(color = "white"),  # Set y-axis title color to white
                plot.title = element_text(color = "white"),  # Set plot title color to white
                legend.background = element_rect(fill = "transparent"),  # Set legend background transparent
                legend.text = element_text(color = "white"),  # Set legend text color to white
                legend.title = element_text(color = "white"),  # Set legend title color to white
                legend.key = element_rect(fill = "transparent"),  # Set legend key box fill to transparent
                legend.box.background = element_rect(color = "white", size = 0.5)  # Set legend box outline color to white
            ) +
            scale_fill_manual(
                values = c("Group A" = "#0073C2FF", "Group B" = "#9ecae1"),
                name = "Group",  # Legend title
                labels = c("Group A", "Group B")  # Legend labels
            )

        # Save the plot to a file
        ggsave("success_rate_comparison_groups_A_B.png", plot = plot, width = 20, height = 12, dpi = 1000)

        return(plot)  # Optionally return the plot object if needed
    }
''')(data_r, success_rate_A_1, success_rate_B_1, success_rate_A_2, success_rate_B_2, success_rate_A_3, success_rate_B_3)





# Display the plot
print(plot)

# Save the ggplot to a file
robjects.r('ggsave("success_rate_comparison_groups_A_B.png")')