"""
Business Intelligence Dashboard - Database Setup
Create SQLite database and import cleaned data
"""

import sqlite3
import pandas as pd
import os
from datetime import datetime

def create_sqlite_database():
    """Create SQLite database and import data"""
    
    print("🗄️ Creating Business Intelligence Database...")
    
    # Create database connection
    db_path = '../data/business_intelligence.db'
    os.makedirs('../data', exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            segment TEXT NOT NULL,
            country TEXT NOT NULL,
            product TEXT NOT NULL,
            discount_band TEXT,
            units_sold REAL NOT NULL,
            manufacturing_price REAL NOT NULL,
            sale_price REAL NOT NULL,
            gross_sales REAL NOT NULL,
            discounts REAL DEFAULT 0,
            net_sales REAL NOT NULL,
            cogs REAL NOT NULL,
            profit REAL NOT NULL,
            transaction_date DATE NOT NULL,
            month_number INTEGER,
            month_name TEXT,
            year INTEGER,
            quarter INTEGER,
            day_of_week INTEGER,
            profit_margin REAL,
            discount_rate REAL,
            revenue_per_unit REAL,
            sales_category TEXT,
            units_category TEXT,
            high_performer INTEGER DEFAULT 0,
            premium_product INTEGER DEFAULT 0,
            created_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("✅ Database table created successfully")
    
    # Load and import data
    cleaned_file = '../data/processed/cleaned_financial_data.csv'
    
    if not os.path.exists(cleaned_file):
        print(f"❌ Error: Cleaned data file not found: {cleaned_file}")
        print("💡 Please run data_cleaning.py first")
        return None
    
    df = pd.read_csv(cleaned_file)
    print(f"📊 Loaded {len(df)} records from cleaned data")
    
    # Column mapping
    column_mapping = {
        'Segment': 'segment',
        'Country': 'country', 
        'Product': 'product',
        'Discount Band': 'discount_band',
        'Units Sold': 'units_sold',
        'Manufacturing Price': 'manufacturing_price',
        'Sale Price': 'sale_price',
        'Gross Sales': 'gross_sales',
        'Discounts': 'discounts',
        'Net_Sales': 'net_sales',
        'COGS': 'cogs',
        'Profit': 'profit',
        'Date': 'transaction_date',
        'Month Number': 'month_number',
        'Month Name': 'month_name',
        'Year': 'year',
        'Quarter': 'quarter',
        'Day_of_Week': 'day_of_week',
        'Profit_Margin': 'profit_margin',
        'Discount_Rate': 'discount_rate',
        'Revenue_per_Unit': 'revenue_per_unit',
        'Sales_Category': 'sales_category',
        'Units_Category': 'units_category',
        'High_Performer': 'high_performer',
        'Premium_Product': 'premium_product'
    }
    
    df_import = df.rename(columns=column_mapping)
    
    # Select only columns that exist in both mapping and dataframe
    available_columns = [new_col for old_col, new_col in column_mapping.items() if old_col in df.columns]
    df_final = df_import[available_columns]
    
    # Import to SQLite
    df_final.to_sql('sales_transactions', conn, if_exists='replace', index=False)
    
    print(f"✅ Data imported to SQLite database: {db_path}")
    print(f"📊 Records imported: {len(df_final):,}")
    
    # Verify import
    cursor.execute("SELECT COUNT(*) FROM sales_transactions")
    count = cursor.fetchone()[0]
    print(f"🔍 Verification: {count:,} records in database")
    
    # Create some summary queries
    print(f"\n📈 Database Summary:")
    
    cursor.execute("SELECT COUNT(DISTINCT country) FROM sales_transactions")
    countries = cursor.fetchone()[0]
    print(f"🌍 Countries: {countries}")
    
    cursor.execute("SELECT COUNT(DISTINCT product) FROM sales_transactions")
    products = cursor.fetchone()[0]
    print(f"📦 Products: {products}")
    
    cursor.execute("SELECT COUNT(DISTINCT segment) FROM sales_transactions")
    segments = cursor.fetchone()[0]
    print(f"👥 Customer Segments: {segments}")
    
    cursor.execute("SELECT SUM(net_sales), SUM(profit) FROM sales_transactions")
    totals = cursor.fetchone()
    print(f"💰 Total Sales: ${totals[0]:,.2f}")
    print(f"💵 Total Profit: ${totals[1]:,.2f}")
    
    conn.close()
    
    print(f"\n🎉 SQLite database created successfully!")
    print(f"📍 Database location: {os.path.abspath(db_path)}")
    print(f"🔗 Ready for Power BI connection!")
    
    return db_path

if __name__ == "__main__":
    create_sqlite_database()