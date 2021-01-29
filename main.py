from pprint import pprint
import os
from collections import defaultdict
from typing import List, Dict

RESOURCE_DIR = "Resources"

	
def extract_airport_name(row: str) -> str:
	# Find where the second occurrence of the '"' is in the string (basically end of the airport name)
	quote_idx = row[::-1].find('"')
	return row[5:quote_idx*-1 - 1]


def parse_data(data_rows: List[str]) -> Dict:
	airport_dict = defaultdict(lambda: 0)
	for row in data_rows:
		airport_name = extract_airport_name(row)
		airport_dict[airport_name] += 1
	return {f"{k}": airport_dict[k] for k in sorted(airport_dict.keys(), key=lambda x: airport_dict[x], reverse=True)}


if __name__ == '__main__':
	with open(os.path.join(RESOURCE_DIR, "airlines.csv"), 'r') as f:
		header = f.readline()
		data = [i for i in f.read().split('\n') if i]
	airports = parse_data(data_rows=data)
	most_repeated, least_repeated = list(airports.keys())[::len(airports.keys())-1]
	print(f"Output 1 :")
	pprint(airports)
	print(f"Output 2: Most mentioned airport: {most_repeated} with {airports[most_repeated]}")
	print(f"Output 2: Least mentioned airport: {least_repeated} with {airports[least_repeated]}")
