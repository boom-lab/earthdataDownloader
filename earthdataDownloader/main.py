#!/usr/bin/env python3

import earthaccess

def main():

    L3 = "AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0"
    L4 = "OSTIA-UKMO-L4-GLOB-REP-v2.0"

    # 1. Login
    earthaccess.login()

    # 2. Search
    for name in [L4,L3]:
        results = earthaccess.search_data(
            short_name=name,
            bounding_box=(27, -80, 53, -30),  #(lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)
            temporal=("2020-01-01", "2020-01-31"),  #[Union[str, date, datetime]]
            count=-1 # get all
        )

        # 3. Access
        files = earthaccess.download(results, "/tmp/my-download-folder")
    
    return

if __name__ == "__main__":
    main()
