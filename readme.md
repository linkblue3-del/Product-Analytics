# Product Analytics Workshop

E-commerce product analytics project for learning Git collaboration workflows.

## Overview

This is a simplified project focused on **collaboration best practices**, not complex coding. You'll learn to:
- Work in parallel with teammates
- Handle merge conflicts
- Create and review Pull Requests
- Apply Databricks best practices

## Scenario

You're joining an analytics team at an e-commerce company. Your job: Build analytics capabilities for product performance tracking.

## Setup Instructions

### 1. Fork This Repository

Click "Fork" button on GitHub to create your copy.

### 2. Clone to Databricks
```
Databricks → Repos → Add Repo
Git URL: https://github.com/YOUR_USERNAME/product-analytics-workshop
Provider: GitHub
Authenticate with Personal Access Token
```

### 3. Verify Setup
```python
# Run in Databricks notebook
import pandas as pd
df = pd.read_csv('../data/sample_sales.csv')
print(f"✅ Data loaded: {len(df)} rows")
```

## Project Structure
```
notebooks/
  01_data_loading.ipynb       # Core metrics (BOTH users will modify)
  02_analysis_template.ipynb  # Template for new notebooks
  
data/
  sample_sales.csv            # 1000 rows of sales data
  
src/
  utils.py                    # Helper functions
```

## Data Dictionary

**sample_sales.csv:**
- `order_id`: Unique order identifier
- `product_id`: Product identifier (P001-P100)
- `product_name`: Product name
- `category`: Product category (Electronics, Clothing, Home, Books, Sports)
- `quantity`: Items purchased
- `price`: Unit price ($)
- `order_date`: Purchase date (YYYY-MM-DD)
- `customer_id`: Customer identifier
- `region`: Geographic region (North, South, East, West)

## Workshop Exercises

### Round 1: Parallel Development
- **User A:** Add revenue analytics
- **User B:** Add customer analytics
- **Result:** Merge conflict (intentional!)
- **Resolution:** Combine both analytics

### Round 2: Independent Features
- **User A:** Create revenue visualization
- **User B:** Create customer visualization
- **Result:** No conflicts (different files)

## Best Practices Demonstrated

✅ Feature branch workflow  
✅ Parameterization with widgets  
✅ Clear documentation  
✅ Code review process  
✅ Conflict resolution  
✅ Professional Git workflows  

## Key Concepts

**Databricks Best Practices:**
- Use widgets for environment/parameters
- Document with markdown cells
- Write clear, reusable functions
- Avoid hardcoded values

**Git Best Practices:**
- Descriptive commit messages
- Small, focused branches
- Meaningful PR descriptions
- Constructive code review

## Support

Questions? Contact workshop instructor.

## License

MIT License - Free for educational use