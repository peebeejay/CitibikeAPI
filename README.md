# Citibike-API-Wrapper

A library of simple functions used to interact with the Citibike API. Contains a background process to ensure quick delivery of data

# How to Use

Instantiate the class with:

    >>> c = CitibikeAPI(interval=15)

Call any of the functions shown below to request data:

    >>> c.systemRegions()
    >>> c.stationInformation()
    >>> c.stationStatus()
    >>> c.systemInformation()
    >>> c.systemAlerts()