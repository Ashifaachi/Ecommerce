# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import plotly.express as px
# import os
# from django.core.management.base import BaseCommand
# from apps.admin1.models import Product,MainCategory,SubCategory,Manufacturer




# # Define the command class
# class Command(BaseCommand):
#     help = 'Imports CSV data into the database'

#     def handle(self, *args, **kwargs):
#         # Define the absolute path to the datasets folder
#         # Define the path to the datasets directory
#         DATASETS_DIR = 'C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets'

#         # Load the CSV files with full path
#         casual_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Casual Shoes.csv'))
#         formal_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Formal Shoes.csv'))
#         sports_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Sports Shoes.csv'))
#         shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Shoes.csv'))
#         kids_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Kids Shoes.csv'))
#         DATASETS = [

#             casual_shoes,
#             formal_shoes,
#             sports_shoes,
#             shoes,
#             kids_shoes,]
#         return DATASETS
#     def clean_price(price):
#         for dataset in DATASETS:
#             data = pd.read_csv(dataset)
#             df = data
#             df.isnull().sum()
#             # Droping the columns with 70% or more missing data
#             perc = 70.0 
#             min_count =  int(((100 - perc)/100) * df.shape[1] + 1)
#             mod_df = df.dropna(axis = 1, thresh = min_count)
#             # Removing the ₹ sign
#             mod_df["discount_price"] = mod_df["discount_price"].str.split(" ", expand = True).get(0).str.split("₹", expand = True).get(1)
#             mod_df["actual_price"] = mod_df["actual_price"].str.split(" ", expand = True).get(0).str.split("₹", expand = True).get(1)
#             # Change commas to dots and change the type to float
#             mod_df['discount_price'] = mod_df["discount_price"].str.replace(',', '').astype(float)
#             mod_df["actual_price"] = mod_df["actual_price"].str.replace(',', '').astype(float)

#             # Extract the digits and change the type to float
#             mod_df['ratings'] = mod_df['ratings'].replace(['Get','FREE','₹68.99', '₹65','₹70', '₹100', '₹99', '₹2.99'], '0.0')
#             mod_df['ratings'] = mod_df["ratings"].astype(float)
#             mod_df['ratings'].unique()
#             # Add column 'correct_no_of_ratings' which value is 'True' if 'no_of_ratings' begins from digit 
#             mod_df['no_of_ratings'] = mod_df['no_of_ratings'].astype(str)
#             mod_df['correct_no_of_ratings'] = pd.Series([mod_df['no_of_ratings'][x][0].isdigit() for x in range(len(mod_df['no_of_ratings']))])
#             # Drop columns with incorrect 'no_of_ratings'
#             mod_df = mod_df[mod_df['correct_no_of_ratings'] == True]
#             mod_df['correct_no_of_ratings'].value_counts()
#             # Change the type to float
#             mod_df["no_of_ratings"] = mod_df["no_of_ratings"].str.replace(',', '').astype(float)
#             # Let us check and create a dataframe of missing ratings
#             missing_no_of_ratings = mod_df[mod_df['actual_price'].isnull()]
#             # Since our further analysis is based on the price column so let us drop it.
#             df = mod_df.dropna(subset=['actual_price','discount_price'])
#             df['manufacturer'] = df['name'].str.split(' ').str[0]
#             cols = df.columns.tolist()
#             cols
#             cols = ['name',
                    
#                     'manufacturer',
#                     'main_category',
#                     'sub_category',
#                     'image',
#                     'link',
#                     'ratings',
#                     'no_of_ratings',
#                     'discount_price',
#                     'actual_price']
#             df = df[cols]



#     def import_data():
#         for dataset in DATASETS:
#         # Load the dataset
#            data = pd.read_csv(dataset)

#            for _, row in data.iterrows():
#             # Get or create MainCategory
#             main_category, _ = MainCategory.objects.get_or_create(name=row['main_category'])

