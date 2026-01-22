#!/usr/bin/env python3

import earthaccess
import glob

products_short_names = [
    "AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0", # L3 AVHRR
    "OSTIA-UKMO-L4-GLOB-REP-v2.0"            # L4
]
bb = (27, -80, 53, -30)
time_range = ("2019-12-31", "2020-01-03")

def main():

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
