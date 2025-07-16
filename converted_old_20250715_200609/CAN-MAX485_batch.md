---
# Page 1
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## General Description

The MAX481, MAX483, MAX485, MAX487–MAX491, and MAX1487 are low-power transceivers for RS-485 and RS-422 communication. Each part contains one driver and one receiver. The MAX483, MAX487, MAX488, and MAX489 feature slew-rate drivers that minimize EMI and reduce reflections caused by improperly terminated cables, thus allowing error-free data transmission up to 250kbps. The driver slew rates of the MAX481, MAX485, MAX490, MAX491, and MAX1487 are not limited, allowing them to transmit up to 2.5Mbps.

These transceivers draw between 120µA and 500µA of supply current when unloaded or fully loaded with disabled drivers. Additionally, the MAX481, MAX483, and MAX487 have a low-current shutdown mode in which they consume only 0.1µA. All parts operate from a single 5V supply.

Drivers are short-circuit current limited and are protected against excessive power dissipation by thermal shutdown circuitry that disables their outputs into a high-impedance state. The receiver input has a fail-safe feature that guarantees a logic-high output in the open circuit.

The MAX487 and MAX1487 feature quarter-unit-load receiver input impedance, allowing up to 128 MAX487/MAX1487 transceivers on the bus. Specifications are obtained using the MAX488–MAX491, while the MAX481, MAX483, MAX487, and MAX1487 are designed for half-duplex applications.

## Applications

- Low-Power RS-485 Transceivers
- Low-Power RS-422 Transceivers
- Level Translators
- Transceivers for EMI-Sensitive Applications
- Industrial-Control Local Area Networks

## Features

- In µMAX Package: Smallest 8-Pin SO
- Slew-Rate Limited for Error-Free Data Transmission (MAX483/487/488/489)
- 0.1µA Low-Current Shutdown Mode (MAX481/483/487)
- Low Quiescent Current:
  - 120µA (MAX483/487/488/489)
  - 230µA (MAX487)
  - 300µA (MAX481/485/490/491)
- -7V to +12V Common-Mode Input Voltage Range
- Three-State Outputs
- 30ns Propagation Delay, 5ns Skew (MAX481/485/490/491/1487)
- Full-Duplex and Half-Duplex Versions Available
- Operate from a Single 5V Supply
- Allows up to 128 Transceivers on the Bus (MAX487/MAX1487)
- Current-Limiting and Thermal Shutdown for Driver Overload Protection

## Ordering Information

| PART       | TEMP. RANGE   | PIN-PACKAGE   |
|------------|---------------|---------------|
| MAX481CPA  | 0°C to +70°C  | 8 Plastic DIP |
| MAX481CSA  | 0°C to +70°C  | 8 SO          |
| MAX481CUA  | 0°C to +70°C  | 8 µMAX        |
| MAX481CD   | 0°C to +70°C  | 8 DIP         |

*Ordering Information continued at end of data sheet. Contact factory for dice specifications.*

## Selection Table

| PART   | HALF/FULL DUPLEX | DATA RATE (Mbps) | SLEW-RATE LIMITED | LOW-POWER SHUTDOWN | RECEIVER/ DRIVER ENABLE | QUIESCENT CURRENT (µA) | NUMBER OF TRANSMITTERS ON BUS | PIN COUNT |
|--------|------------------|------------------|--------------------|---------------------|-------------------------|-------------------------|-------------------------------|-----------|
| MAX481 | Half             | 2.5              | No                 | Yes                 | Yes                     | 300                     | 32                            | 8         |
| MAX483 | Half             | 0.25             | Yes                | Yes                 | Yes                     | 120                     | 32                            | 8         |
| MAX485 | Half             | 2.5              | No                 | Yes                 | Yes                     | 300                     | 32                            | 8         |
| MAX487 | Half             | 0.25             | Yes                | Yes                 | Yes                     | 120                     | 32                            | 8         |
| MAX488 | Full             | 0.25             | Yes                | No                  | No                      | 120                     | 32                            | 8         |
| MAX489 | Full             | 0.25             | No                 | Yes                 | No                      | 120                     | 32                            | 8         |
| MAX490 | Full             | 2.5              | No                 | No                  | No                      | 300                     | 32                            | 8         |
| MAX491 | Full             | 2.5              | No                 | No                  | No                      | 300                     | 32                            | 14        |
| MAX1487 | Half            | 2.5              | No                 | No                  | Yes                     | 230                     | 128                           | 8         |

