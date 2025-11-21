# Workflow Guide

## Git Workflow for This Project

### 1. Starting New Work
```bash
# Always start from main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Making Changes

**Best Practices:**
- Make small, logical commits
- Test your changes before committing
- Write clear commit messages
```bash
# Stage changes
git add filename

# Commit with descriptive message
git commit -m "Add revenue metrics to summary function

- Calculate total revenue
- Add average order value
- Break down by category"

# Push to remote
git push origin feature/your-feature-name
```

### 3. Creating Pull Request

1. Go to GitHub repository
2. Click "Compare & pull request"
3. Fill in PR description:
   - What changed?
   - Why did it change?
   - How to test it?
4. Add reviewer
5. Create PR

### 4. Code Review

**As Reviewer:**
- Check functionality
- Verify best practices
- Test the code
- Leave constructive feedback

**As Author:**
- Address feedback
- Make requested changes
- Re-request review
- Merge when approved

### 5. After Merge
```bash
# Update your main branch
git checkout main
git pull origin main

# Delete feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

## Databricks Best Practices

### Parameterization

❌ **Bad:**
```python
data_path = "/mnt/prod-data/sales/"
analysis_date = "2024-01-01"
```

✅ **Good:**
```python
dbutils.widgets.text("environment", "dev", "Environment")
dbutils.widgets.text("analysis_date", "2024-01-01", "Analysis Date")

env = dbutils.widgets.get("environment")
date = dbutils.widgets.get("analysis_date")

data_path = f"/mnt/{env}-data/sales/"
```

### Documentation

❌ **Bad:**
```python
def calc(df):
    return df.sum()
```

✅ **Good:**
```python
def calculate_total_revenue(df: pd.DataFrame) -> float:
    """Calculate total revenue from sales data.
    
    Args:
        df: DataFrame with 'quantity' and 'price' columns
        
    Returns:
        Total revenue as float
    """
    df['revenue'] = df['quantity'] * df['price']
    return df['revenue'].sum()
```

### Project Structure

✅ **Good Organization:**
```
notebooks/     # For exploration and analysis
src/           # For reusable code
data/          # For sample data only (not large files!)
config/        # For configuration files
```

## Common Scenarios

### Merge Conflict

If you get a merge conflict:

1. Pull latest main
2. Merge main into your branch
3. Find conflict markers (<<<<<<)
4. Decide what to keep
5. Remove conflict markers
6. Test the merged code
7. Commit the resolution
8. Push

### Forgot to Create Branch
```bash
# Stash your changes
git stash

# Switch to main and create branch
git checkout main
git checkout -b feature/your-feature

# Apply your changes
git stash pop
```

### Need to Update Branch
```bash
# Get latest from main
git checkout main
git pull origin main

# Go back to your branch
git checkout feature/your-feature

# Merge or rebase
git merge main  # or git rebase main
```

## Getting Help

- Stuck on Git? Check [Git cheat sheet](../docs/git_cheatsheet.md)
- Databricks questions? See [Databricks docs](https://docs.databricks.com)
- Workshop questions? Ask instructor or TAs