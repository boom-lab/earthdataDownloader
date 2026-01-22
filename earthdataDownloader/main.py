#!/usr/bin/env python3

import earthaccess
import glob
import json
from pathlib import Path

def main():
    # Load search parameters from JSON file
    config_path = Path(__file__).parent.parent / "search.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    products_short_names = config["products_short_names"]
    bb = tuple(config["bounding_box"])
    time_range = tuple(config["time_range"])

    dl_folders = {}
    for name in products_short_names:
        dl_folders[name] = "./downloads/" + name + "/"
    
    # 1. Login
    print("Logging in...")
    earthaccess.login()

    # 2. Search
    for name in products_short_names:
        print(
            f"Looking for {name} data in box {bb} and time range {time_range}..."
        )
        results = earthaccess.search_data(
            short_name=name,
            bounding_box=bb,  #(lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)
            temporal=time_range,  #[Union[str, date, datetime]]
            count=-1 # get all
        )

        # 3. Download
        dl_dir = dl_folders[name]
        print(
            f"Found {len(results)} files."
        )
        print(
            f"Downloading {name} data to {dl_dir}..."
        )
        files = earthaccess.download(
            results,
            local_path = dl_dir,
            show_progress = True
        )
        print("Done.")
        
    return

if __name__ == "__main__":
    main()