Maxim Integrated Products
```


---
# Page 2
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## ABSOLUTE MAXIMUM RATINGS

- **Supply Voltage (VCC)**: ................................. 12V
- **Control Input Voltage (DE, DE)**: .................. -0.5V to (VCC + 0.5V)
- **Driver Input Voltage (DI)**: ............................ -0.5V to (VCC + 0.5V)
- **Driver Output Voltage (A, B)**: ...................... -8V to +12.5V
- **Receiver Input Voltage (A, B)**: ..................... -8V to +12.5V
- **Continuous Power Dissipation (Ta = +70°C)**: ... 727mW
- **8-Pin Plastic DIP (derate 0.9mW/°C above +70°C)**: 800mW
- **14-Pin Plastic DIP (derate 10.0mW/°C above +70°C)**: 800mW
- **8-Pin SO (derate 8.8mW/°C above +70°C)**: ........ 471mW
- **14-Pin µMAX (derate 8.33mW/°C above +70°C)**: ... 667mW
- **8-Pin µMAX (derate 1.81mW/°C above +70°C)**: ...... 830mW
- **8-Pin CERDIP (derate 8.00mW/°C above +70°C)**: ... 640mW
- **14-Pin CERDIP (derate 10.0mW/°C above +70°C)**: ... 727mW
- **Operating Temperature Ranges**:
  - MAX4 _ _/MAX1487C: ................................. 0°C to +70°C
  - MAX4 _ _/MAX1487E: ................................. -40°C to +85°C
  - MAX4 _ _/MAX1487M: ................................. -55°C to +125°C
- **Storage Temperature Range**: ........................ -65°C to +160°C
- **Lead Temperature (soldering, 10sec)**: ............ +300°C

## DC ELECTRICAL CHARACTERISTICS

| PARAMETER                                   | SYMBOL | CONDITIONS                                   | MIN  | TYP | MAX  | UNITS |
|---------------------------------------------|--------|----------------------------------------------|------|-----|------|-------|
| Differential Driver Output (no load)       | VOD1   | R = 502 (RS-422)                            | 2    |     |      | V     |
| Differential Driver Output (with load)     | VOD2   | R = 272 (RS-485, Figure 4)                 | 1.5  |     |      | V     |
| Change in Magnitude of Driver               | ΔVOD   | R = 272 or 502, Figure 4                    |      |     | 0.2  | V     |
| Complementary Output States                  | VOC    | R = 272 or 502, Figure 4                    | 3    |     |      | V     |
| Input High Voltage                          | VIH    | DE, DI, RE                                  | 2.0  |     |      | V     |
| Input Low Voltage                           | VIL    | DE, DI, RE                                  | 0.8  |     |      | V     |
| Input Current                               | IIN1   | DE = 0V; VCC = 0V or 5.25V, all devices except MAX487/MAX1487 | VIN = 12V | 1.0  | mA   |
| Input Current (A, B)                       | IIN2   | DE = 0V; VCC = 0V or 5.25V, VIN = -7V, all devices except MAX487/MAX1487 | VIN = 12V | 0.25 | mA   |
| Receiver Differential Threshold Voltage      | VTH    | -7V ≤ VCM ≤ 12V                             | -0.2 |     | 0.2  | V     |
| Receiver Input Hysteresis                   | ΔVTH   | VCM = 0V                                    |      | 70  |      | mV    |
| Receiver Output High Voltage                 | VOH    | IO = -4mA, VID = -200mV                     | 3.5  |     |      | V     |
| Receiver Output Low Voltage                  | VOL    | IO = -4mA, VID = -200mV                     | 0.4  |     |      | V     |
| Three-State High Impedance Output Current   | IOZ    | 0.4V ≤ VOS ≤ 2.4V                           | ±1   |     |      | µA    |
| Receiver Input Resistance                     | RIN    | -7V ≤ VCM ≤ 12V, all devices except MAX487/MAX1487 | 12   |     |      | kΩ    |
| Receiver Input Resistance                     | RIN    | -7V ≤ VCM ≤ 12V, MAX487/MAX1487            | 48   |     |      | kΩ    |
```


---
# Page 3
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## DC ELECTRICAL CHARACTERISTICS (continued)
(V_CC = ±5%, T_A = T_MIN to T_MAX, unless otherwise noted.) (Notes 1, 2)

| PARAMETER                  | SYMBOL | CONDITIONS                                   | MIN  | TYP  | MAX  | UNITS  |
|----------------------------|--------|----------------------------------------------|------|------|------|--------|
| No-Load Supply Current      | I_CC   | MAX488/MAX489, DE, DI, RE = 0V or V_CC      | 120  | 250  |      | µA     |
|                            |        | MAX490/MAX491, DE, DI, RE = 0V or V_CC      | 300  | 500  |      | µA     |
|                            |        | MAX481/MAX485, RE = 0V or V_CC, DE = 0V     | 500  | 900  |      | µA     |
|                            |        | MAX1487, RE = 0V or V_CC, DE = 0V           | 300  | 500  |      | µA     |
|                            |        | MAX483/MAX487, RE = 0V or V_CC, DE = 5V     | 350  | 650  |      | µA     |
|                            |        | MAX487                                     | 250  | 400  |      | µA     |
|                            |        | MAX481/483/487, DE = 0V, RE = V_CC          | 120  | 250  |      | µA     |

| PARAMETER                  | SYMBOL | CONDITIONS                                   | MIN  | TYP  | MAX  | UNITS  |
|----------------------------|--------|----------------------------------------------|------|------|------|--------|
| Supply Current in Shutdown  | I_SHDN | MAX481/483/487, DE = 0V, RE = V_CC          | 0.1  |      |      | µA     |
| Driver Short-Circuit Current, Vo = High | I_OSD1 | -7V ≤ Vo ≤ +12V (Note 4)                   | 35   |      | 250  | mA     |
| Driver Short-Circuit Current, Vo = Low  | I_OSD2 | -7V ≤ Vo ≤ +12V (Note 4)                   | 35   |      | 250  | mA     |
| Receiver Short-Circuit Current | I_OSR | 0V ≤ Vo ≤ 5V                                | 7    |      | 95   | mA     |

