from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

engine = create_engine('sqlite:///da1.db', echo = True)
metadata = MetaData(bind = engine)

hockey = Table('hockey', metadata,
   Column('team', String(16), primary_key = True),
   Column('jersey_colour', String(16)),
   Column('stadium', String(32)),
   Column('goals', Integer),
   Column('date', String(10), primary_key = True),
   Column('assists', Integer))

data = [
   ['Blue', 'Toronto Maple Leafs', 'Air Canada Center', '2013-03-26', 301, 151],
   ['Red', 'Calgary Flames', 'PenWest', '2013-03-27', 254, 147]
]

#metadata.create_all()
#result = engine.execute(hockey.insert().values(data))
s = hockey.select()
result = engine.connect().execute(s)
for row in result:
   print (row)