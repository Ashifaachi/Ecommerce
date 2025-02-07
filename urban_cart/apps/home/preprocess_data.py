import pandas as pd
import os

# Update dataset directory path
DATASET_DIR = "C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets"

# Dataset filenames
FILES = ["Casual Shoes.csv", "Formal Shoes.csv", "Kids Shoes.csv", "Shoes.csv", "Sports Shoes.csv"]

# Columns we need
REQUIRED_COLUMNS = ["name", "main_category", "sub_category", "image", "link", "ratings", "no_of_ratings", "discount_price", "actual_price"]

# Read and merge datasets
dataframes = []
for file in FILES:
    file_path = os.path.join(DATASET_DIR, file)
    
    if os.path.exists(file_path):  # Ensure file exists
        df = pd.read_csv(file_path)

        # Standardize column names (remove spaces, make lowercase)
        df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

        # Select required columns (only if they exist in the dataset)
        selected_columns = [col.lower() for col in REQUIRED_COLUMNS if col.lower() in df.columns]
        
        if selected_columns:
            df = df[selected_columns]

            # Ensure the "main_category" and "sub_category" columns exist, handle if missing
            if 'main_category' not in df.columns or 'sub_category' not in df.columns:
                print(f"⚠️ Warning: 'main_category' or 'sub_category' column missing in {file}. Adding placeholders.")
                df['main_category'] = 'Unknown'  # Add default value if missing
                df['sub_category'] = 'Unknown'  # Add default value if missing

            # Create a "tags" column for Content-Based Filtering
            df["tags"] = df["main_category"] + " " + df["sub_category"]

            dataframes.append(df)
        else:
            print(f"⚠️ Warning: Required columns missing in {file}")
    else:
        print(f"⚠️ Warning: {file} not found!")

# Merge all datasets
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)

    # Fill missing values
    final_df.fillna("", inplace=True)

    # Save cleaned dataset inside your Django project
    SAVE_PATH = "C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/apps/home/data/cleaned_data.csv"
    final_df.to_csv(SAVE_PATH, index=False)

    print(f"✅ Data Preprocessing Completed! File saved at: {SAVE_PATH}")
else:
    print("❌ No datasets were found or processed!")
