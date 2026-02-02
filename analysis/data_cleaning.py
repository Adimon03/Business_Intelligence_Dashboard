"""
Business Intelligence Dashboard - Data Cleaning Script
Automated data cleaning for the Financial Sample dataset
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

def load_financial_data():
    """Load the financial sample data"""
    file_path = '../data/raw/Financial_Sample.xlsx'
    
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Data loaded successfully! Shape: {df.shape}")
        print(f"📊 Columns: {list(df.columns)}")
        
        # Display basic info
        print(f"\n=== DATASET OVERVIEW ===")
        print(f"Total Records: {len(df):,}")
        print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"Countries: {', '.join(df['Country'].unique())}")
        print(f"Products: {', '.join(df['Product'].unique())}")
        print(f"Customer Segments: {', '.join(df['Segment'].unique())}")
        
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def clean_financial_data(df):
    """Comprehensive data cleaning for financial sales data"""
    df_clean = df.copy()
    
    print(f"\n🧹 Starting data cleaning process...")
    
    # 1. Remove duplicates
    initial_rows = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f"🔄 Removed {initial_rows - len(df_clean)} duplicate rows")
    
    # 2. Handle missing values in Discount Band
    df_clean['Discount Band'] = df_clean['Discount Band'].fillna('None')
    print(f"🔧 Filled missing Discount Band values with 'None'")
    
    # 3. Fix column name (remove leading space)
    df_clean = df_clean.rename(columns={' Sales': 'Net_Sales'})
    print(f"📝 Fixed column name: ' Sales' -> 'Net_Sales'")
    
    # 4. Create derived features
    df_clean['Profit_Margin'] = (df_clean['Profit'] / df_clean['Gross Sales']) * 100
    df_clean['Discount_Rate'] = (df_clean['Discounts'] / df_clean['Gross Sales']) * 100
    df_clean['Quarter'] = df_clean['Date'].dt.quarter
    df_clean['Day_of_Week'] = df_clean['Date'].dt.dayofweek
    df_clean['Revenue_per_Unit'] = df_clean['Net_Sales'] / df_clean['Units Sold']
    
    # 5. Create categorical features
    df_clean['Sales_Category'] = pd.cut(df_clean['Net_Sales'], 
                                       bins=[0, 50000, 100000, 200000, float('inf')],
                                       labels=['Low', 'Medium', 'High', 'Very High'])
    
    df_clean['Units_Category'] = pd.cut(df_clean['Units Sold'],
                                       bins=[0, 1000, 2000, 3000, float('inf')],
                                       labels=['Low Volume', 'Medium Volume', 'High Volume', 'Very High Volume'])
    
    # 6. Create performance indicators
    df_clean['High_Performer'] = (df_clean['Profit_Margin'] > df_clean['Profit_Margin'].median()).astype(int)
    df_clean['Premium_Product'] = (df_clean['Sale Price'] > 100).astype(int)
    
    print(f"✨ Created derived features: Profit_Margin, Discount_Rate, Quarter, Revenue_per_Unit, etc.")
    print(f"✅ Data cleaning completed! Final shape: {df_clean.shape}")
    
    return df_clean

def assess_data_quality(df):
    """Assess the quality of cleaned data"""
    print(f"\n📋 === DATA QUALITY ASSESSMENT ===")
    
    # Basic statistics
    print(f"📊 Total records: {len(df):,}")
    print(f"📈 Total columns: {len(df.columns)}")
    print(f"📅 Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    # Missing values check
    missing_values = df.isnull().sum().sum()
    print(f"❓ Total missing values: {missing_values}")
    
    # Duplicate check
    duplicates = df.duplicated().sum()
    print(f"🔄 Duplicate records: {duplicates}")
    
    # Financial metrics validation
    print(f"\n💰 === FINANCIAL METRICS VALIDATION ===")
    print(f"💵 Total Gross Sales: ${df['Gross Sales'].sum():,.2f}")
    print(f"💸 Total Net Sales: ${df['Net_Sales'].sum():,.2f}")
    print(f"💰 Total Profit: ${df['Profit'].sum():,.2f}")
    print(f"📊 Average Profit Margin: {df['Profit_Margin'].mean():.2f}%")
    print(f"🏷️ Average Discount Rate: {df['Discount_Rate'].mean():.2f}%")
    
    # Performance insights
    print(f"\n🎯 === PERFORMANCE INSIGHTS ===")
    print(f"🏆 High Performing Records: {df['High_Performer'].sum()} ({(df['High_Performer'].mean()*100):.1f}%)")
    print(f"💎 Premium Products: {df['Premium_Product'].sum()} ({(df['Premium_Product'].mean()*100):.1f}%)")
    
    return True

def export_cleaned_data(df, filename='cleaned_financial_data.csv'):
    """Export cleaned data for analysis and database import"""
    
    # Ensure processed directory exists
    os.makedirs('../data/processed', exist_ok=True)
    
    output_path = f'../data/processed/{filename}'
    df.to_csv(output_path, index=False)
    print(f"📁 Cleaned data exported to: {output_path}")
    
    # Also create Excel version
    excel_path = output_path.replace('.csv', '.xlsx')
    df.to_excel(excel_path, index=False)
    print(f"📊 Excel version exported to: {excel_path}")
    
    # Create summary report
    summary_path = output_path.replace('.csv', '_summary.txt')
    with open(summary_path, 'w') as f:
        f.write("BUSINESS INTELLIGENCE DATA CLEANING SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Original records: {len(df):,}\n")
        f.write(f"Columns: {len(df.columns)}\n")
        f.write(f"Date range: {df['Date'].min()} to {df['Date'].max()}\n")
        f.write(f"Countries: {', '.join(df['Country'].unique())}\n")
        f.write(f"Products: {', '.join(df['Product'].unique())}\n")
        f.write(f"Customer Segments: {', '.join(df['Segment'].unique())}\n")
        f.write(f"Total Gross Sales: ${df['Gross Sales'].sum():,.2f}\n")
        f.write(f"Total Net Sales: ${df['Net_Sales'].sum():,.2f}\n")
        f.write(f"Total Profit: ${df['Profit'].sum():,.2f}\n")
        f.write(f"Average Profit Margin: {df['Profit_Margin'].mean():.2f}%\n")
        f.write(f"Average Discount Rate: {df['Discount_Rate'].mean():.2f}%\n")
    
    print(f"📋 Summary report saved to: {summary_path}")
    return output_path

def main():
    """Main execution function"""
    print("🚀 Starting Business Intelligence Data Cleaning Process")
    print("=" * 60)
    
    # Load data
    df = load_financial_data()
    if df is None:
        print("❌ Cannot proceed without data")
        return
    
    # Clean data
    df_clean = clean_financial_data(df)
    
    # Assess quality
    assess_data_quality(df_clean)
    
    # Export cleaned data
    export_path = export_cleaned_data(df_clean)
    
    print(f"\n🎉 === PROCESS COMPLETED SUCCESSFULLY ===")
    print(f"✅ Data cleaning completed!")
    print(f"📁 Cleaned data saved to: {export_path}")
    print(f"📊 Ready for EDA and database import")
    print(f"🔄 Next steps:")
    print(f"   1. Run EDA analysis")
    print(f"   2. Set up database")
    print(f"   3. Create Power BI dashboard")

if __name__ == "__main__":
    main()