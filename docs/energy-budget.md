# Energy feasibility

Assumptions (must be verified):
- One LED module: 15 W at full light, 7.5 W at half light.
- Constant-current LED driver: 88% efficiency.
- Night schedule: 2 hours full, 8 hours half.
- Battery A: 7 x 3.2 V x 6 Ah = 134.4 Wh nominal.

One light electrical LED energy: (15 W x 2 h) + (7.5 W x 8 h) = **90 Wh**.
Approximate energy before LED driver losses: 90 / 0.88 = **102.3 Wh/night per light**.
Two lights: **204.5 Wh/night**, excluding controller/DC-DC losses.

A single 134.4 Wh nominal bank cannot sustainably deliver the full two-light schedule. Even with two banks (268.8 Wh nominal), reserve capacity, converter losses, aging and low-sun days constrain runtime. A 30 W panel's daily harvested energy depends on peak-sun-hours, panel orientation, shading, temperature and charging losses; it is **not** 30 W continuously.

Requirements:
- Firmware must budget actual current/energy and protect minimum cell voltage.
- Two jacks are electrically fully functional, but both full schedules are not guaranteed.
- Do not promise 2000 lm from 15 W without an LED efficacy and thermal measurement.
