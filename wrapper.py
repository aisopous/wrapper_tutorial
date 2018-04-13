import json

def get_data():
    with open('data.csv', 'r') as f:
        data = f.read()
    return data

def get_all_data():
    with open('data.csv', 'r') as f:
        data = f.readlines()
    return data

def data_from_csv(raw):
    pass # returns a Data object

def data_from_query(query):
    return # returns a Data object

class Data(object):
    def __init__(self, raw):
        name, value, latitude, longitude, altitude = raw.split(',')
        self.name = name
        self.value = value
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


    def convert_back(self):
        """Converts data back to original csv format of name,value,lat,long,alt
        """
        pass


    def to_dict(self):
        return vars(self)

    def to_json(self):
        vars(self)
        return json.dumps(vars)


    def compute_distance_from(self, loc):
        return (self.longitude - loc.x)**2 + (self.latidude - loc.y)**2


"""
{
coordinates:
    {name: string},
    {value: int},
    }
"""



# print get_data()
data = Data(get_data())
print vars(data)

# print data.name, "is located at", "(", data.latitude, ",", data.longitude, ")"
print data.to_json()
