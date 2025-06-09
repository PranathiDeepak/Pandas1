import pandas as pd
list1 = [['Math', 50], ['Science',45], ['Social', 40], ['Arts', 50]]
df = pd.DataFrame(list1, columns = ['Subject', 'Marks'])
print (df)