#             # Get or create SubCategory
#             sub_category, _ = SubCategory.objects.get_or_create(name=row['sub_category'], main_category=main_category)
#             # Get or create manufacturer
#             manufacturer, _ = Manufacturer.objects.get_or_create(name=row['manufacturer'])

#             # Create Product
#             Product.objects.create(
#                 name=row['name'],
#                 main_category=main_category,
#                 sub_category=sub_category,
#                 image_url=row['image_url'],
#                 site_link=row['site_link'],
#                 ratings=row['ratings'] if not pd.isna(row['ratings']) else None,
#                 no_of_ratings=row['no_of_ratings'] if not pd.isna(row['no_of_ratings']) else None,
#                 discount_price=clean_price(row['discount_price']),
#                 actual_price=clean_price(row['actual_price']),
#             )

# # Call the import function
# if __name__ == "__main__":
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_cart.settings')
#     import django
#     django.setup()
#     import_data()
#     print("Data imported successfully!")


        
    
    
    
    
    




        








# import os
# import pandas as pd
# from django.core.management.base import BaseCommand
# from apps.admin1.models import Product, MainCategory, SubCategory

# # Define the command class
# class Command(BaseCommand):
#     help = 'Imports CSV data into the database'

#     # Define the absolute path to the datasets folder
#     DATASETS_DIR = 'C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets'

#     def handle(self, *args, **kwargs):
#         # Load the CSV files with full path
#         casual_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Casual Shoes.csv'))
#         formal_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Formal Shoes.csv'))
#         sports_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Sports Shoes.csv'))
#         shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Shoes.csv'))
#         kids_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Kids Shoes.csv'))

#         # List of datasets
#         DATASETS = [
#             casual_shoes,
#             formal_shoes,
#             sports_shoes,
#             shoes,
#             kids_shoes,
#         ]

#         # Clean prices and import data
#         self.clean_and_import_data(DATASETS)

#         # Confirmation message
#         self.stdout.write(self.style.SUCCESS("Data imported successfully!"))

#     @staticmethod
#     def clean_price(df, price_column):
#         # Removing the ₹ sign and converting price to float
#         df[price_column] = df[price_column].str.split(" ", expand=True).get(0).str.split("₹", expand=True).get(1)
#         df[price_column] = df[price_column].str.replace(',', '').astype(float)
#         return df

#     def clean_and_import_data(self, datasets):
#         for data in datasets:
#             # Clean price columns
#             data = self.clean_price(data, 'discount_price')
#             data = self.clean_price(data, 'actual_price')

#             # Drop columns with more than 70% missing data
#             perc = 70.0
#             min_count = int(((100 - perc) / 100) * data.shape[1] + 1)
#             mod_df = data.dropna(axis=1, thresh=min_count)

#             # Import data into the database
#             for _, row in mod_df.iterrows():
#                 # Get or create MainCategory
#                 main_category, _ = MainCategory.objects.get_or_create(name=row['main_category'])

#                 # Get or create SubCategory
#                 sub_category, _ = SubCategory.objects.get_or_create(name=row['sub_category'], main_category=main_category)

#                 # Create Product
#                 Product.objects.create(
#                     name=row['name'],
#                     main_category=main_category,
#                     sub_category=sub_category,
#                     image_url=row['image_url'],
#                     site_link=row['site_link'],
#                     ratings=row['ratings'] if not pd.isna(row['ratings']) else None,
#                     no_of_ratings=row['no_of_ratings'] if not pd.isna(row['no_of_ratings']) else None,
#                     discount_price=row['discount_price'],
#                     actual_price=row['actual_price'],
#                 )

# import os
# import pandas as pd
# from django.core.management.base import BaseCommand
# from apps.admin1.models import Product, MainCategory, SubCategory

# # Define the command class
# class Command(BaseCommand):
#     help = 'Imports CSV data into the database'

#     # Define the absolute path to the datasets folder
#     DATASETS_DIR = 'C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets'

