import pandas as pd

def validate_data(data):
    for record in data:
        for field in ['open', 'high', 'low', 'close']:
            if not isinstance(record[field], (float, int)):
                raise ValueError(f"{field} needs to be a decimal number")

        if not isinstance(record['volume'], int):
            raise ValueError("Volume needs to be an integer")

        if not isinstance(record['instrument'], str):
            raise ValueError("Instrument needs to be a string")

        if not isinstance(record['datetime'], pd.Timestamp):
            raise ValueError("Datetime needs to be a datetime")