from deltalake import DeltaTable

dt = DeltaTable("./data/table1")

print(dt.version())

print(dt.files())

print(dt.metadata())

print(dt.schema())

print(dt.history())

print(dt.to_pandas())