#     def handle(self, *args, **kwargs):
#         # Load the CSV files with full path
#         casual_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Casual Shoes.csv'))
#         formal_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Formal Shoes.csv'))
#         sports_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Sports Shoes.csv'))
#         shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Shoes.csv'))
#         kids_shoes = pd.read_csv(os.path.join(self.DATASETS_DIR, 'Kids Shoes.csv'))

#         # List of datasets
#         DATASETS = [
#             casual_shoes,
#             formal_shoes,
#             sports_shoes,
#             shoes,
#             kids_shoes,
#         ]

#         # Clean and import data
#         self.clean_and_import_data(DATASETS)

#         # Confirmation message
#         self.stdout.write(self.style.SUCCESS("Data imported successfully!"))

#     @staticmethod
#     def clean_price(df, price_column):
#         # Removing the ₹ sign and converting price to float
#         df[price_column] = df[price_column].str.split(" ", expand=True).get(0).str.split("₹", expand=True).get(1)
#         df[price_column] = df[price_column].str.replace(',', '').astype(float)
#         return df

#     def clean_and_import_data(self, datasets):
#         for data in datasets:
#             # Clean price columns
#             data = self.clean_price(data, 'discount_price')
#             data = self.clean_price(data, 'actual_price')

#             # Drop columns with more than 70% missing data
#             perc = 70.0
#             min_count = int(((100 - perc) / 100) * data.shape[1] + 1)
#             mod_df = data.dropna(axis=1, thresh=min_count)

#             # Import data into the database
#             for _, row in mod_df.iterrows():
#                 # Get or create MainCategory
#                 main_category, _ = MainCategory.objects.get_or_create(name=row['main_category'])

#                 # Get or create SubCategory
#                 sub_category, _ = SubCategory.objects.get_or_create(name=row['sub_category'], main_category=main_category)

#                 # Check if 'image_url' column exists before accessing it
#                 image_url = row['image'] if 'image' in row else None

#                 # Create Product
#                 Product.objects.create(
#                     name=row['name'],
#                     main_category=main_category,
#                     sub_category=sub_category,
#                     image_url=image_url,  # Use None if column doesn't exist
#                     site_link=row['link'],
#                     product_stock=100,  # Default stock value of 100
#                     ratings=row['ratings'] if not pd.isna(row['ratings']) else None,
#                     no_of_ratings=row['no_of_ratings'] if not pd.isna(row['no_of_ratings']) else None,
#                     discount_price=row['discount_price'],
#                     actual_price=row['actual_price'],
#                 )

import os
import pandas as pd
from django.core.management.base import BaseCommand
from apps.admin1.models import Product, MainCategory, SubCategory, Manufacturer

