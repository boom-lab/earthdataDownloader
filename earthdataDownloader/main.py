#!/usr/bin/env python3

import earthaccess
import glob
from pathlib import Path

def update_dl_list(results_list, dl_dir):

    existing_list = glob.glob(dl_dir)

    def extract_fname(fpath):
        return fpath.rstrip('/').rsplit('/', 1)[-1]

    results_fnames = [
        extract_fname(result.data_links()[0]) for result in results_list
    ]
    existing_fnames = [
        extract_fname(existing_file) for existing_file in existing_list
    ]

    # Get files not already present in destination folder
    updated_list = [
        fpath for fname, fpath in zip(results_fnames, results_list)
        if fname not in existing_fnames
    ] 

    if len(updated_list)==0:
        return False
    else:
        return updated_list

def main():

    L3 = "AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0"
    L4 = "OSTIA-UKMO-L4-GLOB-REP-v2.0"
    bb = (27, -80, 53, -30)
    time_range = ("2020-01-01", "2020-01-03")
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
        to_download = update_dl_list(results, dl_dir)
        dl_dir = Path(dl_dir)
        print(
            f"Downloading {name} data to {dl_dir}..."
        )
        if not to_download:
            print("No new file to download, exiting...")
        else:
            files = earthaccess.download(
                to_download,
                local_path = dl_dir,
                show_progress = True
            )

        print("Done.")
        
    return

if __name__ == "__main__":
    main()