## SWITCHING CHARACTERISTICS
(MAX481/MAX485, MAX490/MAX491, MAX1487)
(V_CC = ±5%, T_A = T_MIN to T_MAX, unless otherwise noted.) (Notes 1, 2)

| PARAMETER                  | SYMBOL | CONDITIONS                                   | MIN  | TYP  | MAX  | UNITS  |
|----------------------------|--------|----------------------------------------------|------|------|------|--------|
| Driver Input to Output     | t_PLH  | Figures 6 and 8, R_DIFF = 54Ω, CL1 = CL2 = 100pF | 10   | 30   | 60   | ns     |
| Driver Output Skew to Output| t_SKEW | Figures 6 and 8, R_DIFF = 54Ω, CL1 = CL2 = 100pF | 10   | 30   | 60   | ns     |
| Driver Rise or Fall Time   | t_r, t_f | Figures 6 and 8, R_DIFF = 54Ω, CL1 = CL2 = 100pF | 5    | 15   | 25   | ns     |
| Driver Enable to Output Low | t_ZH   | Figures 7 and 9, CL = 100pF, S1 closed     | 40   | 70   |      | ns     |
| Driver Disable Time from High | t_LZ | Figures 7 and 9, CL = 15pF, S1 closed      | 40   | 70   |      | ns     |
| Driver Disable Time from Low | t_HZ  | Figures 7 and 9, CL = 15pF, S1 closed      | 40   | 70   |      | ns     |
| Receiver Input to Output    | t_PLH, t_PHL | Figures 6 and 10, MAX481, MAX1487 | 20   | 90   | 200  | ns     |
|                            |        | MAX490/EC, MAX491/EC                       | 20   | 90   | 200  | ns     |
| t_PLH - t_PHL | Differential Receiver Skew | Figures 6 and 10, R_DIFF = 54Ω, CL1 = CL2 = 100pF | 13   |      |      | ns     |
| Receiver Enable to Output Low | t_ZL | Figures 5 and 11, CL = 15pF, S1 closed     | 20   | 50   |      | ns     |
| Receiver Enable to Output High | t_ZH | Figures 5 and 11, CL = 15pF, S2 closed     | 20   | 50   |      | ns     |
| Receiver Disable Time from High | t_HZ | Figures 5 and 11, CL = 15pF, S1 closed    | 20   | 50   |      | ns     |
| Receiver Disable Time from Low | t_LZ | Figures 5 and 11, CL = 15pF, S1 closed     | 20   | 50   |      | ns     |
| Maximum Data Rate           | f_MAX  |                                            | 2.5  |      |      | Mbps   |
| Time to Shutdown            | t_SHDN | MAX481 (Note 5)                            | 50   |      | 600  | ns     |
```


---
# Page 4
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## SWITCHING CHARACTERISTICS—MAX481/MAX485, MAX490/MAX491, MAX1487 (continued)
(V_CC = ±5V, T_A = T_MIN to T_MAX, unless otherwise noted.) (Notes 1, 2)

| PARAMETER                               | SYMBOL      | CONDITIONS                                   | MIN  | TYP  | MAX  | UNITS |
|-----------------------------------------|-------------|----------------------------------------------|------|------|------|-------|
| Driver Enable from Shutdown to Output High (MAX481) | t_ZH(SHDN)  | Figures 7 and 9, C_L = 100pF, S2 closed    | 40   | 100  |      | ns    |
| Driver Enable from Shutdown to Output Low (MAX481)  | t_ZL(SHDN)  | Figures 7 and 9, C_L = 100pF, S1 closed    | 40   | 100  |      | ns    |
| Receiver Enable from Shutdown to Output High (MAX481) | t_ZH(SHDN)  | Figures 5 and 11, C_L = 15pF, S2 closed, A - B = 2V | 300  | 1000 |      | ns    |
| Receiver Enable from Shutdown to Output Low (MAX481)  | t_ZL(SHDN)  | Figures 5 and 11, C_L = 15pF, S1 closed, B - A = 2V | 300  | 1000 |      | ns    |

## SWITCHING CHARACTERISTICS—MAX483, MAX487/MAX488/MAX489
(V_CC = ±5V, T_A = T_MIN to T_MAX, unless otherwise noted.) (Notes 1, 2)

| PARAMETER                               | SYMBOL      | CONDITIONS                                   | MIN  | TYP  | MAX  | UNITS |
|-----------------------------------------|-------------|----------------------------------------------|------|------|------|-------|
| Driver Input to Output                  | t_PH        | Figures 6 and 8, R_DIFF = 54Ω, C_L = C_L2 = 100pF | 250  | 800  | 2000 | ns    |
| Driver Output Skew to Output            | t_SKEW      | Figures 6 and 8, R_DIFF = 54Ω, C_L = C_L2 = 100pF | 100  | 800  |      | ns    |
| Driver Rise or Fall Time                | t_r         | Figures 6 and 8, R_DIFF = 54Ω, C_L = C_L2 = 100pF | 250  | 2000 |      | ns    |
| Driver Enable to Output High             | t_ZH        | Figures 7 and 9, C_L = 100pF, S2 closed    | 250  | 2000 |      | ns    |
| Driver Enable to Output Low              | t_ZL        | Figures 7 and 9, C_L = 100pF, S1 closed    | 250  | 2000 |      | ns    |
| Driver Disable Time from Shutdown        | t_Z         | Figures 7 and 9, C_L = 15pF, S1 closed     | 300  | 3000 |      | ns    |
| Driver Disable Time from Shutdown        | t_Z         | Figures 7 and 9, C_L = 15pF, S2 closed     | 300  | 3000 |      | ns    |
| Driver Input to Output                   | t_PH        | Figures 6 and 10, R_DIFF = 54Ω, C_L = C_L2 = 100pF | 250  | 2000 |      | ns    |
| t_PH + t_PL | Differential Receiver Skew | t_SKEW      | Figures 6 and 10, R_DIFF = 54Ω, C_L = C_L2 = 100pF |      |      | ns    |
| Receiver Enable to Output Low            | t_ZL        | Figures 5 and 11, C_L = 15pF, S1 closed     | 20   | 50   |      | ns    |
| Receiver Enable to Output High           | t_ZH        | Figures 5 and 11, C_L = 15pF, S2 closed     | 20   | 50   |      | ns    |
| Receiver Disable Time from Low           | t_LZ        | Figures 5 and 11, C_L = 15pF, S2 closed     | 20   | 50   |      | ns    |
| Receiver Disable Time from High          | t_HZ        | Figures 5 and 11, C_L = 15pF, S2 closed     | 20   | 50   |      | ns    |
| Maximum Data Rate                        | f_MAX       | t_PH, t_PL < 50% of data period             | 250  |      |      | kbps  |
| Time to Shutdown                         | t_SHDN      | MAX483/MAX487 (Note 5)                       | 50   | 200  | 600  | ns    |
| Driver Enable from Shutdown to Output High | t_ZH(SHDN) | MAX483/MAX487, Figures 7 and 9, C_L = 100pF, S2 closed | 2000 |      |      | ns    |
| Driver Enable from Shutdown to Output Low  | t_ZL(SHDN) | MAX483/MAX487, Figures 7 and 9, C_L = 100pF, S1 closed | 2000 |      |      | ns    |
| Driver Shutdown to Output High           | t_ZH(SHDN)  | MAX483/MAX487, Figures 5 and 11, C_L = 15pF, S2 closed | 2500 |      |      | ns    |
| Driver Shutdown to Output Low            | t_ZL(SHDN)  | MAX483/MAX487, Figures 5 and 11, C_L = 15pF, S1 closed | 2500 |      |      | ns    |
```