class Command(BaseCommand):
    help = 'Imports CSV data into the database'

    def handle(self, *args, **kwargs):
        # Define the absolute path to the datasets folder
        DATASETS_DIR = 'C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets'

        # Load the CSV files with full path
        casual_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Casual Shoes.csv'))
        formal_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Formal Shoes.csv'))
        sports_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Sports Shoes.csv'))
        shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Shoes.csv'))
        kids_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Kids Shoes.csv'))
        DATASETS = [casual_shoes, formal_shoes, sports_shoes, shoes, kids_shoes]

        # Clean the data and import it into the database
        self.import_data(DATASETS)

        # Confirmation message
        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))

    def clean_price(self, df, price_column):
        """Clean the price columns by removing '₹' and converting to float"""
        df[price_column] = df[price_column].str.split(" ", expand=True).get(0).str.split("₹", expand=True).get(1)
        df[price_column] = df[price_column].str.replace(',', '').astype(float)
        return df

    # def clean_data(self, df):
    #     """Clean the dataset by handling missing values, removing unwanted data, and converting columns"""
    #     # Drop columns with 70% or more missing data
    #     perc = 70.0
    #     min_count = int(((100 - perc) / 100) * df.shape[1] + 1)
    #     df = df.dropna(axis=1, thresh=min_count)

    #     # Clean the 'discount_price' and 'actual_price'
    #     df = self.clean_price(df, 'discount_price')
    #     df = self.clean_price(df, 'actual_price')

    #     # Clean 'ratings'
    #     df['ratings'] = df['ratings'].replace(['Get', 'FREE', '₹68.99', '₹65', '₹70', '₹100', '₹99', '₹2.99'], '0.0')
    #     df['ratings'] = df['ratings'].astype(float)

    #     # Clean 'no_of_ratings' (keep only rows where 'no_of_ratings' is a digit)
    #     df['no_of_ratings'] = df['no_of_ratings'].astype(str)
    #     df['correct_no_of_ratings'] = df['no_of_ratings'].str[0].isdigit()
    #     df = df[df['correct_no_of_ratings'] == True]
    #     df['no_of_ratings'] = df['no_of_ratings'].str.replace(',', '').astype(float)

    #     # Remove rows with missing prices
    #     df = df.dropna(subset=['actual_price', 'discount_price'])

    #     # Add manufacturer info (based on 'name')
    #     df['manufacturer'] = df['name'].str.split(' ').str[0]

    #     # Select relevant columns for import
    #     cols = ['name', 'manufacturer', 'main_category', 'sub_category', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']
    #     df = df[cols]

    #     return df
    def clean_data(self, df):
        """Clean the dataset by handling missing values, removing unwanted data, and converting columns"""
        # Drop columns with 70% or more missing data
        perc = 70.0
        min_count = int(((100 - perc) / 100) * df.shape[1] + 1)
        df = df.dropna(axis=1, thresh=min_count)

        # Clean the 'discount_price' and 'actual_price'
        df = self.clean_price(df, 'discount_price')
        df = self.clean_price(df, 'actual_price')

        # Clean 'ratings'
        df['ratings'] = df['ratings'].replace(['Get', 'FREE', '₹68.99', '₹65', '₹70', '₹100', '₹99', '₹2.99'], '0.0')
        df['ratings'] = df['ratings'].astype(float)

        # Clean 'no_of_ratings' (keep only rows where 'no_of_ratings' is a digit)
        df['no_of_ratings'] = df['no_of_ratings'].astype(str)
        df['correct_no_of_ratings'] = df['no_of_ratings'].apply(lambda x: str(x)[0].isdigit() if pd.notnull(x) else False)
        df = df[df['correct_no_of_ratings'] == True]
        df['no_of_ratings'] = df['no_of_ratings'].str.replace(',', '').astype(float)

        # Remove rows with missing prices
        df = df.dropna(subset=['actual_price', 'discount_price'])

        # Add manufacturer info (based on 'name')
        df['manufacturer'] = df['name'].str.split(' ').str[0]

        # Select relevant columns for import
        cols = ['name', 'manufacturer', 'main_category', 'sub_category', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']
        df = df[cols]

        return df


    def import_data(self, datasets):
        """Import cleaned data into the database"""
        for dataset in datasets:
            # Clean the data
            cleaned_data = self.clean_data(dataset)

            # Import the data into the database
            for _, row in cleaned_data.iterrows():
                # Get or create MainCategory
                main_category, _ = MainCategory.objects.get_or_create(name=row['main_category'])

                # Get or create SubCategory
                sub_category, _ = SubCategory.objects.get_or_create(name=row['sub_category'], main_category=main_category)

                # Get or create manufacturer
                manufacturer, _ = Manufacturer.objects.get_or_create(name=row['manufacturer'])

                # Check if 'image' column exists and assign it to 'image_url' field
                image_url = row['image'] if 'image' in row else None

                # Create Product with default stock of 100
                Product.objects.create(
                    name=row['name'],
                    main_category=main_category,
                    sub_category=sub_category,
                    manufacturer=manufacturer,
                    image_url=image_url,  # Use None if column doesn't exist
                    site_link=row['link'],
                    product_stock=100,  # Default stock value of 100
                    ratings=row['ratings'] if not pd.isna(row['ratings']) else None,
                    no_of_ratings=row['no_of_ratings'] if not pd.isna(row['no_of_ratings']) else None,
                    discount_price=row['discount_price'],
                    actual_price=row['actual_price'],
                )
