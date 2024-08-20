# ASCE-Calculator
A calculator to automate various structural calculations

**SAMPLE OUTPUT:**

```
--------TABLE VALUES------

Aerodynamic Multiplier: 0.315
Restoring Moments due to Gravity (Mg): 7.34
Attachment Resistance Expressed as a Moment (Mf): 45.5

-------PRESSURE ZONES-----

Zone 1: -71
Zone 2e: -91
Zone 2r: -91
Zone 3: -111

-----------REPORT---------

Zone 1: (71 x 0.315 = 22.365) - 7.34 = 15.025 <= 45.5  OK
Zone 2e: (91 x 0.315 = 28.665) - 7.34 = 21.325 <= 45.5  OK
Zone 2r: (91 x 0.315 = 28.665) - 7.34 = 21.325 <= 45.5  OK
Zone 3: (111 x 0.315 = 34.965) - 7.34 = 27.625 <= 45.5  OK
```

Required Modules:
```
pip install colorama
pip install customtkinter
pip install reportlab
```

Disclaimer: Not connected/related in any way to the American Society of Civil Engineers
