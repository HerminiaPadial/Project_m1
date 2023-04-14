**Where is my bike?**

It is a pilot project that aims to allow users to find the nearest BICIMAD station to a specific place. 
In this first version, much more limited, the selected places have been the cultural centers of Madrid. It only allows the user to know the BICIMAD station closest to them, so the user will be able to know where to find the nearest BICIMAD station.

![02-bicimad-conversacion](https://user-images.githubusercontent.com/120276613/232133724-c82262c0-6c0a-4e9f-bc7e-1b549ed1e8cd.gif)

📁 **Folder structure**

💻 **Technology stack**

- DBeaver [Link]https://dbeaver.io/
- Python [Link]https://docs.python.org/3.7/l
- DuckDB [Link]
- Libreries such as:
  - Pandas [Link]https://pandas.pydata.org/
  - GeoPandas [Link]
  - Requests [Link]https://requests.readthedocs.io/en/latest/
- Argparse [Link]https://docs.python.org/3.7/library/argparse.html

**Acquisition Data**
There are 2 different datasource involved:
- DBeaver. The database contains information from the BiciMAD stations.
- API REST from the Portal de datos abiertos del Ayuntamiento de Madrid, 

⏩ **How it works**


:arrow_upper_right: **Output**
A. CSV file with all cultural centers of Madrid and the nearest BICIMAD station.
B. CSV file with the desired cultural center and the nearest BICIMAD station.

The data of the documents are:
  - Place of interest
  - Type of center
  - Address of the center
  - Name of the BICIMAD station
  - Address of BICIMAD station
  - Distance in meters
  
**Next steps**
- Expand the network of points of interest
- Optimize the operation of the script

:incoming_envelope: **Contact info**