---
# Page 5
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## NOTES FOR ELECTRICAL/SWITCHING CHARACTERISTICS

- **Note 1:** All currents into device pins are positive; all currents out of device pins are negative. All voltages are referenced to device ground unless otherwise specified.
- **Note 2:** All typical specifications are given for \( V_{CC} = 5 \, V \) and \( T_A = +25^\circ C \).
- **Note 3:** Supply current specification is valid for loaded transmitters when \( DE = 0 \, V \).
- **Note 4:** Applies to peak current. See **Typical Operating Characteristics**.
- **Note 5:** The MAX481/MAX483/MAX487 are put into shutdown by bringing \( RE \) high and \( DE \) low. If the inputs are in this state for less than 50 ns, the parts are guaranteed not to enter shutdown. If the inputs are in this state for at least 600 ns, the parts are guaranteed to have entered shutdown. See **Low-Power Shutdown Mode** section.

## Typical Operating Characteristics

### Receiver Output Low Voltage vs. Output Low Voltage

- **Conditions:** \( V_{CC} = 5 \, V, T_A = +25^\circ C \)

| OUTPUT LOW VOLTAGE (V) | OUTPUT CURRENT (mA) |
|-------------------------|---------------------|
| 0.0                     | 0                   |
| 0.5                     | 5                   |
| 1.0                     | 20                  |
| 1.5                     | 25                  |
| 2.0                     | 30                  |
| 2.5                     | 45                  |

### Output Current vs. Output High Voltage

| OUTPUT HIGH VOLTAGE (V) | OUTPUT CURRENT (mA) |
|--------------------------|---------------------|
| 1.5                      | -16                 |
| 2.0                      | -18                 |
| 2.5                      | -14                 |
| 3.0                      | -12                 |
| 3.5                      | -8                  |
| 4.0                      | -6                  |
| 4.5                      | -4                  |
| 5.0                      | -2                  |

### Receiver Output Low Voltage vs. Temperature

| TEMPERATURE (°C) | OUTPUT LOW VOLTAGE (V) |
|-------------------|-------------------------|
| -50               | 0.1                     |
| 0                 | 0.3                     |
| 25                | 0.5                     |
| 75                | 0.7                     |
| 125               | 0.9                     |

### Driver Output Current vs. Differential Output Voltage

| DIFFERENTIAL OUTPUT VOLTAGE (V) | OUTPUT CURRENT (mA) |
|-----------------------------------|---------------------|
| 0.0                               | 0                   |
| 0.5                               | 10                  |
| 1.0                               | 30                  |
| 1.5                               | 60                  |
| 2.0                               | 80                  |
| 2.5                               | 90                  |
| 3.0                               | 70                  |
| 3.5                               | 40                  |
| 4.0                               | 20                  |

### Driver Differential Output Voltage vs. Temperature

