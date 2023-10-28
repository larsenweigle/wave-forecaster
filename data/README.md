# Data Repository

This repository contains both processed and raw data.

## Processed Data

- Folder: `processed`
- Description: This folder contains all the post-processed data.

## Raw Data

- Folder: `raw`
- Description: The `raw` folder contains massive raw data files, each exceeding 2 GB in size.
- `.gitignore`: A `.gitignore` file is set up to ignore changes from the `raw` data subfolder. This is done to prevent large binary files from being included in the version control history.

You may have to create these folders on local main on your own If they do not appear when cloning the project. For now the data/raw folder should only contain data text files from the historical time series datasets which you can download [here](https://www.ndbc.noaa.gov/station_history.php?station=46266).
