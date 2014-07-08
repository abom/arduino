nfc_rfid-monitor
================

A threaded monitor for the [NFC/RFID shield](http://store.fut-electronics.com/SLD80453P-1.html).

* Reads the passive id of [RFID cards (13.56Mhz)](http://store.fut-electronics.com/RFR104A1B.html)

Usage
=====

* First you should have:
* arduino board connected to NFC/RFID shield
* the NFC-SPI library attached is modified by commenting some lines which is writing to Serial.
* any 13.56Mhz RFID cards
* [python](https://www.python.org/download/), [pyserial](https://pypi.python.org/pypi/pyserial) and [pyqt4](http://www.riverbankcomputing.co.uk/software/pyqt/download) installed

* then just run the monitor-gui

```
python monitor-gui.py
```