| TEMPERATURE (°C) | DIFFERENTIAL OUTPUT VOLTAGE (V) |
|-------------------|----------------------------------|
| -50               | 1.5                              |
| 0                 | 1.7                              |
| 25                | 1.9                              |
| 75                | 2.1                              |
| 125               | 2.4                              |

**Note:** \( I_{RO} = 8 \, mA \) and \( R = 54 \, \Omega \).
```

---
# Page 6
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

**(Vcc = 5V, TA = +25°C, unless otherwise noted.)**

## Typical Operating Characteristics (continued)

### OUTPUT CURRENT vs. DRIVER OUTPUT LOW VOLTAGE

- **X-axis:** OUTPUT LOW VOLTAGE (V)
- **Y-axis:** OUTPUT CURRENT (mA)

The graph shows the relationship between the driver output low voltage and the output current, indicating how the output current varies with changes in the low voltage level.

### OUTPUT CURRENT vs. DRIVER OUTPUT HIGH VOLTAGE

- **X-axis:** OUTPUT HIGH VOLTAGE (V)
- **Y-axis:** OUTPUT CURRENT (mA)

This graph illustrates the output current as a function of the driver output high voltage, demonstrating the current behavior at different high voltage levels.

### MAX481/MAX485/MAX490/MAX491 SUPPLY CURRENT vs. TEMPERATURE

- **X-axis:** TEMPERATURE (°C)
- **Y-axis:** SUPPLY CURRENT (µA)

The supply current for the MAX481, MAX485, MAX490, and MAX491 transceivers is plotted against temperature, showing how supply current changes with temperature variations.

- **Specifications:**
  - MAX481: DE = 0, RE = X
  - MAX485: DE = 0, RE = X
  - MAX490: DE = 0, RE = X
  - MAX491: DE = 0, RE = X

### MAX1487 SUPPLY CURRENT vs. TEMPERATURE

- **X-axis:** TEMPERATURE (°C)
- **Y-axis:** SUPPLY CURRENT (µA)

This graph depicts the supply current for the MAX1487 transceiver as a function of temperature.

- **Specifications:**
  - MAX1487: DE = 0, RE = X

### MAX483/MAX487/MAX489 SUPPLY CURRENT vs. TEMPERATURE

- **X-axis:** TEMPERATURE (°C)
- **Y-axis:** SUPPLY CURRENT (µA)

The supply current for the MAX483, MAX487, and MAX489 transceivers is shown against temperature, indicating the current behavior across a temperature range.

- **Specifications:**
  - MAX487: DE = Vcc, RE = X
  - MAX483/MAX487: DE = RE = 0
  - MAX483/MAX487: DE = 0, RE = Vcc
```


---
# Page 7
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Pin Description

| PIN                          | MAX481/MAX483/MAX485/MAX487/MAX1487 | MAX488/MAX490 | MAX489/MAX491 | NAME | FUNCTION                                                                                     |
|------------------------------|--------------------------------------|---------------|---------------|------|----------------------------------------------------------------------------------------------|
| DIP/SO                       | jMAX  | DIP/SO | jMAX | DIP/SO |                                                                                              |
| 1                            | 3     | 2     | 4     | 2     | RO   | Receiver Output: If A > B by 200mV, RO will be high; If A < B by 200mV, RO will be low.     |
| 2                            | 4     | —     | 3     | —     | RÉ   | Receiver Output Enable. RÉ is enabled when RÉ is low; RO is high impedance when RÉ is high. |
| 3                            | 5     | —     | —     | 4     | DE   | Driver Output Enable. The driver outputs, Y and Z, are enabled by bringing DE high. If the driver outputs are enabled, the parts function as line drivers. While they are high impedance, they function as line receivers if RÉ is low. |
| 4                            | 6     | 3     | 5     | 5     | DI   | Driver Input. A low on DI forces output Y low and output Z high. Similarly, a high on DI forces output Y high and output Z low. |
| 5                            | 7     | 4     | 6     | 6     | GND  | Ground                                                                                       |
| —                            | —     | 5     | 7     | 9     | Y    | Noninverting Driver Output                                                                    |
| —                            | —     | 6     | 8     | 10    | Z    | Inverting Driver Output                                                                       |
| 6                            | 8     | —     | —     | A     | Noninverting Receiver Input and Noninverting Driver Output                                   |
| —                            | 8     | 2     | 12    | A     | Noninverting Receiver Input                                                                    |
| 7                            | 1     | —     | —     | B     | Inverting Receiver Input and Inverting Driver Output                                          |
| 8                            | 2     | 1     | 3     | 14    | Vcc  | Positive Supply: 4.75V ≤ Vcc ≤ 5.25V                                                        |
| —                            | —     | —     | 1, 8, 13 | N.C. | No Connect—not internally connected                                                           |

### Note
PIN LABELS Y AND Z ON TIMING, TEST, AND WAVEFORM DIAGRAMS REFER TO PINS A AND B WHEN DE IS HIGH. TYPICAL OPERATING CIRCUIT SHOWN WITH DIP/SO PACKAGE.

## Figure 1
MAX481/MAX483/MAX485/MAX487/MAX1487 Pin Configuration and Typical Operating Circuit
```


---
# Page 8
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Pin Configuration and Typical Operating Circuit

### MAX488/MAX490

```
TOP VIEW
       VCC  1
        R   8
        A   2
        DI  3
       GND  4
        B   6
        Z   5
        Y   7
       RO   4
