# Citibike-API-Wrapper

A library of simple functions for interaction with the Citibike API. Contains a continuously-running background process to ensure quick delivery of up-to-date data

# How to Use

Instantiate the class with:

    >>> c = CitibikeAPI(interval=15)

Call any of the functions shown below to request data:

    >>> c.systemRegions()
    >>> c.stationInformation()
    >>> c.stationStatus()
    >>> c.systemInformation()
    >>> c.systemAlerts()