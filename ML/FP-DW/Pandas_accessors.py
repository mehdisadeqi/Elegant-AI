import pandas as pd

df = pd.DataFrame({'Date': pd.date_range('2020-04-08', periods=5, freq='M'),
                   'Name': ['Mehdi-SD', 'Saeed-SD', 'Elshan-YP', 'Ariel-SB', 'Parisa-MH'],
                   'Score': pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C', 'D', 'E', 'F'], ordered=True)})

# .dt accessor examples
print(f"\n =========== .dt Accessor ========= \
        \n Date: {df['Date'].dt.date.tolist()}, \
        \n Month Name: {df['Date'].dt.month_name().tolist()}, \
        \n Day Name: {df['Date'].dt.day_name().tolist()}, \
        \n Days in month: {df['Date'].dt.days_in_month.tolist()}, \
        \n Converted to Python datetime: {df['Date'].dt.to_pydatetime().tolist()}, \
        \n Convert to monthly periods: {df['Date'].dt.to_period('M').tolist()}")

# .str accessor
print(f"\n =========== .str Accessor ========= \
        \n Upper-cased: {df['Name'].str.upper().tolist()}, \
        \n Last name extracted: {df['Name'].str.extract(r'-([A-Z]{2})')[0].tolist()}, \
        \n Convert to comma sepearted: {df['Name'].str.replace('-', ', ').tolist()}, \
        \n Number of vowels: {df['Name'].str.count(r'[aeiouAEIOU]').tolist()}, \
        \n Left justified: {df['Name'].str.ljust(width=20).tolist()}, \
        \n Leading zeros added: {df['Name'].str.zfill(width=20).tolist()}, \
        \n Trailing zeros added: {df['Name'].str.ljust(width=20, fillchar='0').tolist()}")

# .cat accessor
print(f"\n =========== .cat Accessor ========= \
        \n Codes: {df['Score'].cat.codes.tolist()}, \
        \n Categories: {df['Score'].cat.categories.tolist()}, \
        \n Are the categories ordered: {df['Score'].cat.ordered}, \
        \n Reorder categories: {df['Score'].cat.reorder_categories(['F', 'E', 'D', 'C', 'B', 'A']).cat.codes.tolist()}, \
        \n Categories: {df['Score'].cat.add_categories(['A+']).tolist()}, \
        \n Is it ordered: {df['Score'].cat.remove_unused_categories().tolist()}")