```

### MAX487/MAX491/MAX1487

```
TOP VIEW
       DE   4
       VCC  14
       RE   3
       DI   5
       Z    10
       Y    9
       RO   12
       R    2
       B    1
       A    6
       GND  7
```

**Note:** Typical operating circuit shown with DIP/SO package.

## Applications Information

The MAX481/MAX483/MAX485/MAX487/MAX491 and MAX1487 are low-power transceivers for RS-485 and RS-422 communications. The MAX481, MAX485, MAX490, MAX491, and MAX1487 can transmit and receive at data rates up to 2.5Mbps, while the MAX483, MAX487, MAX488, and MAX491 are specified for data rates up to 250kbps. The MAX488/MAX491 are full-duplex transceivers while the MAX481, MAX483, MAX485, MAX487, and MAX1487 are half-duplex. In addition, Driver Enable (DE) and Receiver Enable (RE) pins are included on the MAX481, MAX483, MAX485, MAX487, MAX489, and MAX1487. When disabled, the driver and receiver outputs are high impedance.

## MAX487/MAX1487: 128 Transceivers on the Bus

The 48kΩ, 1/4-unit-load receiver input impedance of the MAX487 and MAX1487 allows up to 128 transceivers on a bus, compared to the 1-unit load (12kΩ input impedance) of standard RS-485 drivers (32 transceivers maximum). Any combination of MAX487/MAX1487 and other RS-485 transceivers with a total of 32 unit loads or less can be put on the bus. The MAX481/MAX483/MAX485 and MAX488/MAX491 have standard 12kΩ Receiver Input impedance.
```

---
# Page 9
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Test Circuits

### Figure 4. Driver DC Test Load
```
```
Y ---- R ---- Vcc
          |
          Rv
          |
          Z
```

### Figure 5. Receiver Timing Test Load
```
          +--------+
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |
          |        |


---
# Page 10
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Switching Waveforms

### Figure 8. Driver Propagation Delays
```
- **DI**: Data Input
- **VO**: Output Voltage
- **tPHL**: Propagation Delay Time, High to Low
- **tPLH**: Propagation Delay Time, Low to High
- **Z**: High Impedance State
- **VODFF**: Differential Output Voltage
- **VODFF = V(Y) - V(Z)**

### Figure 9. Driver Enable and Disable Times (except MAX488 and MAX490)
```
- **DE**: Driver Enable
- **tZ(SHDN)**: Time from Shutdown to Output Enable
- **tZ**: Output Enable Time
- **VOH**: Output High Voltage
- **VOL**: Output Low Voltage

### Figure 10. Receiver Propagation Delays
```
- **RE**: Receiver Enable
- **RO**: Output Resistance
- **tPHL**: Propagation Delay Time, High to Low
- **tPLH**: Propagation Delay Time, Low to High

### Figure 11. Receiver Enable and Disable Times (except MAX488 and MAX490)
```
- **VCC**: Supply Voltage
- **tZ(SHDN)**: Time from Shutdown to Output Enable
- **RO**: Output Resistance

## Function Tables (MAX481/MAX483/MAX485/MAX487/MAX1487)

### Table 1. Transmitting

| RE | DE | DI | Z | Y |
|----|----|----|---|---|
| X  | 1  | 1  | 0 | 1 |
| X  | 1  | 0  | 1 | 0 |
| 0  | 0  | X  | High-Z | High-Z |
| 1  | 0  | X  | High-Z | High-Z |

* X = Don’t care  
* High-Z = High impedance  
* Shutdown mode for MAX481/MAX483/MAX487  

### Table 2. Receiving

| RE | DE | A-B | RO |
|----|----|-----|----|
| 0  | 0  | ≥ 0.2V | 1 |
| 0  | 0  | ≤ -0.2V | 0 |
| 1  | 0  | X | High-Z |

* X = Don’t care  
* High-Z = High impedance  
* Shutdown mode for MAX481/MAX483/MAX487  
```


---
# Page 11
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Low-Power Shutdown Mode (MAX481/MAX483/MAX487)

A low-power shutdown mode is initiated by bringing both RE high and DE low. The devices will not shut down unless both the driver and receiver are disabled. In shutdown, the devices typically draw only 0.1µA of supply current.

RE and DE may be driven simultaneously; the parts are guaranteed not to enter shutdown if RE is high and DE is low for at least 600ns. The parts are guaranteed to enter shutdown.

For the MAX481, MAX483, and MAX487, the tZH and tZL enable times assume the part was not in the low-power shutdown state (the MAX485/MAX488/MAX491 and MAX1487 can not be shut down). The tZH(SHDN) and tZL(SHDN) enable times assume the parts were shut down (see Electrical Characteristics).

It takes the drivers and receivers longer to become enabled from the low-power shutdown state (tZH(SHDN), tZL(SHDN)) than from the operating mode (IZH, tZL). (The parts are in operating mode if the RE, DE inputs equal a logical 0 or 1, or 1, or 0.)

## Driver Output Protection

Excessive output current and power dissipation caused by faults or by bus contention are prevented by two mechanisms. A foldback current limit on the output stage provides immediate protection against short circuits over the whole common-mode voltage range (see Typical Operating Characteristics). In addition, a thermal shutdown circuit forces the driver outputs into a high-impedance state if the die temperature rises excessively.

## Propagation Delay

Many digital encoding schemes depend on the difference between the driver and receiver propagation delay times. Typical propagation delays are shown in Figures 15–18 using Figure 14's test circuit.

The difference in receiver delay times, tPHL + tPLH, is typically under 13ns for the MAX481, MAX485, MAX490, MAX491, and MAX1487 and is typically less than 100ns for the MAX483 and MAX487–MAX489.

The driver skew times are typically 5ns (10ns max) for the MAX481, MAX485, MAX490, MAX491, and MAX1487, and are typically 100ns (800ns max) for the MAX483 and MAX487–MAX489.
```


