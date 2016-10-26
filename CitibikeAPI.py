# Citibike API Wrapper
# Work in Progress 10.26.16
# Jay Puntham-Baker
import requests, time, math, threading, json
from threading import Thread


class CitibikeAPI(object):
    """
    WIP: A library of functions used to interact with the Citibike API. Contains an additional
    class to initialize a background process to continuously update data.

    Initialize the class with CitibikeAPI(interval=x) and then use any of the functions found in the class
    """
    class APICaller(Thread):
        # Class defines a background process to continuously call API
        def __init__(self, URL='https://gbfs.citibikenyc.com/gbfs/en/', interval=10):
            # Initialize local class variables
            print("Gathering Initial Data . . . ")
            Thread.__init__(self)
            self.URL = URL
            self.interval = interval
            self.system_regions = {}
            self.station_information = {}
            self.station_status = {}
            self.system_information = {}
            self.system_alerts = {}
            self.t1 = time.asctime()
            self.stopped = False
            self.initialCall()

        def initialCall(self):
            # Performs initial call to the API and prevents the execution of code prior to its completion
            # Prevents a program from working with empty data dictionaries
            self.system_regions = requests.get(self.URL + 'system_regions.json').json()
            self.station_information = requests.get(self.URL + 'station_information.json').json()
            self.station_status = requests.get(self.URL + 'station_status.json').json()
            self.system_information = requests.get(self.URL + 'system_information.json').json()
            self.system_alerts = requests.get(self.URL + 'system_alerts.json').json()
            self.t1 = time.asctime()
            print('Initial Data Received: ', "|", time.asctime())

        def run(self):
            # Defines the function that continuously calls the Citibike API in N second intervals
            while True:
                self.system_regions = requests.get(self.URL + 'system_regions.json').json()
                self.station_information = requests.get(self.URL + 'station_information.json').json()
                self.station_status = requests.get(self.URL + 'station_status.json').json()
                self.system_information = requests.get(self.URL + 'system_information.json').json()
                self.system_alerts = requests.get(self.URL + 'system_alerts.json').json()
                self.t1 = time.asctime()
                print('New Data Received', "|", time.asctime())
                time.sleep(self.interval)

    def __init__(self, interval):
        # Instantiates a new instance of the Citibike class
        # Initializes the parallel / background APICaller thread once initial data received
        print("Initializing . . .")
        self.api = self.APICaller(interval=interval)
        self.api.start()

    def systemRegions(self):
        # Returns System Regions data
        return self.api.system_alerts

    def stationInformation(self):
        # Returns Station Information data
        return self.api.station_information

    def stationStatus(self):
        # Returns Station Status data
        return self.api.station_status

    def systemInformation(self):
        # Returns System Information data
        return self.api.system_information

    def systemAlerts(self):
        # Returns System Alerts data
        return self.api.system_alerts

if __name__ == "__main__":
    C1 = CitibikeAPI(interval=15)
    print(C1.systemRegions())




