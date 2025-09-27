import joblib
feature_columns = joblib.load(r'C:\Users\msent\OneDrive\Desktop\SIH\feature_columns.pkl')
template_lines = ["new_data_dict = {"]
for feature in feature_columns:
    template_lines.append(f"    '{feature}': 0,")
template_lines.append("}")
with open("feature_template.py", "w") as f:
    f.write("\n".join(template_lines))
print("Feature template generated in feature_template.py")