---
# Page 12
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Receiver Propagation Delay Test Circuit

The following circuit diagram illustrates the receiver propagation delay test circuit:

```
          +---[100pF]---+
          |             |
          |             |
        [D]           [B]
          |             |
          |             |
        [Y]---[R=54Ω]---[A]
          |             |
          |             |
          +---[100pF]---+
```

### Figures

#### Figure 15: MAX481/MAX485/MAX490/MAX491/MAX1487 Receiver tPHL

- **Vertical Scale**: 500 mV/div
- **Horizontal Scale**: 20 ns/div
- **Conditions**: VCC = 5V, TA = 25°C

#### Figure 16: MAX481/MAX485/MAX490/MAX491/MAX1487 Receiver tPLH

- **Vertical Scale**: 500 mV/div
- **Horizontal Scale**: 20 ns/div
- **Conditions**: VCC = 5V, TA = 25°C

#### Figure 17: MAX483, MAX487–MAX489 Receiver tPHL

- **Vertical Scale**: 500 mV/div
- **Horizontal Scale**: 400 ms/div
- **Conditions**: VCC = 5V, TA = 25°C

#### Figure 18: MAX483, MAX487–MAX489 Receiver tPLH

- **Vertical Scale**: 500 mV/div
- **Horizontal Scale**: 400 ms/div
- **Conditions**: VCC = 5V, TA = 25°C
```


---
# Page 13
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Line Length vs. Data Rate
The RS-485/RS-422 standard covers line lengths up to 4000 feet. For line lengths greater than 4000 feet, see Figure 23.

Figures 19 and 20 show the system differential voltage for the parts driving 4000 feet of 26AWG twisted-pair wire at 110kHz into 120Ω loads.

## Typical Applications
The MAX481, MAX483, MAX485, MAX487–MAX491, and MAX1487 transceivers are designed for bidirectional data communications on multipoint bus transmission lines.

Figures 21 and 22 show typical network applications circuits. These parts can also be used as line repeaters, with cable lengths longer than 4000 feet, as shown in Figure 23.

To minimize reflections, the line should be terminated at both ends in its characteristic impedance, and stub lengths of the main line should be kept as short as possible. The slew-rate-limited MAX483 and MAX487–MAX489 are more tolerant of imperfect termination.

### Figures
- **Figure 19**: MAX481/MAX485/MAX490/MAX491/MAX1487 System Differential Voltage at 110kHz Driving 4000ft of Cable
- **Figure 20**: MAX483, MAX487–MAX489 System Differential Voltage at 110kHz Driving 4000ft of Cable
- **Figure 21**: MAX481/MAX483/MAX485/MAX487/MAX1487 Typical Half-Duplex RS-485 Network

```


---
# Page 14
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Figure 22. MAX488–MAX491 Full-Duplex RS-485 Network

```
[Diagram description: The diagram illustrates a full-duplex RS-485 network using MAX488 and MAX491 transceivers. It shows connections between the transceivers with labeled pins such as A, B, RO, RE, DE, DI, and Y. Resistors of 120Ω are depicted in the circuit.]
```

**Note:** RE and DE on MAX489/MAX491 only.

## Figure 23. Line Repeater for MAX488–MAX491

```
[Diagram description: This diagram depicts a line repeater configuration for the MAX488 and MAX491 transceivers. It includes labeled pins such as R, DE, DI, and data flow from DATA IN to DATA OUT, with a 120Ω resistor shown in the circuit.]
```

**Note:** RE and DE on MAX489/MAX491 only.

## Isolated RS-485

