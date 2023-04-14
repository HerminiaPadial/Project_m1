**<h1 align="center">Where is my bike?</h1>**
===============================================

It is a pilot project that aims to allow users to find the nearest BICIMAD station to a specific place. 
In this first version, much more limited, the selected places have been the cultural centers of Madrid. It only allows the user to know the BICIMAD station closest to them, so the user will be able to know where to find the nearest BICIMAD station.
![imagen1](https://user-images.githubusercontent.com/120276613/232158034-6761cdc6-a324-4610-b74a-31faef6c5973.jpeg)

📁 **Folder structure**
-----------------------
![estructura](https://user-images.githubusercontent.com/120276613/232158905-a4b12cbe-87f9-44d0-a057-179160bf336b.png)

💻 **Technology stack**
-----------------------

- [DBeaver](https://dbeaver.io/)
- [Python](https://docs.python.org/3.7/l)
- [DuckDB](https://duckdb.org/why_duckdb.html)
Libreries such as:
  - [Pandas](https://pandas.pydata.org/)
  - [GeoPandas](https://geopandas.org/en/stable/)
  - [Requests](https://requests.readthedocs.io/en/latest/)
- [Argparse](https://docs.python.org/3.7/library/argparse.html)

**Acquisition Data**
-----------------------
There are 2 different datasource involved:
- DBeaver. The database contains information from the BiciMAD stations.
- API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/)

⏩ **How it works**
-----------------------
The main script is locally executed each time you need this information. 

You have two options:

A. Get a list of all the cultural centers in Madrid and the nearest BICIMAD station.
If you want to execute it, just write:
`python main.py --places "places"`

B. Get a document with the specific site that the user specifies and the nearest BICIMAD station. 
If you want to execute it, just write:
`python main.py --my place "place you want"`

:arrow_upper_right: **Output**
-------------------------------
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
-----------------------
- Expand the network of points of interest
- Optimize the operation of the script

:incoming_envelope: **Contact info**
-------------------------------------
If you are hiring Data Analysts I'm all you need, write me through my [Linkedin](www.linkedin.com/in/herminiapr-data-analist-product-manager)!

If you have any questions also, cantact me by that way!
