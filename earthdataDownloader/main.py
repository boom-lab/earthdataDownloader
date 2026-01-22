#!/usr/bin/env python3

import earthaccess

def main():

    L3 = "AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0"
    L4 = "OSTIA-UKMO-L4-GLOB-REP-v2.0"
    bb = (27, -80, 53, -30)
    time_range = ("2020-01-01", "2020-01-02")
    dl_folders = {}
    dl_folders[L3] = "./downloads/" + L3 + "/"
    dl_folders[L4] = "./downloads/" + L4 + "/"
    
    # 1. Login
    print("Logging in...")
    earthaccess.login()

    # 2. Search
    for name in [L3,L4]:
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
            f"Downloading {name} data to {dl_dir}..."
        )
        files = earthaccess.download(
            results,
            local_path = dl_dir,
            show_progress = True
        )
    
    return

if __name__ == "__main__":
    main()
