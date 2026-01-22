#!/usr/bin/env python3

import earthaccess

def main():

    # 1. Login
    earthaccess.login()

    # 2. Search
    results = earthaccess.search_data(
        short_name='ATL06',  # ATLAS/ICESat-2 L3A Land Ice Height
        bounding_box=(-10, 20, 10, 50),  # Only include files in area of interest...
        temporal=("1999-02", "2019-03"),  # ...and time period of interest.
        count=10
    )

    # 3. Access
    files = earthaccess.download(results, "/tmp/my-download-folder")
    
    return

if __name__ == "__main__":
    main()
