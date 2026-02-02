# Business Intelligence Dashboard - Setup Guide

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.8+** installed
- **Power BI Desktop** (free from Microsoft)
- **Git** (for cloning the repository)

## 📥 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/Adimon03/Business_Intelligence_Dashboard.git
cd Business_Intelligence_Dashboard
```

### Step 2: Install Python Dependencies
```bash
pip install -r analysis/requirements.txt
```

### Step 3: Run Data Analysis Pipeline
```bash
# Navigate to analysis folder
cd analysis

# Run data cleaning
python data_cleaning.py

# Set up database
python database_setup.py
```

## 📊 Power BI Dashboard Setup

### Option 1: Use Pre-built Dashboard
1. **Download Power BI Desktop** (free)
2. **Open**: `powerbi/business_intelligence_dashboard.pbix`
3. **Explore** the interactive dashboard

### Option 2: Connect to Database
1. **Open Power BI Desktop**
2. **Get Data** → **Database** → **SQLite database**
3. **Browse to**: `data/business_intelligence.db`
4. **Select**: `sales_transactions` table
5. **Load** the data (700 records, 25+ columns)

### Option 3: Use Excel Data
1. **Get Data** → **File** → **Excel workbook**
2. **Browse to**: `data/processed/cleaned_financial_data.xlsx`
3. **Load** the data

## 🎯 Creating Your Dashboard

### Essential Visualizations
1. **KPI Cards**: Total Sales, Profit, Margin, Transactions
2. **Line Chart**: Monthly sales trends
3. **Bar Chart**: Sales by customer segment
4. **Pie Chart**: Product performance
5. **Map**: Geographic distribution

### Recommended Layout
- **Top Row**: KPI cards
- **Middle**: Main trend chart
- **Bottom**: Supporting analysis charts

## 📈 Key Metrics Available

### Financial Metrics
- `net_sales`: Revenue ($118.7M total)
- `profit`: Profit amount ($16.9M total)
- `profit_margin`: Profit percentage (25.99% avg)
- `discount_rate`: Discount percentage

### Dimensions
- `segment`: Customer segments
- `country`: Geographic regions
- `product`: Product lines
- `transaction_date`: Time analysis

### Derived Fields
- `sales_category`: Performance tiers
- `high_performer`: Top transactions
- `premium_product`: Premium indicators

## 🔧 Troubleshooting

### Common Issues

**Python Dependencies**
```bash
# If installation fails
pip install --upgrade pip
pip install -r analysis/requirements.txt --user
```

**Power BI Connection**
- Ensure SQLite database exists in `data/` folder
- Try Excel file if SQLite doesn't work
- Check file paths are correct

**Data Loading**
- Run `data_cleaning.py` first
- Check that `Financial_Sample.xlsx` is in `data/raw/`
- Verify all file paths

## 📊 Expected Results

### After Setup
- ✅ 700 transaction records loaded
- ✅ 25+ analysis columns available
- ✅ SQLite database created
- ✅ Power BI dashboard functional

### Key Insights
- **Government segment**: Top performer (44.2%)
- **Paseo product**: Best seller (27.8%)
- **Q4 performance**: Peak season ($51.7M)
- **US market**: Leading region (21.1%)

## 🎯 Next Steps

1. **Customize dashboard** for specific needs
2. **Add advanced analytics** (forecasting, trends)
3. **Create additional pages** for detailed analysis
4. **Publish to Power BI Service** for sharing
5. **Set up data refresh** for updated insights

## 📞 Support

For issues or questions:
- **Check troubleshooting** section above
- **Review file paths** and dependencies
- **Ensure data files** are in correct locations
- **Verify Python environment** is set up correctly

## 🎉 Success Checklist

- [ ] Repository cloned successfully
- [ ] Python dependencies installed
- [ ] Data cleaning completed
- [ ] Database created and populated
- [ ] Power BI dashboard opened
- [ ] Key metrics visible and accurate
- [ ] Interactive features working

**Your Business Intelligence Dashboard is ready for analysis!** 🚀📊