For isolated RS-485 applications, see the MAX253 and MAX1480 data sheets.
```


---
# Page 15
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Ordering Information (continued)

### Part List

| PART      | TEMP. RANGE   | PIN-PACKAGE  |
|-----------|---------------|--------------|
| MAX481EPA | -40°C to +85°C | 8 Plastic DIP |
| MAX4185A  | -40°C to +85°C | 8 SO         |
| MAX481MJA | -55°C to +125°C| 8 CERDIP     |
| MAX483CPA | 0°C to +70°C  | 8 SO         |
| MAX483CSA | 0°C to +70°C  | 8 µMAX       |
| MAX483C/D | 0°C to +70°C  | Dice*        |
| MAX483EA  | -40°C to +85°C | 8 Plastic DIP |
| MAX483EB  | -40°C to +85°C | 8 SO         |
| MAX483E/D | 0°C to +70°C  | Dice*        |
| MAX485MJA | -55°C to +125°C| 8 CERDIP     |
| MAX485CPA | 0°C to +70°C  | 8 Plastic DIP |
| MAX485CSA | 0°C to +70°C  | 8 SO         |
| MAX485C/D | -40°C to +85°C | Dice*        |
| MAX485E    | -40°C to +85°C | 8 SO         |
| MAX485MJD | -55°C to +125°C| 8 CERDIP     |
| MAX487CPA | 0°C to +70°C  | 8 Plastic DIP |
| MAX487CSA | 0°C to +70°C  | 8 SO         |
| MAX487CUA | 0°C to +70°C  | 8 µMAX       |
| MAX487C/D | 0°C to +70°C  | Dice*        |
| MAX487PA  | -40°C to +85°C | 8 Plastic DIP |
| MAX487ESA | -40°C to +85°C | 8 SO         |
| MAX487MJA | -55°C to +125°C| 8 CERDIP     |
| MAX488CPA | 0°C to +70°C  | 8 Plastic DIP |
| MAX488CSA | 0°C to +70°C  | 8 SO         |
| MAX488C/D | 0°C to +70°C  | Dice*        |
| MAX488EA  | -40°C to +85°C | 8 Plastic DIP |
| MAX488ESA | -40°C to +85°C | 8 SO         |
| MAX488MJA | -55°C to +125°C| 8 CERDIP     |
| MAX489CPD | 0°C to +70°C  | 14 Plastic DIP|
| MAX489CSD | 0°C to +70°C  | 14 SO        |
| MAX489C/D | 0°C to +70°C  | Dice*        |
| MAX489E   | -40°C to +85°C | 14 Plastic DIP|
| MAX489ESD | -40°C to +85°C | 14 SO        |
| MAX489MJD | -55°C to +125°C| 14 CERDIP    |

* Contact factory for dice specifications.

## Chip Topographies

### MAX481/MAX483/MAX485/MAX487/MAX491/MAX1487

- **VCC**
- **RO**
- **RE**
- **DE**
- **DI**
- **GND**

Dimensions:
- A: 0.054" (1.372mm)
- B: 0.080" (2.032mm)
```


---
# Page 16
---

```markdown
# Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers

## Chip Topographies

### MAX488/MAX490
- **VCC**
- **RO**
- **N.C.**
- **DI**
- **GND**
- **A**
- **B**
- **Z** (0.054" / 1.372mm)
- **Y**
- **N.C.**
- **Transistor Count:** 248
- **Substrate Connected to GND**
- **Dimensions:**
  - **0.080" / 2.032mm**

### MAX489/MAX491
- **VCC**
- **RO**
- **RE**
- **DE**
- **DI**
- **GND**
- **A**
- **B**
- **Z** (0.054" / 1.372mm)
- **Y**
- **Dimensions:**
  - **0.080" / 2.032mm**

## Package Information

### 8-PIN µMAX MICROMAX SMALL-OUTLINE PACKAGE

| DIM | INCHES | MILLIMETERS |
|-----|--------|-------------|
| A   | MIN: 0.036 | MAX: 0.044 | MIN: 0.91 | MAX: 1.11 |
| A1  | MIN: 0.004 | MAX: 0.008 | MIN: 0.10 | MAX: 0.20 |
| B   | MIN: 0.010 | MAX: 0.014 | MIN: 0.25 | MAX: 0.36 |
| C   | MIN: 0.005 | MAX: 0.007 | MIN: 0.13 | MAX: 0.18 |
| D   | MIN: 0.116 | MAX: 0.120 | MIN: 2.95 | MAX: 3.05 |
| E   | MIN: 0.116 | MAX: 0.120 | MIN: 2.95 | MAX: 3.05 |
| L   | MIN: 0.0256 | MAX: 0.026 | MIN: 0.65 | MAX: 0.66 |
| H   | MIN: 0.188 | MAX: 0.198 | MIN: 4.78 | MAX: 5.03 |
| α   | 0° | 6° | 0° | 6° |

**Note:** Maxim cannot assume responsibility for use of any circuitry other than circuitry entirely embodied in a Maxim product. No circuit patent licenses are implied. Maxim reserves the right to change the circuitry and specifications without notice at any time.

---

Maxim Integrated Products, 120 San Gabriel Drive, Sunnyvale, CA 94068 (408) 737-7600  
© 1996 Maxim Integrated Products  
MAXIM is a registered trademark of Maxim Integrated Products.
```

---

## Processing Metadata

- **Document:** CAN-MAX485
- **Total Pages:** 16
- **Processing Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Batch ID:** batch_6876e59c6e908190b68f3f13dda5e3e1
- **Processed:** 2025-07-15 20:02:23

### 📊 Processing Statistics

- **Total Tokens Used:** 424,809
- **Prompt Tokens:** 409,824
- **Completion Tokens:** 14,985
- **Total Processing Cost:** $0.0705
- **Average Tokens per Page:** 26551
- **Average Cost per Page:** $0.0044

### 💰 Cost Breakdown

- **Input Processing:** $0.0615 (vision + text)
- **Output Generation:** $0.0090 (markdown text)
- **Batch API Discount:** 50% off regular pricing
- **Estimated Regular Cost:** $0.1409

### ⚡ Efficiency Metrics

- **Tokens per Dollar:** 6028687
- **Pages per Dollar:** 227.1
- **Processing Method:** Batch API (cost-optimized)
