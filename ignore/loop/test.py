dataset = [1,2,3]
users_bt_18_40 = 2


dataset["is_age_18-40"] = dataset.age.gt(40)
users_between_18_40 = dataset[dataset["is_age_18-40"]==True]
has_account_between_18_40 = len(users_between_18_40[users_between_18_40["has_facebook_account"] == 1])
percentage_of_between_18_40 = has_account_between_18_40 / len(users_between_18_40) * 100
print("The total percentage (%) of Facebook users of age 18-40: ", percentage_of_between_18_40, "%")


dataset["is_age_gt_40"] = dataset.age.gt(40)
users_gt_40 = dataset[dataset["is_age_gt_40"] == True]
print(users_gt_40)
has_account_gt_40 = len(users_gt_40[users_gt_40["has_facebook_account"] == 1])
percentage_gt_40 = has_account_gt_40 / len(users_gt_40) * 100
print("The total percentage (%) of Facebook users of age greater than 40: ", percentage_gt_40, "%")