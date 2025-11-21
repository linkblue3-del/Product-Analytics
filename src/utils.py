"""
Utility functions for product analytics.

Best Practices Demonstrated:
- Type hints
- Docstrings
- Error handling
- Reusable functions
"""

import pandas as pd
from typing import Dict, List


def format_currency(amount: float) -> str:
    """Format number as currency.
    
    Args:
        amount: Dollar amount
        
    Returns:
        Formatted string with $ and commas
        
    Example:
        >>> format_currency(1234.56)
        '$1,234.56'
    """
    return f"${amount:,.2f}"


def calculate_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate revenue from quantity and price.
    
    Best Practice: Create derived columns with clear names.
    
    Args:
        df: DataFrame with 'quantity' and 'price' columns
        
    Returns:
        DataFrame with added 'revenue' column
    """
    df = df.copy()
    df['revenue'] = df['quantity'] * df['price']
    return df


def get_top_n(df: pd.DataFrame, column: str, n: int = 5) -> pd.DataFrame:
    """Get top N rows by a column value.
    
    Args:
        df: Input DataFrame
        column: Column to sort by
        n: Number of rows to return (default: 5)
        
    Returns:
        Top N rows
    """
    return df.nlargest(n, column)


def validate_data(df: pd.DataFrame) -> Dict[str, bool]:
    """Validate data quality.
    
    Best Practice: Always validate your data!
    
    Args:
        df: DataFrame to validate
        
    Returns:
        Dictionary of validation results
    """
    validations = {
        'no_missing_values': df.isnull().sum().sum() == 0,
        'positive_prices': (df['price'] > 0).all() if 'price' in df.columns else None,
        'positive_quantities': (df['quantity'] > 0).all() if 'quantity' in df.columns else None,
        'valid_dates': pd.to_datetime(df['order_date'], errors='coerce').notna().all() if 'order_date' in df.columns else None
    }
    return validations


def print_summary(metrics: Dict) -> None:
    """Print metrics dictionary in readable format.
    
    Args:
        metrics: Dictionary of metric name -> value
    """
    print("=" * 50)
    print("SUMMARY METRICS")
    print("=" * 50)
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            if isinstance(value, float):
                print(f"{key}: {value:,.2f}")
            else:
                print(f"{key}: {value:,}")
        else:
            print(f"{key}: {value}")
    print("=" * 50)