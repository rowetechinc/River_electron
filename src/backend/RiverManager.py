from TabularDataVM import TabularDataVM
from DataManager import DataManager
from threading import Thread
import logging


class RiverManager:
    """
    Handle all the ViewModels in the display.
    Starts the threads for each ViewModel and the thread for the ADCP.
    """

    def __init__(self):
        """
        Initialize the threads for the ViewModels and ADCP
        """
        # Start the Playback
        self.data_mgr = DataManager()
        self.data_mgr_thread = Thread(target=self.data_mgr.start, args=(4241,), name="DataManager Thread")
        self.data_mgr_thread.start()
        logging.info("Data Thread started")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    RiverManager()
