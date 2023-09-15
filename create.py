from deltalake.writer import write_deltalake
import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'a', 'b']})

write_deltalake('./data/table1', df, name='Table 1', description='This is my first datalake table', partition_by=['y'])
