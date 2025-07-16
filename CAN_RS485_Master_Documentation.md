# CAN-RS485 Documentation Master Collection
Generated: 2025-07-15 19:52:20
Total Documents: 7

## Table of Contents
1. [Can Max485](#can-max485)
2. [Can Rs485 Can Hat B Schematic](#can-rs485-can-hat-b-schematic)
3. [Can Rs485 Can Hat User Manual En](#can-rs485-can-hat-user-manual-en)
4. [Can Rs485 Can Shield Schematic](#can-rs485-can-shield-schematic)
5. [Can Rs485 Can Shield User Manual](#can-rs485-can-shield-user-manual)
6. [Can Sn65Hvd230](#can-sn65hvd230)
7. [Can Sp3481 Sp3485](#can-sp3481_sp3485)

---

# Can Max485 {#can-max485}

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



---

# Can Rs485 Can Hat B Schematic {#can-rs485-can-hat-b-schematic}

---
# Page 1
---

```markdown
# Circuit Diagram Overview

## Power Supply Sections

### Power 5V
- **Description**: Provides a 5V power supply.
- **Components**: 
  - Voltage regulator
  - Capacitors
  - Resistors

### Power 3V3
- **Description**: Provides a 3.3V power supply.
- **Components**: 
  - Voltage regulator
  - Capacitors
  - Resistors

### Power 3V3B
- **Description**: Additional 3.3V power supply.
- **Components**: 
  - Voltage regulator
  - Capacitors
  - Resistors

### Power Isolator
- **Description**: Isolates power supply to prevent interference.
- **Components**: 
  - Isolation components
  - Capacitors

## Raspberry Pi Interface
- **Description**: Interface for connecting to Raspberry Pi.
- **Pin Configuration**:
  - Pin 1: [Function]
  - Pin 2: [Function]
  - Pin 3: [Function]
  - Pin 4: [Function]
  - Pin 5: [Function]
  - Pin 6: [Function]
  - Pin 7: [Function]
  - Pin 8: [Function]
  - Pin 9: [Function]
  - Pin 10: [Function]

## Communication Interfaces

### RS485 Transceiver
- **Description**: Facilitates RS485 communication.
- **Channels**:
  - **RS485 Channel 1**
    - Components: Transceiver, resistors, capacitors
  - **RS485 Channel 2**
    - Components: Transceiver, resistors, capacitors

### CAN Transceiver
- **Description**: Facilitates CAN communication.
- **Components**: 
  - Transceiver
  - Resistors
  - Capacitors

## Controllers

### CAN Controller
- **Description**: Manages CAN communication.
- **Components**: 
  - Microcontroller
  - Resistors
  - Capacitors

### RS485 Controller
- **Description**: Manages RS485 communication.
- **Components**: 
  - Microcontroller
  - Resistors
  - Capacitors

## Additional Components

### Mode Switch
- **Description**: Switch to change operational modes.
- **Components**: 
  - Switch
  - Resistors

### Serial Expansion
- **Description**: Allows for serial communication expansion.
- **Components**: 
  - Connectors
  - Resistors

### Digital Isolator
- **Description**: Provides digital signal isolation.
- **Components**: 
  - Isolation components
  - Capacitors

## Summary
This document outlines the schematic design for a circuit involving power supplies, communication interfaces, and controllers, specifically tailored for integration with a Raspberry Pi and supporting RS485 and CAN communication protocols.
```

---



---

# Can Rs485 Can Hat User Manual En {#can-rs485-can-hat-user-manual-en}

---
# Page 1
---

```markdown
# RS485 CAN HAT User Manual

## OVERVIEW

The RS485 CAN HAT will enable your Pi to communicate with other devices stably in long-distance via RS485/CAN functions.

## FEATURES

- **Raspberry Pi connectivity**: Compatible with Raspberry Pi Zero/Zero W/Zero WH/2B/3B/3B+
- **CAN function**: Onboard CAN controller MCP2515 via SPI interface, with transceiver SN65HVD230
- **RS485 function**: Controlled via UART, half-duplex communication, with transceiver SP3485
- **Reserved control pins**: Allows working with other control boards
- **Development resources**: Comes with development resources and manual (examples in wiringPi/python)

## SPECIFICATIONS

- **Operating voltage**: 3.3V
- **CAN controller**: MCP2515
```

---
# Page 2
---

```markdown
# RS485 CAN HAT

## Specifications

- **CAN transceiver**: SN65HVD230
- **485 transceiver**: SP3485
- **Dimension**: 65mm x 30mm
- **Mounting hole size**: 3.0mm

## Interfaces

### CAN:

| PIN | Raspberry Pi | Description               |
|-----|--------------|---------------------------|
| 3V3 | 3V3         | 3.3V Power                |
| GND | GND         | Ground                    |
| SCK | SCK         | SPI Clock                 |
| MOSI| MOSI        | SPI Data input            |
| MISO| MISO        | SPI Data output           |
| CS  | CE0         | Data/Command selection     |
| INT | PIN22 /GPIO.6/P25 | Interrupt            |

### RS485:

| PIN | Raspberry Pi | Description               |
|-----|--------------|---------------------------|
| 3V3 | 3V3         | 3.3V power                |
| GND | GND         | Ground                    |
| RXD | RXD         | RS485 UART receive        |
| TXD | TXD         | RS485 UART transmit       |
| RSE | PIN7/GPIO.7/P4 | RS485 RX/TX setting     |

**Note**: RSE pin could not be used because the module is set to auto receiver and transmit in hardware by default.
```

---
# Page 3
---

```markdown
# RS485 CAN HAT

## CONTENT

1. [Overview](#overview) .................................................................................................................. 1  
   1.1 [Features](#features) ............................................................................................................... 1  
   1.2 [Specifications](#specifications) ............................................................................................ 1  
   1.3 [Interfaces](#interfaces) .......................................................................................................... 2  
2. [Hardware Description](#hardware-description) ........................................................................ 5  
   2.1 [CAN BUS](#can-bus) ............................................................................................................... 5  
   2.2 [RS485 BUS](#rs485-bus) ......................................................................................................... 6  
3. [How to use](#how-to-use) ........................................................................................................... 9  
   3.1 [Libraries installation](#libraries-installation) ....................................................................... 9  
   3.2 [CAN test](#can-test) .............................................................................................................. 10  
       3.2.1 [Hardware](#hardware) .................................................................................................... 10  
       3.2.2 [Preparation](#preparation) ............................................................................................. 10  
       3.2.3 [C code example](#c-code-example) .............................................................................. 11  
       3.2.4 [Python example](#python-example) .............................................................................. 12  
4. [RS485 Test](#rs485-test) ........................................................................................................... 13  
   4.1 [Hardware](#hardware-1) ......................................................................................................... 13  
```


---
# Page 4
---

```markdown
# RS485 CAN HAT

## Table of Contents

- Preparation ................................................................................................................. 13
- Python code ................................................................................................................ 16
- Code Analysis ............................................................................................................. 17
- CAN .................................................................................................................................. 17
  - C code ..................................................................................................................... 17
  - Python ..................................................................................................................... 20
- RS485 .......................................................................................................................... 22
  - wiringPi code .......................................................................................................... 22
  - Python code ............................................................................................................. 24
```

### Preparation
- Content related to preparation will be detailed here.

### Python code
- Python code examples will be provided here.

### Code Analysis
- Detailed analysis of the code will be discussed here.

### CAN
- Overview of CAN communication.

#### C code
- C code examples will be provided here.

#### Python
- Python code examples for CAN will be provided here.

### RS485
- Overview of RS485 communication.

#### wiringPi code
- wiringPi code examples will be provided here.

#### Python code
- Python code examples for RS485 will be provided here.
```

---
# Page 5
---

```markdown
# RS485 CAN HAT

## Hardware Description

### CAN Bus

The CAN module can process packets for transmission and reception on the CAN bus. Packets are transmitted by first storing the packet in the related buffer and control register. The SPI interface is used to set the bits on the control register or enable the transmit pin for transmission. Registers can be read to detect communication states and errors. The module first checks for any errors in packets detected on the CAN bus, verifies them with a user-defined filter, and stores the packet in one of the buffers if there are no errors.

Raspberry Pi cannot support the SPI bus, so this module uses the SPI interface and includes a receiver/transmitter for CAN communication.

Microchip Technology's MCP2515 is a stand-alone Controller Area Network (CAN) controller that implements the CAN specification, version 2.0B. It is capable of transmitting and receiving both standard and extended data and remote frames. The MCP2515 has two acceptance masks and six acceptance filters that are used to filter out unwanted messages, thereby reducing the overhead on host MCUs. The MCP2515 interfaces with microcontrollers (MCUs) via an industry-standard Serial Peripheral Interface (SPI), which is compatible with Raspberry Pi.

### MCP2515 Pinout

| Pin Number | Pin Name   | Description                          |
|------------|------------|--------------------------------------|
| 1          | TXCAN      | Transmit CAN data                    |
| 2          | RXCAN      | Receive CAN data                     |
| 3          | CLKOUT/SOF | Clock output or Start of Frame      |
| 4          | TXRTS      | Transmit Request to Send             |
| 5          | TX1RTS     | Transmit Request to Send for channel 1 |
| 6          | TX2RTS     | Transmit Request to Send for channel 2 |
| 7          | OSC2       | Oscillator pin 2                     |
| 8          | OSC1       | Oscillator pin 1                     |
| 9          | Vss        | Ground                               |
| 10         | VDD        | Supply Voltage                       |
| 11         | NC         | No Connection                        |
| 12         | SCK        | Serial Clock Input                   |
| 13         | INT        | Interrupt Output                     |
| 14         | RX0BF      | Receive Buffer 0 Flag                |
| 15         | RX1BF      | Receive Buffer 1 Flag                |
| 16         | CS         | Chip Select                          |
| 17         | RESET      | Reset pin                            |
| 18         | VDD        | Supply Voltage                       |
| 19         | RX0BF      | Receive Buffer 0 Flag                |
| 20         | RX1BF      | Receive Buffer 1 Flag                |

```


---
# Page 6
---

```markdown
# RS485 CAN HAT

The RS485 CAN HAT allows communication with MCP2515 via SPI interface without an external driver. What we need to do is enable the kernel driver on the device tree.

For more details, please refer to the datasheet.

## SN65HVD230 Overview

SN65HVD230 from Texas Instruments is a CAN transceiver designed for high communication frequency, anti-jamming, and high reliability CAN bus communication. 

### Modes of Operation

SN65HVD230 provides three different modes of operation:
- High-speed
- Slope control
- Low-power modes

The operation mode can be controlled by the Rs pin. Connect the Tx of the CAN controller to SN65HVD230's data input pin D to transmit data from the CAN node to the CAN network. Connect the RX of the CAN controller to SN65HVD230's data input pin R to receive data.

### Pin Configuration

| Pin | Name  | Description                     |
|-----|-------|---------------------------------|
| 1   | D     | Driver input                    |
| 2   | GND   | Ground                          |
| 3   | Vcc   | Supply voltage                  |
| 4   | R     | Receiver output                 |
| 5   | Vref  | Reference output                |
| 6   | CANL  | Low bus output                  |
| 7   | CANH  | High bus output                 |
| 8   | RS    | Standby/slope control           |

## RS485 Bus

The SP3485 is a low power half-duplex transceiver that meets the specifications of RS485 serial protocols. 

### Pin Descriptions

- **RO**: Receiver output pin
- **DI**: Driver input pin
- **RE**: Receiver Output Enable pin (Active LOW)
- **DE**: Driver output Enable pin (Active HIGH)
- **A**: Driver Output/Receiver input non-inverting port
- **B**: Driver Output/Receiver input inverting port
```


---
# Page 7
---

```markdown
# RS485 CAN HAT

## Output/Receiver Input

Inverting port. When \( A - B > +0.2V \), RO pin will output logic 1; and when \( A - B < -0.2V \), RO pin will output logic 0. A 100Ω resistor is recommended to add between A and B ports.

### Pin Function

| Pin | Function                                   |
|-----|--------------------------------------------|
| 1   | RO - Receiver Output                       |
| 2   | RE - Receiver Output Enable Active LOW     |
| 3   | DE - Driver Output Enable Active HIGH      |
| 4   | DI - Driver Input                          |
| 5   | GND - Ground Connection                    |
| 6   | A - Driver Output/Receiver Input Non-inverting |
| 7   | B - Driver Output/Receiver Input Inverting |
| 8   | VCC                                       |

According to the hardware description, RE and DE pins of SP3485 are set to enable receive and send.

This module is set to the way that hardware automatically receives/sends. You can also change to software receive/sending by changing the \( \Omega \) resistors on board.

## Hardware Auto Control

The hardware auto control circuit includes various components such as resistors, capacitors, and the MAX485 chip, which facilitate the automatic switching between receive and send modes.
```


---
# Page 8
---

```markdown
# RS485 CAN HAT

## Receiving Data
- **P_TX** is in idle state, which is high level.
- Transistor breakover, **RE** pin of **SP3485** is low to be active.
- **RO** pin begins to receive data from **485AB** port.

## Sending Data
- **P_TX** will get a pull-down level, toggling that sending data.
- Transistor cut off, **DE** pin is high to enable sending.
- In sending states, if the data sent is `"1"`, the transistor will turn to breakover, which looks like receiving states. However, the chip is in high impedance state, and data `"1"` will still be sending instead of changing to receiving.
```

---
# Page 9
---

```markdown
# RS485 CAN HAT

## HOW TO USE

### LIBRARIES INSTALLATION

To use the demo codes, you should install libraries (WiringPi, bcm2835, Python) first; otherwise, the codes cannot work properly. For instructions on how to install libraries, you can refer to the Wiki page:

[Waveshare Libraries Installation for RPi](https://www.waveshare.com/wiki/Libraries_Installation_for_RPi)

For Python, you should install two more libraries as follows:

```bash
sudo apt-get install python-pip
sudo pip install python-can
```

Visit Waveshare Wiki: [Waveshare Wiki](https://www.waveshare.com/wiki) and search for “RS485 CAN CAPE”, then download the demo code.

Decompress and copy to Raspberry Pi.
```

---
# Page 10
---

```markdown
# RS485 CAN HAT

## CAN TEST

### HARDWARE

- Raspberry Pi 3B x2
- Waveshare RS485 CAN HAT x2

### PREPARATION

1. Insert RS485 CAN HAT to Raspberry Pi, and then modify the `config.txt` file:

   ```bash
   sudo vi /boot/config.txt
   ```

2. Append these statements to the file:

   ```bash
   dtparam=spi=on
   dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25,spimaxfrequency=1000000
   ```

3. Save and exit, then restart your Pi:

   ```bash
   sudo reboot
   ```

4. After restart, check if it initializes successfully:

   ```bash
   dmesg | grep -i '\(can\|spi\)'
   ```

   It will print information as below:

   ```
   pigaraspberrypi:~ $ dmesg | grep -i '\(can\|spi\)'
   [  16.369868] systemd[1]: Cannot add dependency job for unit regenerate_ssh_host_keys.service, ignoring: Unit regener...
   [  16.537610] systemd[1]: Cannot add dependency job for unit display-manager.service, ignoring: Unit manager...
   [  20.892310] CAN device driver interface
   [  20.915184] mcp251x spi0.0 can0: MCP2515 successfully initialized.
   ```

   The information will be different if RS485 CAN HAT doesn't get inserted.
```


---
# Page 11
---

```markdown
# RS485 CAN HAT

In this case, you need to check if the module is connected. If the SPI interface and CP2515 kernel driver are enabled, restart the Raspberry Pi.

5. Connect the H and L port of RS485 CAN HAT to another device.

## C Code Example

1. List the folder of demo code you can get as below:

   ```
   pigraspberrypi:~ $ ls RS485_CAN_HAT_code/can/c/
   receive  send
   ```

2. **Set one HAT as receiver:** Enter the directory of the receiver and run the code:

   ```bash
   cd /RS485_CAN_HAT_code/can/c/receive
   make
   sudo ./can_receive
   ```

   Output:
   ```
   pigraspberrypi:~/RS485_CAN_HAT_code/can/c/receive $ sudo ./can_receive
   this is a can receive demo
   ```

3. **Set another as Sender:** Enter the directory of the sender and run the code:

   ```bash
   cd /RS485_CAN_HAT_code/can/c/send
   make
   sudo ./can_send
   ```
```

---
# Page 12
---

```markdown
# RS485 CAN HAT

## Sending and Receiving Data

To send data using the CAN protocol, execute the following command in the terminal:

```bash
sudo ./can_send
```

The output will display the following:

```
this is a can send demo
can_id = 0x123
can_dlc = 8
data[0] = 1
data[1] = 2
data[2] = 3
data[3] = 4
data[4] = 5
data[5] = 6
data[6] = 7
data[7] = 8
```

At the same time, you can find the receiver receiving the packet from the sender by executing:

```bash
sudo ./can_receive
```

The output will display:

```
RTNETLINK answers: Device or resource busy
this is a can receive demo
can_id = 0x123
can_dlc = 8
data[0] = 1
data[1] = 2
data[2] = 3
data[3] = 4
data[4] = 5
data[5] = 6
data[6] = 7
data[7] = 8
```

## Python Example

1. **List the folder:**

   Execute the following command to list the contents of the folder:

   ```bash
   ls
   ```

   The output will show:

   ```
   receive  send
   ```

   Navigate to the Python directory:

   ```bash
   cd ../python/
   ```

   List the contents again:

   ```bash
   ls
   ```

   The output will show:

   ```
   README.txt  receive.py  send.py
   ```

2. **Set the receiver first:**

   Execute the following command to start the receiver:

   ```bash
   sudo python can_receive.py
   ```

3. **Then the sender:**

   Execute the following command to start the sender:

   ```bash
   sudo python can_send.py
   ```
```

---
# Page 13
---

```markdown
# RS485 CAN HAT

## RS485 Test

### Hardware

- Raspberry Pi 3B x2
- RS485 CAN HAT x2

### Preparation

The serial of Raspberry Pi is used for Linux console output by default, so we need to disable it first:

1. Run command to open `raspi-config`:
   ```bash
   sudo raspi-config
   ```

2. Choose **Interfaces Options** -> **Serial** -> **no**
```
```

---
# Page 14
---

```markdown
# RS485 CAN HAT

## Raspberry Pi Software Configuration Tool (raspi-config)

- **P1 Camera**: Enable/Disable connection to the Raspberry Pi Camera
- **P2 SSH**: Enable/Disable remote command line access to your Pi using SSH
- **P3 VNC**: Enable/Disable graphical remote access to your Pi using RealVNC
- **P4 SPI**: Enable/Disable automatic loading of SPI kernel module
- **P5 I2C**: Enable/Disable automatic loading of I2C kernel module
- **P6 Serial**: Enable/Disable shell and kernel messages on the serial connection
- **P7 1-Wire**: Enable/Disable one-wire interface
- **P8 Remote GPIO**: Enable/Disable remote access to GPIO pins

## Configuration Steps

1. Open file `/boot/config.txt`, add the statement to the end:

   ```bash
   enable_uart=1
   ```

2. For Raspberry Pi, the serial port is used for Bluetooth, which should be commented:

   ```bash
   #dtoverlay=pi-minuart-bt
   ```

3. Reboot Raspberry Pi:

   ```bash
   sudo reboot
   ```

4. Connect A and B port of HAT to another's.

## WIRINGPI CODE
```


---
# Page 15
---

```markdown
# RS485 CAN HAT

## 1. List folders:
To list the folders, use the following command:
```bash
pigraspberrypi:~/RS485_CAN_HAT_code/485/WiringPi $ ls
receive send
```

## 2. Set receiver:
Navigate to the receiver directory and compile the code:
```bash
cd /RS485_CAN_HAT_code/can/c/receive
make
sudo ./can_receive
```
You should see the following output indicating success:
```
set wiringPi lib success !!!
```

## 3. Set sender:
Navigate to the sender directory and compile the code:
```bash
cd /RS485_CAN_HAT_code/can/c/send
make
sudo ./can_send
```
You should see the following output indicating success:
```
set wiringPi lib success !!!
send data 123456789
```

### Packet Received
The packet received at the receiver is as follows:
```
set wiringPi lib success !!!
1
2
3
4
5
5
6
7
8
9
```
```

---
# Page 16
---

```markdown
# RS485 CAN HAT

## PYTHON CODE

1. **List folders:**
   ```bash
   pigraspberrypi:~/RS485_CAN_HAT_code/485/python $ ls
   receive.py  send.py
   ```

2. **First set receiver:**
   ```bash
   sudo python reveive.py
   ```

3. **Set sender:**
   ```bash
   sudo python send.py
   ```
```

---
# Page 17
---

```markdown
# RS485 CAN HAT

## CODE ANALYSIS

### CAN

We provide two codes for CAN communication, one is C code and another is Python. C code uses socket-can and Python uses similar libraries as well.

### C CODE

This example uses socket skills similar to network coding skills of Linux. If you have studied Linux network coding, you will be familiar with it: Socketcan is the method for CAN protocol in Linux.

#### Step 1: Open socket

```c
s = socket(PF_CAN, SOCK_RAW, CAN_RAW);
```
If it failed, it will return -1.

#### Step 2: Target device can0

```c
strcpy(ifr.ifr_name, "can0");
ret = ioctl(s, SIOCGIFINDEX, &ifr);
```

#### Step 3: Bind socket to CAN interface

```c
addr.can_family = AF_CAN;
addr.can_ifindex = ifr.ifr_ifindex;
ret = bind(s, (struct sockaddr *)&addr, sizeof(addr));
```
```

---
# Page 18
---

```markdown
# RS485 CAN HAT

## Step 4: Set Rule That Only Send

```c
setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, NULL, 0);
```

## Step 5: Set the Data

```c
struct can_frame frame;
frame.can_id = 0x123;
frame.can_dlc = 8;
frame.data[0] = 1;
frame.data[1] = 2;
frame.data[2] = 3;
frame.data[3] = 4;
frame.data[4] = 5;
frame.data[5] = 6;
frame.data[6] = 7;
frame.data[7] = 8;
```

## Step 6: Transmit Data

```c
nbytes = write(s, &frame, sizeof(frame));
```

Calling `write()` function to write the data to socket, it will return -1 if failed and return the number of bytes if success. We could use the return value to check if it is successfully sending.

```c
if(nbytes != sizeof(frame)) {
    // Handle error
}
```
```

---
# Page 19
---

```markdown
# RS485 CAN HAT

## Step 7: Close Socket and CAN Device

```c
close(s);
system("sudo ifconfig can0 down");
```

**Note:** If you don't close the CAN device, the system will prompt that the CAN bus is busy at the next sending.

## For Receiving:

1. **Binding Socket**

   It is different when binding the socket:

   ```c
   addr.can_family = PF_CAN;
   addr.can_ifindex = ifr.ifr_ifindex;
   ret = bind(s, (struct sockaddr *)&addr, sizeof(addr));
   if (ret < 0) {
       perror("bind failed");
       return 1;
   }
   ```

2. **Receive Filter Definition**

   The receive could be defined to only receive socket whose ID is `0x123`:

   ```c
   struct can_filter rfilter[1];
   ```
```

---
# Page 20
---

```markdown
# RS485 CAN HAT

## C Code Example

### Setting Up CAN Filter

```c
rfilter[0].can_id = 0x123;
rfilter[0].can_mask = CAN_SFF_MASK;
setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));
```

### Read Data

```c
nbytes = read(s, &frame, sizeof(frame));
```

Return number of bytes it read.

For more information about socket-can coding, please refer to the [Socket-CAN Documentation](https://www.kernel.org/doc/Documentation/networking/can.txt).

## PYTHON

Before using the Python sample, check if the python-can library has been installed.

### Build Up CAN Device First

```python
os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')
```

### Step 1: Connect to CAN Bus

```python
can0 = can.interface.Bus(channel='can0', bustype='socketcan_ctypes')  # socketcan_native
```

### Step 2: Create Message

```python
msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
```

### Step 3: Send Message
```
```
``` 

This Markdown document maintains the structure and formatting of the original content while adhering to the specified guidelines.


---
# Page 21
---

```markdown
# RS485 CAN HAT

## Sending Data

```python
can0.send(msg)
```

## Step 4: Final Close Device as Well

```python
os.system('sudo ifconfig can0 down')
```

## Receive Data

```python
msg = can0.recv(10.0)
```

`recv()` defines the timeout of receiving.

For more information please refer to: [SocketCAN Documentation](https://python-can.readthedocs.io/en/stable/interfaces/socketcan.html)
```

---
# Page 22
---

```markdown
# RS485 CAN HAT

## RS485

For RS485 communication, we provide two sample codes: one is based on the wiringPi library and another is Python.

## WIRINGPI CODE

### Steps 1: Set Receiving and Sending

The RE and DE pins of SP3485 are used for enabling input and output.

```c
#define EN_485 18

if(wiringPiSetupGpio() < 0) { // use BCM2835 Pin number table
    printf("set wiringPi lib failed !!! \r\n");
    return -1;
} else {
    printf("set wiringPi lib success !!! \r\n");
}

pinMode(EN_485, OUTPUT);
digitalWrite(EN_485, HIGH);
```

The example code sets the module to sending states. The Pin 18 is the ID based on bcm2835 libraries. For wiringPi, the pin ID of bcm2835 is workable as well as wiringPi pin ID. `wiringPiSetupGpio()` is called for using bcm2835 pin ID and `wiringPiSetup()` is called for using wiringPi pin ID.
```

---
# Page 23
---

```markdown
# RS485 CAN HAT

## Step 2: Create File Descriptor

Open serial `/dev/ttyS0` and set baud rate.

```c
if((fd = serialOpen("/dev/ttyS0",9600)) < 0) {
    printf("serial err\n");
    return -1;
}
```

## Step 3: Send Data

```c
serialFlush(fd);
serialPrintf(fd, "\r");
serialPuts(fd, "12345");
serialFlush(); // Clean all data on serial and wait for sending
serialPrintf(); // Similar to printf function, bind the transmit data to file descriptor
serialPuts(); // Send string which ends with null to serial device marked by related file descriptor
```

The `serialGetchar(fd)` function will return a character which should be used next for the serial device. It may cause some errors, so the sender should send a character `"\r"` to avoid this phenomenon. 

*(If you have a better way, kindly contact us.)*

For more information about functions, please refer to:  
[WiringPi Serial Library](http://wiringpi.com/reference/serial-library/)
```

---
# Page 24
---

```markdown
# RS485 CAN HAT

## PYTHON CODE

Using Python to control RS485 will be much easy. Python could operate serial directly:

Open serial file and set the baud rate as well.

```python
t = serial.Serial("/dev/ttyS0", 115200)
```

Set the command which you want to send:

```python
command = ["a", "b", "c", "", "1", "5", 0x24, 0x48]
```

Write the data to serial, and it will respond with the number of bytes written:

```python
len = ser.write(command)
print("len:", len)
```

### Reading

Return the number of bytes in buffer:

```python
ser.inWaiting()
```

Read data (length is definable):

```python
ser.read(ser.inWaiting())
```
```

---



---

# Can Rs485 Can Shield Schematic {#can-rs485-can-shield-schematic}

---
# Page 1
---

```markdown
# RS485 CAN Shield

**Size:** A4  
**Date:** 2015/4/20  
**File:** E:\PCB\RS485 CAN Shield.SchDoc  
**Sheet:** 1  
**Drawn By:** [Your Name]

## 1. 485 Receiving Circuit

```
   +---+---+
   | U1|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |485_RX|RO |
   | 2 | 3 |
   |485_E |RE |
   | 4 | 5 |
   |485_TX|DI |
   +---+---+
```

### Components:
- **MAX485**
  - Pin 1: 485_RX
  - Pin 2: RO
  - Pin 3: RE
  - Pin 4: DE
  - Pin 5: DI
  - Pin 6: A
  - Pin 7: B
  - Pin 8: VCC

### Connections:
- **C1:** 104
- **R1:** 120Ω
- **GND:** Connected to pin 4 of MAX485

## 2. CAN Receiving Circuit

```
   +---+---+
   | U2|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |CAN_TX|D |
   | 3 | 4 |
   |CAN_RX|GND|
   | 5 | 6 |
   |VCC_CANL|Vref|
   +---+---+
```

### Components:
- **SN65HVD230**
  - Pin 1: CAN_TX
  - Pin 2: GND
  - Pin 3: CAN_RX
  - Pin 4: VCC_CANH
  - Pin 5: VCC_CANL
  - Pin 6: Vref

### Connections:
- **C2:** 104
- **R2:** 1k
- **R3:** 120Ω
- **GND:** Connected to pin 2 of SN65HVD230

## 3. 485 RXD/TXD Jump

```
   +---+---+
   | P1|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |TX1 |RX1|
   | 3 | 4 |
   |485_TX|485_EX|
   | 5 | 6 |
   |TX2 |RX2|
   +---+---+
```

## 4. CAN Jump

```
   +---+---+
   | P3|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |D14 |CAN_TX|
   | 3 | 4 |
   |D15 |CAN_RX|
   +---+---+
```

## 5. 485 Chip Selection

```
   +---+---+
   | P2|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |485_F|D7|
   +---+---+
```

## 6. Extension Power

```
   +---+---+
   | P2|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |3V3 |GND|
   | 3 | 4 |
   |SV |NC|
   +---+---+
```

## 7. Extension Interface

```
   +---+---+
   | H1|   |
   |   |   |
   |   |   |
   +---+---+
   | 1 | 2 |
   |D15 |D14|
   | 3 | 4 |
   |AVDD|GND|
   | 5 | 6 |
   |D12 |D11|
   +---+---+
```

### Additional Components:
- **C3:** 104
- **C4:** 104
- **R4:** 3V3
- **R5:** 5V
- **R6:** 1k
- **PWR_LED:** Connected to GND

## Notes
- Ensure all connections are secure.
- Verify component values before assembly.
```


---



---

# Can Rs485 Can Shield User Manual {#can-rs485-can-shield-user-manual}

---
# Page 1
---

```markdown
# RS485 CAN Shield User Manual

## Overview

The RS485 CAN Shield will easily enable RS485/CAN communication functions for your NUCLEO/XNUCLEO Arduino boards.

## Features

- **Arduino standard interfaces**, compatible with Arduino boards like Arduino UNO, Leonardo, NUCLEO, XNUCLEO
  - *Note*: When using with Arduino UNO, Leonardo, the CAN function is unavailable due to hardware limitation.
- **RS485 function**, onboard transceiver MAX3485, 3.3V power supply
- **CAN function**, onboard transceiver SN65HVD230, 3.3V power supply

---

**Rev**: V1.4, **Date**: May 19th, 2015
```

---
# Page 2
---

```markdown
# RS485 CAN Shield User Manual

## Contents

- [Overview](#overview) ......................................................................................................................... 1
- [1. Hardware Description](#1-hardware-description) ........................................................................ 3
  - [1.1 Chip Pins Feature](#11-chip-pins-feature) ............................................................................... 3
    - [1.1.1 MAX3485](#111-max3485) ................................................................................................. 3
    - [1.1.2 SN65HVD230](#112-sn65hvd230) ..................................................................................... 4
- [2. How to use](#2-how-to-use) ......................................................................................................... 4
  - [2.1 Preparations](#21-preparations) ............................................................................................. 4
  - [2.2 Description of Jumper settings on Xnucleo](#22-description-of-jumper-settings-on-xnucleo) ........................................................................................................... 4
  - [2.3 Working principle](#23-working-principle) ............................................................................. 5
    - [2.3.1 Sending side program description](#231-sending-side-program-description) ............... 6
    - [2.3.2 Receiving side program description](#232-receiving-side-program-description) .......... 7
    - [2.3.3 Operating phenomenon](#233-operating-phenomenon) .................................................. 8

---

**Rev: V1.4, Date: May 19th 2015**
```


---
# Page 3
---

```markdown
# RS485 CAN Shield User Manual

## 1. Hardware Description

### 1.1. Chip Pins Feature

#### 1.1.1. MAX3485

The MAX3485 is 3.3V low-power transceivers for RS-485 communication. Each part contains one driver and one receiver. RS-485 works under a single power supply and communicates with half-duplex mode.

```
Pin Name   Function
1   RO     Receiver Output.
2   RE     Receiver Output Enable
           Active LOW
3   DE     Driver Output Enable
           Active HIGH
4   DI     Driver Input
5   GND    Ground Connection
6   A      Driver Output/Receiver Input.
           Non-inverting
7   B      Driver Output/Receiver Input.
           Inverting
8   Vcc    Power Supply
```

### Table 1: Transmit Function Truth Table

| Inputs | RE | DE | DI | Line Condition | Outputs | B | A |
|--------|----|----|----|----------------|---------|---|---|
|        | X  | 1  | 1  | No Fault       |         | 0 | 1 |
|        | X  | 1  | 0  | No Fault       |         | 1 | 0 |
|        | X  | 0  | X  | X              |         | Z | Z |

### Table 2: Receive Function Truth Table

| Inputs | RE | DE | A-B | Outputs |
|--------|----|----|-----|---------|
|        | 0  | 0  | >+0.2V | 1       |
|        | 0  | 0  | <0.2V  | 0       |
|        | 0  | 0  | Inputs Open | 1   |
|        | 1  | 0  | X       | Z       |

Rev: V1.4, Date: May 19th, 2015
```

---
# Page 4
---

```markdown
# RS485 CAN Shield User Manual

## 1.1.2. SN65HVD230

The SN65HVD230 controller area network (CAN) transceivers are designed by Texas Instruments. It applies to CAN bus serial communication of higher speed, anti-jamming capability, and high reliability.

On the SN65HVD230, pin 8 (Rs) provides three different modes of operation: high-speed, slope control, and low-power modes. The sending pin Tx of the CAN controller is connected to Driver input (D) of SN65HVD230. It sends the CAN node data to the CAN network. The receiving pin Tx of the CAN controller is connected to Receiver output (R) of SN65HVD230.

### Pin Configuration

| NO. | NAME         | DESCRIPTION                       |
|-----|--------------|-----------------------------------|
| 1   | D            | Driver input                      |
| 2   | GND          | Ground                            |
| 3   | VCC          | Supply voltage                    |
| 4   | R            | Receiver output                   |
| 5   | Vref         | Reference output                  |
| 6   | CANL         | Low bus output                    |
| 7   | CANH         | High bus output                   |
| 8   | Rs           | Standby/slope control             |

**Top View of SN65HVD230**

```
       D  1
      GND 2
      VCC 3
       R  4
     Vref 5
     CANL 6
     CANH 7
      Rs  8
```

## 2. How to Use

### 2.1. Preparations

- Two RS485 CAN Shields
- Two STM32 development boards; we use Waveshare Xnucleo-F103RB board (with STM32F103R chip) in this manual.
- Some jumper wires.

### 2.2. Description of Jumper Settings on Xnucleo

- D14 (PB_9) and D15 (PB_8) are CAN's sending and receiving ports respectively as default.  
  **Note:** Please remap PB_9 and PB_8 to the function of STM32 CAN1 by modifying the program:  
  `GPIO_PinRemapConfig(GPIO_Remap1_CAN1, ENABLE);`

- D7 (PA_8) is for RS485 sending or receiving enable. High level is for sending, low level is for receiving.

- D8 (PA_9), D2 (PA_10) are the sending and receiving ports of UART1. D0 (PA_2), D1 (PA_3) are the sending and receiving ports of UART2. You can choose UART1 or UART2 for RS485 transceiver port by setting jumper 485 RXD/TXD JMP.
```


---
# Page 5
---

```markdown
# RS485 CAN Shield User Manual

**Note:** PA_2 and PA_3 of Xnucleo are Serial to USB ports as default. If you want to use D0 and D1 as RS485 serial port, the jumper JP4 should be set: connect pin 1 and 3, connect pin 2 and pin 4. The schematic of JP4 on Xnucleo is shown in the following figure:

```
JP4
| D0 /RX | 1 | 2 | D1 /TX |
| PA 3 /RX | 3 | 4 | PA 2 /TX |
| TXD | 5 | 6 | RXD |
| PA 10 /RX | 7 | 8 | PA 9 /TX |
```

- **Communication between two boards:** Connect the CANH and CANL to another one’s CANH and CANL of the CAN port separately. Connect the A and B to another one’s A and B of the RS485 port separately.

## 2.3. Working Principle

The demo program, divided into sending and receiving program, is based on mbed framework + STM32 library.

### CAN:

The CAN driver is written based on STM32 library, packaged into the two files `CAN.cpp` and `CAN.h`.

At the beginning of the program, the function `CAN_Config()` is called to initiate related registers.

At the side of sending program, the message to be sent will be saved into the Mailbox `TxMessage`, then it will be sent by calling `CAN_Transmit(CAN1, &TxMessage)`.

At the side of receiving program, the message received will be saved into the Mailbox `RxMessage` by calling `CAN_Receive(CAN1, CAN_FIFO00, &RxMessage)`.

### RS485:

The sending side program sets `RS485_E` to high level, which will make RS485 into sending status. Messages will be sent by function `RS485.printf()`, through RS485 serial port.

The receiving side program enables reception interruption, and sets `RS485_E` to low level, which will set RS485 to receiving status. Then, the RX interrupt handler will scan received message via `RS485.sscanf()`.

### Connection:

- D14 and D15 are CAN's sending and receiving port respectively as default.

Rev: V1.4, Date: May 19th 2015
```

---
# Page 6
---

```markdown
# RS485 CAN Shield User Manual

## 2.3.1 Sending Side Program Description

- **D8(PA_9), D2(PA_10)** are the sending and receiving port of RS485.
- **D7(PA_8)** is for RS485 sending or receiving enable. High level is for sending, low level is for receiving.
- Message is sent to the serial port of PC through D0 and D1.
- The CANH and CANL of one CAN port should be connected to another’s CANH and CANL port, and the A and B port of one RS485 should be connected to another’s A and B.

### Code Example

```cpp
#include "mbed.h" // Include mbed library
#include "CAN.h"   // Include CAN library

Serial pc(D1, D0); // Serial print message
Serial RS485(D8, D2); // RS485_TX RS485_RX
DigitalOut RS485_E(D7); // RS485_E

CanTxMsg TxMessage; // CAN transmit message
uint8_t TransmitMailbox = 0; // Mailbox for transmission
int i = 0, j = 0; // Initialize counters

int main() {
    CAN_Config(); // CAN initiation
    RS485_E = 1; // Enable RS485 sending status

    /* TxMessage */
    TxMessage.StdId = 0x10; // Set standard ID
    TxMessage.ExtId = 0x1234; // Set extended ID
    TxMessage.RTR = CAN_RTR_DATA; // Set remote transmission request
    TxMessage.IDE = CAN_ID_STD; // Set identifier type
    TxMessage.DLC = 8; // Set data length code
    TxMessage.Data[0] = 'C'; // Set data
    TxMessage.Data[1] = 'A';
    TxMessage.Data[2] = 'N';
    TxMessage.Data[3] = ' ';
    TxMessage.Data[4] = 'T'; // Continue setting data
```

### Notes
- Ensure that all related registers are initiated before sending messages.
- The message to be sent will be saved into the Mailbox, and then it will be sent by driver functions.
- Set RS485_E to high level to make RS485 into sending status. Messages will be sent through RS485 serial port.
```


---
# Page 7
---

```markdown
# RS485 CAN Shield User Manual

## 2.3.2. Receiving Side Program Description

### CAN
After related registers are initiated, the receiving side will check if FIFO data exists. If yes, the received message will be saved in the mailbox `RxMessage` and printed.

### RS485
Enable RS485 reception interruption and set `RS485_E` to low for setting RS485 to receiving status. Then, the interrupt service routine will scan the received message via `RS485.scanf`.

### Code Example
```c
TxMessage.Data[5] = 'e';
TxMessage.Data[6] = 's';
TxMessage.Data[7] = 't';

pc.printf("***** This is a RS485_CAN_Shield Send test program *****\r\n");

while(1) {
    RS485.printf("ncounter=%d ", j); // RS485 sending
    wait(1);
    TransmitMailbox = CAN_Transmit(CAN1, &TxMessage); // CAN sending

    i = 0;
    while((CAN_TransmitStatus(CAN1, TransmitMailbox) != CANTXOK) && (i != 0xFFFF)) {
        i++;
    }

    if(i == 0xFFFF) {
        pc.printf("\r\nCAN send fail\r\n"); // Send Timeout, fail
    } else {
        pc.printf("\r\nCAN send TxMessage successfully \r\n"); // Send successfully
    }
    pc.printf("\r\nRS485 send: counter=%d\r\n", j++); // print message
    pc.printf("The CAN TxMsg: %s\r\n", TxMessage.Data);
    
    wait(1);
}
```
``` 

**Rev: V1.4, Date: May 19th 2015**
```

---
# Page 8
---

```markdown
# RS485 CAN Shield User Manual

```cpp
#include "mbed.h"
#include "CAN.h"

Serial pc(D1,D0); // serial print message
Serial RS485(D8, D2); // RS485_TX RS485_RX
DigitalOut RS485_E(D7); // RS485_E
CanRxMsg RxMessage; // RxMessage
char s[1024];

void callback() { // RS485 RX interrupt handler
    // Note: you need to actually read from the serial to clear the RX interrupt
    RS485.scanf("%s",s); // Save received messages
    pc.printf("\r\nRS485 Receive:%s \r\n",s); // Print Received messages
}

int main() {
    CAN_Config(); // CAN initiation
    RS485.attach(&callback); // Open RS485 reception interruption
    RS485_E = 0; // Enable receiving status
    pc.printf("***** This is a can receive test program *****\r\n");
    while(1) {
        while(CAN_MessagePending(CAN1, CAN_FIFO0) < 1) { // Message waiting
        }
        CAN_Receive(CAN1, CAN_FIFO0, &RxMessage); // CAN data reception
        pc.printf("The CAN RxMsg: %s\r\n", RxMessage.Data); // Print received messages
    }
}
```

## 2.3.3. Operating Phenomenon

The serial port of the sending side will print:

```
***** This is a RS485_CAN_Shield Send test program *****
CAN send TxMessage successfully
RS485 send: counter=0
```

Rev: V1.4, Date: May 19th 2015
```

---
# Page 9
---

```markdown
# RS485 CAN Shield User Manual

## Transmitting Messages

The CAN TxMsg: CAN Test  
CAN send TxMessage successfully  

```
RS485 send: counter=1  
The CAN TxMsg: CAN Test  
CAN send TxMessage successfully  

RS485 send: counter=2  
The CAN TxMsg: CAN Test  
```

## Receiving Messages

The serial port of receiving side will print:

```
**** This is a can receive test program ****  

RS485 Receive:ncounter=0  
The CAN RxMsg: CAN Test  

RS485 Receive:ncounter=1  
The CAN RxMsg: CAN Test  

RS485 Receive:ncounter=2  
The CAN RxMsg: CAN Test  

RS485 Receive:ncounter=3  
The CAN RxMsg: CAN Test  
```

---

**Rev: V1.4, Date: May 19th 2015**
```

---



---

# Can Sn65Hvd230 {#can-sn65hvd230}

---
# Page 1
---

```markdown
# 3.3V CAN TRANSCEIVERS

Check for Samples: SN65HVD230, SN65HVD231, SN65HVD232

## FEATURES

- Operates With a 3.3-V Supply
- Low Power Replacement for the PCA82C250 Footprint
- Bus/Pin ESD Protection Exceeds 16 kV HBM
- High Input Impedance Allows for 120 Nodes on a Bus
- Controlled Driver Output Transition Times for Improved Signal Quality on the SN65HVD230 and SN65HVD231
- Unpowered Node Does Not Disturb the Bus
- Compatible With the Requirements of the ISO 11898 Standard
- Low-Current SN65HVD230 Standby Mode 370 µA Typical
- Low-Current SN65HVD231 Sleep Mode 40 nA Typical
- Designed for Signaling Rates up to 1 Megabit/Second (Mbps)
- Thermal Shutdown Protection
- Open-Circuit Fail-Safe Design
- Glitch-Free Power-Up and Power-Down Protection for Hot-Plugging Applications

## APPLICATIONS

- Motor Control
- Industrial Automation
- Basteation Control and Status
- Robotics
- Automotive
- UPS Control

## LOGIC DIAGRAM (POSITIVE LOGIC)

### SN65HVD230, SN65HVD231

```
       VCC
        |
        |
        +---+
        |   |
        |   |
        |   |
        +---+
        |   |
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |   |
        |   |
        +---+
        |

---
# Page 2
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232

**SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011**  
**www.ti.com**

> These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

## DESCRIPTION

The SN65HVD230, SN65HVD231, and SN65HVD232 controller area network (CAN) transceivers are designed for use with the Texas Instruments TMS320LX240™; 3.3-V DSPs with CAN controllers, or with equivalent devices. They are intended for use in applications employing the CAN serial communication physical layer in accordance with the ISO 11898 standard. Each CAN transceiver is designed to provide differential transmit capability to the bus and differential receive capability to a CAN controller at speeds up to 1 Mbps.

Designed for operation in especially-harsh environments, these devices feature cross-wire protection, loss-of-ground and overvoltage protection, overtemperature protection, as well as wide common-mode range.

The transceiver interfaces the single-ended CAN controller with the differential CAN bus found in industrial, building automation, and automotive applications. It operates over a -2 V to 7 V common-mode range on the bus, and it can withstand common-mode transients of ±25 V.

On the SN65HVD230 and SN65HVD231, pin 8 provides three different modes of operation: high-speed, slope control, and low-power modes. The high-speed mode of operation is selected by connecting pin 8 to ground, allowing the transmitter output transistors to switch on and off as fast as possible with no limitation on the rise and fall slopes. The rise and fall slopes can be adjusted by connecting a resistor to ground at pin 8, since the slope is proportional to the pin's output current. This slope control is implemented with external resistor values of 10 kΩ, to achieve a 15 V/µs slew rate, to 100 kΩ, to achieve a 2 V/µs slew rate. See the Application Information section of this datasheet.

The circuit of the SN65HVD230 enters a low-current standby mode during which the driver is switched off and the receiver remains active if a high logic level is applied to pin 8. The DSP controller reserves this low-current standby mode when a dominant state (differential voltage > 900 mV typical) occurs on the bus.

The unique difference between the SN65HVD230 and the SN65HVD231 is that both the driver and the receiver are switched off in the SN65HVD231 when a high logic level is applied to pin 8 and remains in this sleep mode until the circuit is reactivated by a low logic level on pin 8.

The Vref pin 5 on the SN65HVD230 and SN65HVD231 is available as a VCC/2 voltage reference.

The SN65HVD232 is a basic CAN transceiver with no added options; pins 5 and 8 are NC, no connection.

## Table 1. AVAILABLE OPTIONS

| PART NUMBER  | LOW POWER MODE         | INTEGRATED SLOPE CONTROL | Vref PIN | TA                | MARKED AS: |
|--------------|------------------------|--------------------------|----------|-------------------|------------|
| SN65HVD230   | Standby mode           | Yes                      | Yes      | VP230             |
| SN65HVD231   | Sleep mode             | Yes                      | Yes      | 40°C to 85°C      | VP231      |
| SN65HVD232   | No standby or sleep mode| No                       | No       | VP232             |

## FUNCTION TABLES

| INPUT D | RS      | CANH | CANL | BUS STATE  |
|---------|---------|------|------|------------|
| L       | V(RS) < 1.2 V | H    | L    | Dominant   |
| H       | Z       | Z    | Z    | Recessive  |
| Open    | X       | Z    | Z    | Recessive  |
| X       | V(RS) > 0.75 Vcc | Z    | Z    | Recessive  |

> (1) H = high level; L = low level; X = irrelevant; ? = indeterminate; Z = high impedance.

---

**© 2001–2011, Texas Instruments Incorporated**
```

---
# Page 3
---

```markdown
# SN65HVD230 / SN65HVD231 / SN65HVD232

## Table 2. Driver (SN65HVD232)

| INPUT D | OUTPUTS | BUS STATE  |
|---------|---------|------------|
| L       | H       | L          | Dominant  |
| H       | Z       | Z          | Recessive  |
| Open    | Z       | Z          | Recessive  |

*(1) H = high level; L = low level; Z = high impedance*

## Table 3. Receiver (SN65HVD230)

| DIFFERENTIAL INPUTS | Rs | OUTPUT R |
|---------------------|----|----------|
| V_ID ≥ 0.9 V       | X  | L        |
| 0.5 V < V_ID < 0.9 V | X  | ?        |
| V_ID ≤ 0.5 V       | X  | H        |
| Open                | X  | H        |

*(1) H = high level; L = low level; X = irrelevant; ? = indeterminate*

## Table 4. Receiver (SN65HVD231)

| DIFFERENTIAL INPUTS | Rs | OUTPUT R |
|---------------------|----|----------|
| V_ID ≥ 0.9 V       | V(Rs) < 1.2 V | L        |
| 0.5 V < V_ID < 0.9 V | V(Rs) > 0.75 V_CC | H        |
| V_ID ≤ 0.5 V       | X  | H        |
| Open                | X  | H        |

*(1) H = high level; L = low level; X = irrelevant; ? = indeterminate*

## Table 5. Receiver (SN65HVD232)

| DIFFERENTIAL INPUTS | OUTPUT R |
|---------------------|----------|
| V_ID ≥ 0.9 V       | L        |
| 0.5 V < V_ID < 0.9 V | ?        |
| V_ID ≤ 0.5 V       | H        |
| Open                | H        |

*(1) H = high level; L = low level; X = irrelevant; ? = indeterminate*

## Table 6. Transceiver Modes (SN65HVD230, SN65HVD231)

| V(Rs)               | OPERATING MODE       |
|---------------------|----------------------|
| V(Rs) > 0.75 V_CC   | Standby              |
| 10 kΩ to 100 kΩ to ground | Slope control   |
| V(Rs) < 1 V        | High speed (no slope control) |
```


---
# Page 4
---

```markdown
# TERMINAL FUNCTIONS

## SN65HVD230, SN65HVD231

| TERMINAL | NO. | DESCRIPTION                |
|----------|-----|----------------------------|
| CANL     | 6   | Low bus output             |
| CANH     | 7   | High bus output            |
| D        | 1   | Driver input               |
| GND      | 2   | Ground                     |
| R        | 4   | Receiver output            |
| RS       | 8   | Standby/slope control      |
| VCC      | 3   | Supply voltage             |
| Vref     | 5   | Reference output           |

## SN65HVD232

| TERMINAL | NO. | DESCRIPTION                |
|----------|-----|----------------------------|
| CANL     | 6   | Low bus output             |
| CANH     | 7   | High bus output            |
| D        | 1   | Driver input               |
| GND      | 2   | Ground                     |
| NC       | 5,8 | No connection              |
| R        | 4   | Receiver output            |
| VCC      | 3   | Supply voltage             |

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 5
---

```markdown
# Equivalent Input and Output Schematic Diagrams

## CANH and CANL Inputs

```
       Vcc
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
```

- **Input Voltage Levels:**
  - 16 V
  - 20 V

- **Resistor Values:**
  - 110 kΩ
  - 9 kΩ
  - 45 kΩ

## D Input

```
       Vcc
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
```

- **Input Voltage Levels:**
  - 9 V

- **Resistor Values:**
  - 1 kΩ
  - 100 kΩ

## CANH and CANL Outputs

```
       Vcc
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
```

- **Output Voltage Levels:**
  - 16 V
  - 20 V

## R Output

```
       Vcc
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
        |
        |
       ----
      |    |
      |    |
      |    |
      |    |
      |    |
      ------
```

- **Output Voltage Levels:**
  - 9 V

- **Resistor Value:**
  - 5 Ω

---

© 2001–2011, Texas Instruments Incorporated
```


---
# Page 6
---

```markdown
# SN65HVD230 / SN65HVD231 / SN65HVD232

## ABSOLUTE MAXIMUM RATINGS
over operating free-air temperature range (unless otherwise noted)¹ (²)

| Parameter                                   | Unit          |
|---------------------------------------------|---------------|
| Supply voltage, V<sub>CC</sub>              | -0.3 to 6 V   |
| Voltage range at any bus terminal (CANH or CANL) | -4 to 16 V   |
| Voltage input range, transient pulse, CANH and CANL, through 100 Ω (see Figure 7) | -25 to 25 V   |
| Input voltage range, V<sub>I</sub> (D or R) | -0.5 to V<sub>CC</sub> + 0.5 V |
| Receiver output current, I<sub>O</sub>      | ±11 mA       |
| Electrostatic discharge                      |               |
| Human body model³                           | CANH, CANL and GND | 16 kV |
| Charged-device model⁴                        | All pins      | 4 kV  |
| Continuous total power dissipation          | All pins      | 1 kV  |

1. Stresses beyond those listed under "absolute maximum ratings" may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under "recommended operating conditions" is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.  
2. All voltage values, except differential bus voltages, are with respect to network ground terminal.  
3. Tested in accordance with JEDEC Standard 22, Test Method A114-A.  
4. Tested in accordance with JEDEC Standard 22, Test Method C101.  

## THERMAL INFORMATION

| Parameter                                   | SN65HVD230   | SN65HVD231   | SN65HVD232   | Units       |
|---------------------------------------------|---------------|---------------|---------------|-------------|
| θ<sub>JA</sub>                              | 76.8          | 101.5         | 101.5         | °C/W       |
| θ<sub>JCtop</sub>                           | 33.4          | 43.3          | 43.3          | °C/W       |
| θ<sub>JB</sub>                              | 15.3          | 42.2          | 42.4          | °C/W       |
| θ<sub>JT</sub>                              | 1.4           | 4.8           | 4.8           | °C/W       |
| θ<sub>JB</sub>                              | 14.9          | 41.8          | 41.8          | °C/W       |
| θ<sub>JCbot</sub>                           | n/a           | n/a           | n/a           | °C/W       |

1. For more information about traditional and new thermal metrics, see the IC Package Thermal Metrics application report, SPRA953.

## RECOMMENDED OPERATING CONDITIONS

| Parameter                                   | Min   | Nom   | Max   | Unit       |
|---------------------------------------------|-------|-------|-------|------------|
| Supply voltage, V<sub>CC</sub>              | 3     |       | 3.6   | V          |
| Voltage at any bus terminal (common mode) V<sub>IC</sub> | -2 (1) |       | 7     | V          |
| Voltage at any bus terminal (separately) V<sub>I</sub> | -2.5  |       | 7.5   | V          |
| High-level input voltage, V<sub>IH</sub>    |       | D, R  | 2     | V          |
| Low-level input voltage, V<sub>IL</sub>     |       | D, R  | 0.8   | V          |
| Differential output voltage, V<sub>OD</sub> | -6    |       | 6     | V          |
| Input voltage, V<sub>RS</sub>                | 0     | V<sub>CC</sub> | V<sub>CC</sub> | V          |
| Input voltage for standby or sleep, V<sub>RS</sub> | 0.75 V<sub>CC</sub> | V<sub>CC</sub> | V          |
| Wave-shaping resistance, R<sub>S</sub>      | 0     |       | 100   | kΩ         |
| High-level output current, I<sub>OH</sub>    |       | Driver | -40   | mA         |
| Low-level output current, I<sub>OL</sub>     |       | Receiver | -8   | mA         |
| Operating free-air temperature, T<sub>A</sub> | -40   |       | 85    | °C         |

1. The algebraic convention, in which the least positive (most negative) limit is designated as minimum is used in this data sheet.
```

---
# Page 7
---

```markdown
# DRIVER ELECTRICAL CHARACTERISTICS
*over recommended operating conditions (unless otherwise noted)*

## Parameters

| **PARAMETER**         | **TEST CONDITIONS**                     | **MIN** | **TYP** | **MAX** | **UNIT** |
|-----------------------|-----------------------------------------|---------|---------|---------|----------|
| V_OH                   | Dominant                                | V_I = 0 V, See Figure 1 and Figure 3 | CANH   | 2.45    | V_CC    |
|                       |                                         |         | CANL   | 0.5     | 1.25    | V      |
| V_OL                   | Recessive                               | V_I = 3 V, See Figure 1 and Figure 3 | CANH   | 2.3     | V      |
|                       |                                         |         | CANL   | 2.3     | V      |
| V_OD(D)               | Differential output voltage             | V_I = 0 V, See Figure 1               | 1.5    | 2      | 3      | V      |
| V_OD(R)               | Recessive                               | V_I = 3 V, See Figure 1               | -120   | 0      | 12     | mV     |
| I_HR                  | High-level input current                | V_I = 2 V                             | -0.5   | -0.2   | 0.05   | V      |
| I_LL                  | Low-level input current                 | V_I = 0.8 V                           | -30    | µA     |        |
| I_OS                  | Short-circuit output current            | V_CANH = 2 V, V_CANL = 7 V            | -250   | 250    | mA     |
| C_O                   | Output capacitance                      | See receiver                           |         |        |        |
| I_CC                  | Supply current                          | Standby SN65HVD230 V_R(SB) = V_CC    | 370    | 600    | µA     |
|                       | Sleep SN65HVD231 V_R(SB) = V_CC, D at V_CC | 0.04   | 1      | µA     |        |
|                       | All devices                            | V_I = 0 V, No load                    | Dominant | 10     | 17     | mA     |
|                       |                                         | V_I = V_CC, No load                   | Recessive | 10    | 17     | mA     |

*(1) All typical values are at 25°C and with a 3.3 V supply.*

---

# DRIVER SWITCHING CHARACTERISTICS
*over recommended operating conditions (unless otherwise noted)*

## Parameters

| **PARAMETER**         | **TEST CONDITIONS**                     | **MIN** | **TYP** | **MAX** | **UNIT** |
|-----------------------|-----------------------------------------|---------|---------|---------|----------|
| t_PHL                 | Propagation delay time, low-to-high-level output | V_R(SB) = 0 V, R_S with 10 kΩ to ground | 35      | 85      | ns       |
| t_PLH                 | Propagation delay time, high-to-low-level output | V_R(SB) = 0 V, R_S with 10 kΩ to ground | 70      | 120     | ns       |
| t_sk                  | Pulse skew (t_PHL + t_PLH)             | V_R(SB) = 0 V, R_S with 10 kΩ to ground | 35      | 60      | ns       |
|                       |                                         | R_S with 100 kΩ to ground              |         | 370     | ns       |
| t_r                   | Differential output signal rise time    | V_R(SB) = 0 V                           | 25      | 50      | 100     | ns       |
| t_f                   | Differential output signal fall time     | V_R(SB) = 0 V                           | 40      | 55      | ns       |
| t_r                   | Differential output signal rise time     | R_S with 10 kΩ to ground                | 80      | 120     | 160     | ns       |
| t_r                   | Differential output signal fall time      | R_S with 10 kΩ to ground                | 80      | 125     | 150     | ns       |
| t_r                   | Differential output signal fall time      | R_S with 100 kΩ to ground               | 600     | 800     | 1200    | ns       |

## SN65HVD232 Parameters

| **PARAMETER**         | **TEST CONDITIONS**                     | **MIN** | **TYP** | **MAX** | **UNIT** |
|-----------------------|-----------------------------------------|---------|---------|---------|----------|
| t_PLH                 | Propagation delay time, low-to-high-level output | V_R(SB) = 0 V | 35      | 85      | ns       |
| t_PHL                 | Propagation delay time, high-to-low-level output | C_L = 50 pF, See Figure 4 | 35      | 70      | ns       |
| t_sk                  | Pulse skew (t_PHL + t_PLH)             | R_S = 50 pF, See Figure 4 | 25      | 50      | ns       |
| t_r                   | Differential output signal rise time     | R_S with 100 kΩ to ground | 40      | 55      | ns       |

---

*© 2001–2011, Texas Instruments Incorporated*
```

---
# Page 8
---

```markdown
# SN65HVD230
# SN65HVD231
# SN65HVD232
# SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011

## RECEIVER ELECTRICAL CHARACTERISTICS
over recommended operating conditions (unless otherwise noted)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|-----------|----------------|-----|-----|-----|------|
| V_IT+     | Positive-going input threshold voltage | 750 | 900 | mV |
| V_IT-     | Negative-going input threshold voltage | See Table 7 | 500 | 650 | mV |
| V_HYS     | Hysteresis voltage (V_IT+ - V_IT-) | 100 | | mV |
| V_OH      | High-level output voltage | -6 V ≤ V_ID ≤ 500 mV, I_O = -8 mA | See Figure 5 | 2.4 | V |
| V_OL      | Low-level output voltage | 900 mV ≤ V_ID ≤ 6 V, I_O = -8 mA | See Figure 5 | 0.4 | V |
| I_I       | Bus input current | V_IH = 7 V, V_CC = 0 V <br> Other input at 0 V, D = 3 V | 100 | 250 | µA |
|           | | V_IH = 7 V, V_CC = 0 V <br> V_IH = -2 V | -200 | -30 | µA |
| C_I       | CANH, CANL input capacitance | Pin-to-ground, V_I = 0.4 sin(4E6πt) + 0.5 V, V_ID = 3 V | 32 | pF |
| C_DIFF    | Differential input capacitance | Pin-to-pin, V_I = 0.4 sin(4E6πt) + 0.5 V, V_ID = 3 V | 16 | pF |
| R_DIFF    | Differential input resistance | Pin-to-pin, V_ID = 3 V | 40 | 70 | 100 | kΩ |
| R_I       | CANH, CANL input resistance | | 20 | 35 | 50 | kΩ |
| I_CC      | Supply current | See driver | | | |

(1) All typical values are at 25°C and with a 3.3-V supply.

## RECEIVER SWITCHING CHARACTERISTICS
over recommended operating conditions (unless otherwise noted)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|-----------|----------------|-----|-----|-----|------|
| t_PHL     | Propagation delay time, low-to-high-level output | 35 | 50 | ns |
| t_PHL     | Propagation delay time, high-to-low-level output | 35 | 50 | ns |
| t_skew    | Pulse skew (t_PHL + t_PHL) | See Figure 6 | 10 | ns |
| t_r       | Output signal rise time | See Figure 6 | 1.5 | ns |
| t_f       | Output signal fall time | See Figure 6 | 1.5 | ns |

## DEVICE SWITCHING CHARACTERISTICS
over recommended operating conditions (unless otherwise noted)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|-----------|----------------|-----|-----|-----|------|
| t_LOOP(1) | Total loop delay, driver input to receiver output, recessive to dominant | V_RS = 0 V, See Figure 9 <br> R_S with 10 kΩ to ground | 70 | 115 | ns |
|           | | R_S with 100 kΩ to ground, See Figure 9 | 535 | 920 | ns |
| t_LOOP(2) | Total loop delay, driver input to receiver output, dominant to recessive | V_RS = 0 V, See Figure 9 <br> R_S with 10 kΩ to ground | 100 | 135 | ns |
|           | | R_S with 100 kΩ to ground, See Figure 9 | 830 | 990 | ns |

---

© 2001–2011, Texas Instruments Incorporated

Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 9
---

```markdown
# DEVICE CONTROL-PIN CHARACTERISTICS

over recommended operating conditions (unless otherwise noted)

## PARAMETERS

| PARAMETER         | TEST CONDITIONS                                         | MIN   | TYP(1) | MAX   | UNIT  |
|-------------------|-------------------------------------------------------|-------|--------|-------|-------|
| t(WAKE)           | SN65HVD230 wake-up time from standby mode with R_s   | 0.55  | 1.5    |       | µs    |
|                   | SN65HVD231 wake-up time from sleep mode with R_s     | See Figure 8 | 3  | 5     | µs    |
| V_ref             | Reference output voltage                               | -5 µA < I(V_ref) < 5 µA | 0.45 V_CC | 0.55 V_CC | V     |
| I(RS)             | Input current for high-speed                          | V(RS) < 1 V | -450  | 0      | µA    |

(1) All typical values are at 25°C and with a 3.3-V supply.

## PARAMETER MEASUREMENT INFORMATION

### Figure 1. Driver Voltage and Current Definitions

```
       V_CC
         |
         I
         |
         D
         |
         V_OD
         |
         I
         |
         V_I
```

### Figure 2. Driver V_OD

```
       0 V
         |
         +---[60 Ω]---+
         |            |
         |            |
         +---[167 Ω]--+
         |            |
         |            |
         +---[167 Ω]--+
         |
         V_OD
```

### Figure 3. Driver Output Voltage Definitions

```
       CANH
       ┌───────────────┐
       │               │
       │               │
       │               │
       │               │
       │               │
       │               │
       └───────────────┘
       Dominant       Recessive
       = 3 V          = 2.3 V
       = 1 V
       CANL
```

© 2001–2011, Texas Instruments Incorporated

Product Folder Links: SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 10
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011

## PARAMETER MEASUREMENT INFORMATION (continued)

### Driver Test Circuit and Voltage Waveforms

```
Signal Generator (see Note A)
50 Ω
          ┌───────────────┐
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          └───────────────┘
          RL = 60 Ω
          CL = 50 pF
          V0
          (see Note B)
```

- **RS** = 0 Ω to 100 kΩ for SN65HVD230 and SN65HVD231  
- **N/A** for SN65HVD232

### Input and Output Timing

```
Input
          tPLH
          ────────
          │       │
          │       │
          │       │
          │       │
          │       │
          └───────┘
          Output
          tPHL
          ────────
          │       │
          │       │
          │       │
          │       │
          │       │
          └───────┘
```

- The input pulse is supplied by a generator having the following characteristics: PRR ≤ 500 kHz, 50% duty cycle, t ≤ 6 ns, Z0 = 50 Ω.
- **CL** includes probe and jig capacitance.

### Receiver Voltage and Current Definitions

```
V_IC = (V_CANH + V_CANL) / 2
```

```
          ┌───────────────┐
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          └───────────────┘
          V_CANH
```

```
          ┌───────────────┐
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          │               │
          └───────────────┘
          V_CANL
```

- **V_ID**: Voltage difference across the receiver.
- **I_O**: Output current.

---

**Submit Documentation Feedback**  
Product Folder Link(s): SN65HVD230, SN65HVD231, SN65HVD232

© 2001–2011, Texas Instruments Incorporated
```

---
# Page 11
---

```markdown
# PARAMETER MEASUREMENT INFORMATION (continued)

## Signal Generator Test Circuit

- **Signal Generator**: 50 Ω
- **Output Voltage**: 1.5 V

### Input and Output Characteristics

- **Input Pulse Characteristics**:
  - PRR ≤ 5 kHz
  - 50% Duty Cycle
  - t ≤ 6 ns
  - Z₀ = 50 Ω

- **Output Voltage Levels**:
  - V_OH = 2.9 V
  - V_OL = 1.3 V
  - V_IL = 1.5 V

### Timing Parameters

- **t_PLH**: Propagation delay time (Low to High)
- **t_PHL**: Propagation delay time (High to Low)

### Notes

A. The input pulse is supplied by a generator having the following characteristics: PRR ≤ 5 kHz, 50% duty cycle, t ≤ 6 ns, Z₀ = 50 Ω.  
B. C_L includes probe and jig capacitance.

## Figures

### Figure 6: Receiver Test Circuit and Voltage Waveforms

- **Components**:
  - Signal Generator
  - Output Load: 50 Ω
  - Capacitor: C_L = 15 pF

### Figure 7: Overvoltage Protection

- **Components**:
  - Pulse Generator: 15 µs Duration, 1% Duty Cycle
  - Resistor: 100 Ω
```


---
# Page 12
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011

### PARAMETER MEASUREMENT INFORMATION (continued)

#### Table 7. Receiver Characteristics Over Common Mode With \( V_{RS} = 1.2 \, V \)

| \( V_{IC} \) | \( V_{ID} \) | \( V_{CANH} \) | \( V_{CANL} \) | \( R \, OUTPUT \) |
|--------------|--------------|----------------|----------------|--------------------|
| -2 V         | 900 mV       | -1.55 V        | -2.45 V        | L                  |
| 7 V          | 900 mV       | 8.45 V         | 6.55 V         | L                  |
| 1 V          | 6 V          | 4 V            | -2 V           | L                  |
| -4 V         | 6 V          | 7 V            | -1 V           | L                  |
| -2 V         | 500 mV       | -1.75 V        | -2.25 V        | H                  |
| 7 V          | 500 mV       | 7.25 V         | 6.75 V         | H                  |
| 1 V          | -6 V         | -2 V           | 4 V            | H                  |
| 4 V          | -6 V         | 1 V            | 7 V            | H                  |
| X            | X            | Open           | Open           | H                  |

### Test Circuit and Voltage Waveforms

- **Generator Specifications:**
  - PRR = 150 kHz
  - 50% Duty Cycle
  - \( t_{r}, t_{f} < 5 \, ns \)
  - \( Z_0 = 50 \, \Omega \)

- **Circuit Components:**
  - \( R_S = 60 \, \Omega \)
  - \( C_L = 15 \, pF \)

#### Waveform Descriptions

- **\( V_{RS} \)**: Represents the voltage at the receiver side.
- **\( t_{WAKE} \)**: Time duration for the wake signal.
- **Output Levels**: 
  - \( V_{CC} = 1.5 \, V \)
  - 0 V and 1.3 V levels are indicated in the waveform.

### Product Folder Links
- SN65HVD230
- SN65HVD231
- SN65HVD232

© 2001–2011, Texas Instruments Incorporated
```

---
# Page 13
---

```markdown
# SN65HVD230 / SN65HVD231 / SN65HVD232
## SLOS346K - MARCH 2001 - REVISED FEBRUARY 2011

### Figure 9: t(LOOP) Test Circuit and Voltage Waveforms

A. All V_I input pulses are supplied by a generator having the following characteristics:  
   - t_r or t_f ≤ 6 ns, Pulse Repetition Rate (PRR) = 125 kHz, 50% duty cycle.

```
0 Ω, 10 kΩ or 100 kΩ ±5% R_S
```

```
V_I
DUT
CANH
CANL
V_O
```

- R = 60 Ω ±1%
- C = 15 pF ±20%

---

## TYPICAL CHARACTERISTICS

### SUPPLY CURRENT (RMS) vs FREQUENCY

```
I_CC - Supply Current (RMS) - mA
```

| Frequency - kbps |
|-------------------|
| 0                 |
| 250               |
| 500               |
| 750               |
| 1000              |

- V_CC = 3.3 V
- 60 Ω Load
- R_S at 0 V

### Figure 10

---

### LOGIC INPUT CURRENT (PIN D) vs INPUT VOLTAGE

```
I_I(D) - Logic Input Current - µA
```

| V_I - Input Voltage - V |
|--------------------------|
| 0.0                      |
| 0.6                      |
| 1.1                      |
| 1.6                      |
| 2.1                      |
| 2.6                      |
| 3.1                      |
| 3.6                      |

### Figure 11

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```


---
# Page 14
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## TYPICAL CHARACTERISTICS (continued)

### BUS INPUT CURRENT vs BUS INPUT VOLTAGE
- **I_I** = Bus Input Current (µA)
- **V_I** = Bus Input Voltage (V)

**Figure 12**

- **V_CC = 0 V**
- **V_CC = 3.6 V**

### DRIVER LOW-LEVEL OUTPUT CURRENT vs LOW-LEVEL OUTPUT VOLTAGE
- **I_O(L)** = Driver Low-Level Output Current (mA)
- **V_O(CANL)** = Low-Level Output Voltage (V)

**Figure 13**

### DRIVER HIGH-LEVEL OUTPUT CURRENT vs HIGH-LEVEL OUTPUT VOLTAGE
- **I_O(H)** = Driver High-Level Output Current (mA)
- **V_O(CANH)** = High-Level Output Voltage (V)

**Figure 14**

### DOMINANT VOLTAGE (V_D0) vs FREE-AIR TEMPERATURE
- **V_D0** = Dominant Voltage (V)
- **T_A** = Free-Air Temperature (°C)

**Figure 15**

- **V_CC = 3.6 V**
- **V_CC = 3.3 V**
- **V_CC = 3 V**

---

**Submit Documentation Feedback**

Product Folder Link(s): SN65HVD230, SN65HVD231, SN65HVD232

© 2001–2011, Texas Instruments Incorporated
```

---
# Page 15
---

```markdown
# TYPICAL CHARACTERISTICS (continued)

## RECEIVER LOW-TO-HIGH PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

| **T_A** - Free-Air Temperature - °C | **t_PHL** - Receiver Low-to-High Propagation Delay Time - ns |
|--------------------------------------|---------------------------------------------------------------|
| -55                                  | 31                                                            |
| -40                                  | 32                                                            |
| 0                                    | 33                                                            |
| 25                                   | 34                                                            |
| 70                                   | 36                                                            |
| 85                                   | 37                                                            |
| 125                                  | 38                                                            |

- **R_S = 0**
- **V_CC = 3 V**
- **V_CC = 3.3 V**
- **V_CC = 3.6 V**

**Figure 16**

---

## RECEIVER HIGH-TO-LOW PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

| **T_A** - Free-Air Temperature - °C | **t_PHL** - Receiver High-to-Low Propagation Delay Time - ns |
|--------------------------------------|---------------------------------------------------------------|
| -55                                  | 35                                                            |
| -40                                  | 36                                                            |
| 0                                    | 37                                                            |
| 25                                   | 38                                                            |
| 70                                   | 39                                                            |
| 85                                   | 39                                                            |
| 125                                  | 40                                                            |

- **R_S = 0**
- **V_CC = 3 V**
- **V_CC = 3.3 V**
- **V_CC = 3.6 V**

**Figure 17**

---

## DRIVER LOW-TO-HIGH PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

| **T_A** - Free-Air Temperature - °C | **t_PHL** - Driver Low-to-High Propagation Delay Time - ns |
|--------------------------------------|-------------------------------------------------------------|
| -55                                  | 10                                                          |
| -40                                  | 15                                                          |
| 0                                    | 20                                                          |
| 25                                   | 25                                                          |
| 70                                   | 35                                                          |
| 85                                   | 40                                                          |
| 125                                  | 45                                                          |

- **R_S = 0**
- **V_CC = 3 V**
- **V_CC = 3.3 V**
- **V_CC = 3.6 V**

**Figure 18**

---

## DRIVER HIGH-TO-LOW PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

| **T_A** - Free-Air Temperature - °C | **t_PHL** - Driver High-to-Low Propagation Delay Time - ns |
|--------------------------------------|------------------------------------------------------------|
| -55                                  | 80                                                         |
| -40                                  | 85                                                         |
| 0                                    | 87                                                         |
| 25                                   | 88                                                         |
| 70                                   | 89                                                         |
| 85                                   | 90                                                         |
| 125                                  | 90                                                         |

- **R_S = 0**
- **V_CC = 3 V**
- **V_CC = 3.3 V**
- **V_CC = 3.6 V**

**Figure 19**

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 16
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## SLOS346K - MARCH 2001 - REVISED FEBRUARY 2011

## TYPICAL CHARACTERISTICS (continued)

### DRIVER LOW-TO-HIGH PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

- **Parameters:**
  - \( R_S = 10 \, k\Omega \)
  - \( V_{CC} = 3 \, V \)
  - \( V_{CC} = 3.3 \, V \)
  - \( V_{CC} = 3.6 \, V \)

- **Graph Description:**
  - The graph plots the driver low-to-high propagation delay time (\( t_{PLH} \)) in milliseconds (ms) against the free-air temperature (\( T_A \)) in degrees Celsius (°C).
  - The x-axis represents the temperature range from -55°C to 125°C.
  - The y-axis represents the propagation delay time ranging from 0 ms to 90 ms.

### DRIVER HIGH-TO-LOW PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

- **Parameters:**
  - \( R_S = 10 \, k\Omega \)
  - \( V_{CC} = 3 \, V \)
  - \( V_{CC} = 3.3 \, V \)
  - \( V_{CC} = 3.6 \, V \)

- **Graph Description:**
  - The graph plots the driver high-to-low propagation delay time (\( t_{PHL} \)) in milliseconds (ms) against the free-air temperature (\( T_A \)) in degrees Celsius (°C).
  - The x-axis represents the temperature range from -55°C to 125°C.
  - The y-axis represents the propagation delay time ranging from 90 ms to 150 ms.

### DRIVER LOW-TO-HIGH PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

- **Parameters:**
  - \( R_S = 100 \, k\Omega \)
  - \( V_{CC} = 3 \, V \)
  - \( V_{CC} = 3.3 \, V \)
  - \( V_{CC} = 3.6 \, V \)

- **Graph Description:**
  - The graph plots the driver low-to-high propagation delay time (\( t_{PLH} \)) in milliseconds (ms) against the free-air temperature (\( T_A \)) in degrees Celsius (°C).
  - The x-axis represents the temperature range from -55°C to 125°C.
  - The y-axis represents the propagation delay time ranging from 0 ms to 800 ms.

### DRIVER HIGH-TO-LOW PROPAGATION DELAY TIME vs FREE-AIR TEMPERATURE

- **Parameters:**
  - \( R_S = 100 \, k\Omega \)
  - \( V_{CC} = 3 \, V \)
  - \( V_{CC} = 3.3 \, V \)
  - \( V_{CC} = 3.6 \, V \)

- **Graph Description:**
  - The graph plots the driver high-to-low propagation delay time (\( t_{PHL} \)) in milliseconds (ms) against the free-air temperature (\( T_A \)) in degrees Celsius (°C).
  - The x-axis represents the temperature range from -55°C to 125°C.
  - The y-axis represents the propagation delay time ranging from 750 ms to 1000 ms.

---

**Submit Documentation Feedback**

© 2001–2011, Texas Instruments Incorporated

**Product Folder Link(s):** SN65HVD230, SN65HVD231, SN65HVD232
```

---
# Page 17
---

```markdown
# TYPICAL CHARACTERISTICS (continued)

## DRIVER OUTPUT CURRENT vs SUPPLY VOLTAGE

- **I₀** = Driver Output Current (mA)
- **Vₗₗ** = Supply Voltage (V)

**Figure 24**: Graph showing the relationship between driver output current and supply voltage.

---

## DIFFERENTIAL DRIVER OUTPUT FALL TIME vs SOURCE RESISTANCE (Rₛ)

- **t₁** = Differential Driver Output Fall Time (µs)
- **Rₛ** = Source Resistance (kΩ)
- **Vₗₗ** values: 
  - Vₗₗ = 3.3 V
  - Vₗₗ = 3.6 V
  - Vₗₗ = 3 V

**Figure 25**: Graph illustrating the differential driver output fall time as a function of source resistance.

---

## REFERENCE VOLTAGE vs REFERENCE CURRENT

- **Vₗₗₑ** = Reference Voltage (V)
- **Iₗₑₗ** = Reference Current (µA)
- **Vₗₗ** values:
  - Vₗₗ = 3.6 V
  - Vₗₗ = 3 V

**Figure 26**: Graph depicting the reference voltage against reference current.

---

© 2001–2011, Texas Instruments Incorporated
```


---
# Page 18
---

```markdown
# SN65HVD230 SN65HVD231 SN65HVD232
## APPLICATION INFORMATION

This application provides information concerning the implementation of the physical medium attachment layer in a CAN network according to the ISO 11898 standard. It presents a typical application circuit and test results, as well as discussions on slope control, total loop delay, and interoperability in 5-V systems.

## INTRODUCTION

ISO 11898 is the international standard for high-speed serial communication using the controller area network (CAN) bus protocol. It supports multmaster operation, real-time control, programmable data rates up to 1 Mbps, and powerful redundant error checking procedures that provide reliable data transmission. It is suited for networking intelligent devices as well as sensors and actuators within the rugged electrical environment of a machine chassis or factory floor. The SN65HVD230 family of 3.3-V CAN transceivers implement the lowest layers of the ISO/OSI reference model. This is the interface with the physical signaling output of the CAN controller of the Texas Instruments TMS320Lx240x 3.3-V DSPs, as illustrated in Figure 27.

### ISO 11898 Specification

| Layer                     | Description                          |
|---------------------------|--------------------------------------|
| Application Specific Layer | Specific application requirements    |
| Data-Link Layer           | Logic Link Control                   |
| Medium Access Control     | Medium Access Control                |
| Physical Layer            | Physical Signaling                   |
| Physical Medium Attachment | Physical Medium Attachment            |
| Medium Dependent Interface | Interface for medium-dependent devices|

### Implementation

- **TMS320Lx2403/6/7 3.3-V DSP**
- **Embedded CAN Controller**
- **SN65HVD230**
- **CAN Bus-Line**

The SN65HVD230 family of CAN transceivers are compatible with the ISO 11898 standard; this ensures interoperability with other standard-compliant products.

## APPLICATION OF THE SN65HVD230

Figure 28 illustrates a typical application of the SN65HVD230 family. The output of a DSP's CAN controller is connected to the serial driver input, pin D, and receiver serial output, pin R, of the transceiver. The transceiver is then attached to the differential bus lines at pins CANH and CANL. Typically, the bus is a twisted pair of wires with a characteristic impedance of 120 Ω, in the standard half-duplex multipoint topology of Figure 29. Each end of the bus is terminated with 120-Ω resistors in compliance with the standard to minimize signal reflections on the bus.

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 19
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232

## Electronic Control Unit (ECU)

```
TMS320Lx2403/6/7
```
- **CAN-Controller**
  - **CANTX/IOPC6**
  - **CANRX/IOPC7**
  
```
D  R
SN65HVD230
```
- **CANH**
- **CANL**
- **CAN Bus Line**

### Figure 28. Details of a Typical CAN Node

---

### Figure 29. Typical CAN Network

---

## FEATURES OF THE SN65HVD230, SN65HVD231, and SN65HVD232

The SN65HVD230/231/232 3.3-V CAN transceivers provide the interface between the 3.3-V TMS320Lx2403/6/7 CAN DSPs and the differential bus line, and are designed to transmit data at signaling rates up to 1 Mbps as defined by the ISO 11898 standard.

These transceivers feature 3.3-V operation and standard compatibility with signaling rates up to 1 Mbps, and also offer:
- 16-kV HBM ESD protection on the bus pins
- Thermal shutdown protection
- Bus fault protection
- Open-circuit receiver fail-safe

The fail-safe design of the receiver assures a logic high at the receiver output if the bus wires become open-circuited. If a high ambient operating environment temperature or excessive output current result in thermal shutdown, the bus pins become high impedance, while the D and R pins default to a logic high.

The bus pins are also maintained in a high-impedance state during low V_CC conditions to ensure glitch-free power-up and power-down bus protection for hot-plugging applications. This high-impedance condition also means that an unpowered node does not disturb the bus. Transceivers without this feature usually have a very low output impedance. This results in a high current demand when the transceiver is unpowered, a condition that could affect the entire bus.

---

© 2001–2011, Texas Instruments Incorporated

Product Folder Links: SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 20
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232

## OPERATING MODES

RS (Pin 8) of the SN65HVD230 and SN65HVD231 provides for three different modes of operation: high-speed mode, slope-control mode, and low-power mode.

### High-Speed

The high-speed mode can be selected by applying a logic low to RS (pin 8). The high-speed mode of operation is commonly employed in industrial applications. High-speed allows the output to switch as fast as possible with no internal limitation on the output rise and fall slopes. The only limitations of the high-speed operation are cable length and radiated emission concerns, each of which is addressed by the slope control mode of operation.

If the low-power standby mode is to be employed in the circuit, direct connection to a DSP output pin can be used to switch between a logic-low level (< 1 V) for high-speed operation, and the logic-high level (> 0.75 VCC) for standby. 

**Figure 30** shows a typical DSP connection, and **Figure 31** shows the HVD230 driver output signal in high-speed mode on the CAN bus.

```
D   |  1  |  8  | RS
GND |  2  |  7  | CANH
VCC |  3  |  6  | CANL
R   |  4  |  5  | Vref
```

### Slope Control

Electromagnetic compatibility is essential in many applications using unshielded bus cable to reduce system cost. To reduce the electromagnetic interference generated by fast rise times and resulting harmonics, the rise and fall slopes of the SN65HVD230 and SN65HVD231 driver outputs can be adjusted by connecting a resistor.
```

This Markdown format maintains the structure and content of the original document while adhering to the specified guidelines.

---
# Page 21
---

```markdown
# SN65HVD230 / SN65HVD231 / SN65HVD232

## Slope Control/Standby Connection to a DSP

The slope of the driver output signal is proportional to the pin's output current. This slope control is implemented with an external resistor value of 10 kΩ to achieve a ±15 V/µs slew rate, and up to 100 kΩ to achieve a ±2.0 V/µs slew rate.

### Typical Driver Output Waveforms

Typical driver output waveforms from a pulse input signal with and without slope control are displayed below. A pulse input is used rather than NRZ data to clearly display the actual slew rate.

### Figure 32: Slope Control/Standby Connection to a DSP

```
D [1]  *  8  RS
GND [2]  7  CANH
VCC [3]  6  CANL
R [4]  5  Vref
```

### Figure 33: HVD230 Driver Output Signal Slope vs Slope Control Resistance Value

- **X-axis**: Slope Control Resistance (kΩ)
- **Y-axis**: Driver Output Signal Slope (V/µs)

| Resistance (kΩ) | Driver Output Signal Slope (V/µs) |
|------------------|-----------------------------------|
| 4.7              | 25                                |
| 6.8              | 20                                |
| 10               | 15                                |
| 15               | 10                                |
| 22               | 5                                 |
| 33               | 0                                 |
| 47               | 0                                 |
| 68               | 0                                 |
| 100              | 0                                 |

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```


---
# Page 22
---

```markdown
# SN65HVD230 SN65HVD231 SN65HVD232
## SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011

### Tek Run: 250MS/s Sample

#### Figure 34. Typical SN65HVD230 250-kbps Output Pulse Waveforms With Slope Control

---

### Standby Mode (Listen Only Mode) of the HVD230

If a logic high (≥ 0.75 Vcc) is applied to R_s (pin 8) in Figure 30 and Figure 32, the circuit of the SN65HVD230 enters a low-current, listen only standby mode, during which the driver is switched off and the receiver remains active. In its listen only state, the transceiver is completely passive to the bus. It makes no difference if a slope control resistor is in place as shown in Figure 32. The DSP can reverse this low-power standby mode by applying a rising edge of a dominant state (bus differential voltage > 900 mV typical) occurs on the bus. The DSP, sensing bus activity, reactivates the driver circuit by placing a logic low (< 1.2 V) on R_s (pin 8).

### The Babbling Idiot Protection of the HVD230

Occasionally, a runaway CAN controller unintentionally sends messages that completely tie up the bus (what is referred to in CAN jargon as a babbling idiot). When this occurs, the DSP can engage the listen-only standby mode to disengage the driver and release the bus, even when access to the CAN controller has been lost. When the driver circuit is deactivated, its outputs default to a high-impedance state.

### Sleep Mode of the HVD231

The unique difference between the SN65HVD230 and the SN65HVD231 is that both driver and receiver are switched off in the SN65HVD231 when a logic high is applied to R_s (pin 8). The device remains in a very low power-sleep mode until the circuit is reactivated with a logic low applied to R_s (pin 8). While in this sleep mode, the bus pins are in a high-impedance state, while the D and R pins default to a logic high.

### LOOP PROPAGATION DELAY

Transceiver loop delay is a measure of the overall device propagation delay, consisting of the delay from the driver input to the differential outputs, plus the delay from the receiver inputs to its output.

The loop delay of the transceiver displayed in Figure 35 increases accordingly when slope control is being used. This increased loop delay means that the total bus length must be reduced to meet the CAN bit-timing requirements of the overall system. The loop delay becomes ± 100 ns when employing slope control with a 10-kΩ resistor, and ≈ 500 ns with a 100-kΩ resistor. Therefore, considering that the rule-of-thumb propagation
```


---
# Page 23
---

```markdown
# SN65HVD230 SN65HVD231 SN65HVD232

## Delay Characteristics

The delay of a typical bus cable is 5 ns/m. Slope control with the 100-kΩ resistor decreases the allowable bus length by the difference between the 500-ns max loop delay and the loop delay with no slope control, 70.7 ns. This equates to (500 - 70.7 ns) / 5 ns, or approximately 86 m less bus length. This slew-rate/bus length trade-off to reduce electromagnetic interference to adjoining circuits from the bus can also be solved with a quality shielded bus cable.

### Tek Illum: 2.0065/s Li Sample

- **Driver Input**: 2+
- **Receiver Output**: 1
- **Loop Delay**: 70.7 ns
- **Measurement**: 61.5 ns

## ISO 11898 Compliance of SN65HVD230 Family of 3.3-V CAN Transceivers

### Introduction

Many users value the low power consumption of operating their CAN transceivers from a 3.3 V supply. However, some are concerned about the interoperability with 5-V supplied transceivers on the same bus. This report analyzes this situation to address those concerns.

### Differential Signal

CAN is a differential bus where complementary signals are sent over two wires, and the voltage difference between the two wires defines the logical state of the bus. The differential CAN receiver monitors this voltage difference and outputs the bus state with a single-ended output signal.
```


---
# Page 24
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011

### Typical SN65HVD230 Differential Output Voltage Waveform

The CAN driver creates the difference voltage between CANH and CANL in the dominant state. The dominant differential output of the SN65HVD230 is greater than 1.5 V and less than 3 V across a 60-ohm load. The minimum required by ISO 11898 is 1.5 V and maximum is 3 V. These are the same limiting values for 5 V supplied CAN transceivers. The bus termination resistors drive the recessive bus state and not the CAN driver.

A CAN receiver is required to output a recessive state with less than 500 mV and a dominant state with more than 900 mV difference voltage on its bus inputs. The CAN receiver must do this with common-mode input voltages from -2 V to 7 volts. The SN65HVD230 family receivers meet these same input specifications as 5-V supplied receivers.

### Common-Mode Signal

A common-mode signal is an average voltage of the two signal wires that the differential receiver rejects. The common-mode signal comes from the CAN driver, ground noise, and coupled bus noise. Obviously, the supply voltage of the CAN transceiver has nothing to do with noise. The SN65HVD230 family driver lowers the common-mode output in a dominant bit by a couple hundred millivolts from that of most 5-V drivers. While this does not fully comply with ISO 11898, this small variation in the driver common-mode output is rejected by differential receivers and does not affect data, signal noise margins or error rates.

### Interoperability of 3.3-V CAN in 5-V CAN Systems

The 3.3-V supplied SN65HVD230 family of CAN transceivers are electrically interchangeable with 5-V CAN transceivers. The differential output is the same. The recessive common-mode output is the same. The dominant common-mode output voltage is a couple hundred millivolts lower than 5-V supplied drivers, while the receivers exhibit identical specifications as 5-V devices.

Electrical interoperability does not assure interchangeability, however. Most implementers of CAN buses recognize that ISO 11898 does not sufficiently specify the electrical layer and that standard compliance alone does not ensure interchangeability. This comes only with thorough equipment testing.
```


---
# Page 25
---

```markdown
# SN65HVD230, SN65HVD231, SN65HVD232
## SLOS346K - MARCH 2001 - REVISED FEBRUARY 2011

### Figure 37. 3.3-V and 5-V CAN Transceiver System

```
Bus Lines → 40 m max
Stub Lines → 0.3 m max
```

- **V_ref**: Reference Voltage
- **R_s**: Termination Resistor
- **C**: Capacitor (0.1 µF)
- **GND**: Ground

#### Components:
- **SN65HVD251**
  - V_CC: 5 V
  - CAN_TX: TMS320LF243
  - CAN_RX: TMS320LF243
  - Sensor, Actuator, or Control Equipment

- **SN65HVD230**
  - V_CC: 3.3 V
  - CAN_TX: TMS320LF2407A
  - CAN_RX: TMS320LF2407A
  - Sensor, Actuator, or Control Equipment

### Figure 38. 3.3-V and 5-V CAN Transceiver System Testing

#### Setup Description:
- **TEKTRONIX HFS-9003**: Pattern Generator
- **TEKTRONIX P6243**: Single-Ended Probes
- **TEKTRONIX 784D**: Oscilloscope
- **One Meter Belden Cable #3105A**
- **HP E3616A**: 3.3-V Power Supply
- **HP E3516A**: 5-V Power Supply
- **Competitor X251**

```
Bus Lines → 40 m max
Stub Lines → 0.3 m max
```

### Notes:
- All components are connected with 120 Ω termination resistors.
- Ensure proper grounding and voltage levels for optimal performance.

---

© 2001–2011, Texas Instruments Incorporated  
Product Folder Links: SN65HVD230, SN65HVD231, SN65HVD232
```

---
# Page 26
---

```markdown
# SN65HVD230 SN65HVD231 SN65HVD232
## SLOS346K – MARCH 2001 – REVISED FEBRUARY 2011
### www.ti.com

## REVISION HISTORY

### Changes from Revision I (October 2007) to Revision J

- Deleted Low-to-High Propagation Delay Time vs Common-Mode Input Voltage Characteristics ........................................... Page 17
- Deleted Driver Schematic Diagram ................................................................................................................................... Page 17
- Added Figure 37 .................................................................................................................................................................. Page 25
- Added Figure 38 .................................................................................................................................................................. Page 25

### Changes from Revision J (January 2009) to Revision K

- Replaced the DISSIPATION RATING TABLE with the Thermal Information table ................................................................. Page 6

---

26 Submit Documentation Feedback

© 2001–2011, Texas Instruments Incorporated

Product Folder Link(s): SN65HVD230 SN65HVD231 SN65HVD232
```

---
# Page 27
---

```markdown
# PACKAGE OPTION ADDENDUM

**Date:** 19-Jan-2011

## PACKAGING INFORMATION

| Orderable Device   | Status (1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan (2)         | Lead/ Ball Finish         | MSL Peak Temp (3) | Samples (Requires Login)     |
|--------------------|------------|--------------|------------------|------|-------------|-----------------------|---------------------------|-------------------|-------------------------------|
| SN65HVD230D        | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD230D4       | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD230DR       | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD230DRG4     | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD231D        | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD231D4       | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD231DR       | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD231DRG4     | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD232D        | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD232D4       | ACTIVE     | SOIC         | D                | 8    | 75          | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Request Free Samples  |
| SN65HVD232DR       | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD232DRG4     | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |
| SN65HVD232DRG4     | ACTIVE     | SOIC         | D                | 8    | 2500        | Green (RoHS & no Sb/Br)| CU NIPDAU Level-1-260C-UNLIM | Purchase Samples     |

### Notes:
1. **Status Definitions:**
   - **ACTIVE:** Product device recommended for new designs.
   - **LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
   - **NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
   - **PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
   - **OBSOLETE:** TI has discontinued the production of the device.

2. **Eco Plan:** The planned eco-friendliness classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS & no Sb/Br) - please check [TI Product Content](http://www.ti.com/productcontent) for the latest availability information and additional product content details.

3. **TBD:** The Pb-Free/Green conversion plan has not been defined.

---

Addendum-Page 1
```

---
# Page 28
---

```markdown
# PACKAGE OPTION ADDENDUM

**Texas Instruments**  
19-Jan-2011  
www.ti.com

## Pb-Free (RoHS)

TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS requirements for all 6 substances, including the requirement that lead not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified lead-free processes.

### Pb-Free (RoHS Exempt)

This component has a RoHS exemption for either:
1. Lead-based flip chip solder bumps used between the die and package, or
2. Lead-based die adhesive used between the die and leadframe.

The component is otherwise considered Pb-Free (RoHS compatible) as defined above.

### Green (RoHS & no SbBr)

TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb) based flame retardants (Br or Sb do not exceed 0.1% by weight in homogeneous material).

### MSL, Peak Temp

MSL, Peak Temp. -- The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

## Important Information and Disclaimer

The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.
```


---
# Page 29
---

```markdown
# PACKAGE MATERIALS INFORMATION
**Date:** 18-Jan-2011  
**Website:** www.ti.com

## TAPE AND REEL INFORMATION

### REEL DIMENSIONS
- **Reel Diameter:** [Dimension not specified]

### TAPE DIMENSIONS
- **Cavity Dimensions:**
  - **A0:** Dimension designed to accommodate the component width
  - **B0:** Dimension designed to accommodate the component length
  - **K0:** Dimension designed to accommodate the component thickness
  - **W:** Overall width of the carrier tape
  - **P1:** Pitch between successive cavity centers

### QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
- **Sprocket Holes**
- **User Direction of Feed**
- **Pocket Quadrants:**
  - Q1 | Q2 | Q1 | Q2
  - Q3 | Q4 | Q3 | Q4

### TABLE OF DEVICE SPECIFICATIONS

| Device          | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
|-----------------|--------------|------------------|------|-----|---------------------|---------------------|---------|---------|---------|---------|---------|----------------|
| SN65HVD230DR    | SOIC         | D                | 8    | 2500| 330.0               | 12.4                | 6.4     | 5.2     | 2.1     | 8.0     | 12.0    | Q1             |
| SN65HVD231DR    | SOIC         | D                | 8    | 2500| 330.0               | 12.4                | 6.4     | 5.2     | 2.1     | 8.0     | 12.0    | Q1             |
| SN65HVD232DR    | SOIC         | D                | 8    | 2500| 330.0               | 12.4                | 6.4     | 5.2     | 2.1     | 8.0     | 12.0    | Q1             |

> **Note:** All dimensions are nominal.
```

---
# Page 30
---

```markdown
# PACKAGE MATERIALS INFORMATION
**Date:** 18-Jan-2011  
**Source:** www.ti.com

## TAPE AND REEL BOX DIMENSIONS

*All dimensions are nominal*

### Device Specifications

| Device         | Package Type | Package Drawing | Pins | SPQ  | Length (mm) | Width (mm) | Height (mm) |
|----------------|--------------|-----------------|------|------|-------------|------------|--------------|
| SN65HVD230DR   | SOIC         | D               | 8    | 2500 | 340.5       | 338.1      | 20.6         |
| SN65HVD231DR   | SOIC         | D               | 8    | 2500 | 340.5       | 338.1      | 20.6         |
| SN65HVD232DR   | SOIC         | D               | 8    | 2500 | 340.5       | 338.1      | 20.6         |

### Diagram Description
The diagram illustrates a tape and reel box with labeled dimensions: 
- **L** (Length)
- **W** (Width)
- **H** (Height)

The box is designed to hold electronic components securely during transport and storage.
```

---
# Page 31
---

```markdown
# MECHANICAL DATA

## D (R-PDSO-G8) 
### PLASTIC SMALL OUTLINE

### Dimensions
- All linear dimensions are in inches (millimeters).

| Dimension | Value (inches) | Value (mm) |
|-----------|----------------|-------------|
| A         | 0.197          | 5.00        |
| B         | 0.189          | 4.80        |
| C         | 0.244          | 6.20        |
| D         | 0.228          | 5.80        |
| E         | 0.157          | 4.00        |
| F         | 0.150          | 3.80        |
| G         | 0.050          | 1.27        |
| H         | 0.020          | 0.51        |
| I         | 0.012          | 0.31        |
| J         | 0.010          | 0.25        |
| K         | 0.069 Max      | 1.75        |
| L         | 0.010          | 0.25        |
| M         | 0.005          | 0.13        |
| N         | 0.004          | 0.10        |

### Notes
- This drawing is subject to change without notice.
- Body length does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.006 (0.15) each side.
- Body width does not include interlead flash. Interlead flash shall not exceed 0.017 (0.43) each side.
- Reference JEDEC MS-012 variation AA.

### Diagram Description
The diagram illustrates the plastic small outline package (D (R-PDSO-G8)). It includes:
- A top view showing the pin configuration and dimensions.
- A side view indicating the seating plane and gauge plane.
- Various dimensions labeled with their respective values in both inches and millimeters.

### Manufacturer
Texas Instruments  
[www.ti.com](http://www.ti.com)
```


---
# Page 32
---

```markdown
# LAND PATTERN DATA

## D (R-PDSO-G8) PLASTIC SMALL OUTLINE

### Example Board Layout (Note C)

```
6 x 1.27
```

```
8 x 1.95
```

```
4.80
```

### Stencil Openings (Note D)

```
8 x 0.55
```

```
6 x 1.27
```

```
8 x 1.95
```

```
4.80
```

### Example Non Soldermask Defined Pad

```
       0.60
  +-------------+
  |             |
  |             |
  |             |
  |             |
  +-------------+
       2.00
```

### Example Pad Geometry (See Note C)

### Example Solder Mask Opening (See Note E)

```
       0.07
  +-------------+
  |             |
  |             |
  |             |
  |             |
  +-------------+
```

### NOTES:
- A. All linear dimensions are in millimeters.
- B. This drawing is subject to change without notice.
- C. Publication IPC–7351 is recommended for alternate designs.
- D. Laser cutting apertures with trapezoidal walls and also rounding corners will offer better paste release. Customers should contact their board assembly site for stencil design recommendations. Refer to IPC–7525 for other stencil recommendations.
- E. Customers should contact their board fabrication site for solder mask tolerances between and around signal pads.

---

**Texas Instruments**  
**www.ti.com**
```

---
# Page 33
---

```markdown
# IMPORTANT NOTICE

Texas Instruments Incorporated and its subsidiaries (TI) reserve the right to make corrections, modifications, enhancements, improvements, and other changes to its products and services at any time and to discontinue any product or service without notice. Customers should obtain the latest relevant information before placing orders and should verify that such information is current and complete. All products are sold subject to TI's terms and conditions of sale supplied at the time of order acknowledgment.

TI warrants performance of its hardware products to the specifications applicable at the time of sale in accordance with TI's standard warranty. Testing and other quality control techniques are used to the extent TI deems necessary to support this warranty. Except where mandated by government requirements, testing of all parameters of each product is not necessarily performed.

TI assumes no liability for applications assistance or customer product design. Customers are responsible for their products and applications using TI products. To minimize the risks associated with customer products and applications, customers should provide adequate design and operating safeguards.

TI does not warrant or represent that any license, either express or implied, is granted under any TI patent, copyright, mask work right, or other TI intellectual property right relating to any combination, machine, or process in which TI products or services are used. Information published by TI regarding third-party products or services does not constitute a license from TI to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property of the third party, or a license from TI under the patents or other intellectual property of TI.

Reproduction of TI information in data books or data sheets is permissible only if reproduction is without alteration and is accompanied by all associated warranties, conditions, limitations, and notices. Reproduction of this information with alteration is an infringement of TI's business practice. TI is not responsible or liable for such altered documentation. Information of third parties may be subject to additional restrictions.

Resale of TI products or services with statements different from or beyond the parameters stated by TI for that product or service voids all express and implied warranties for the associated TI product or service and is an unfair and deceptive business practice. TI is not responsible for any such statements.

TI products are not authorized for use in safety-critical applications (such as life support) where a failure of the TI product would reasonably be expected to cause severe personal injury or death, unless the parties have executed an agreement specifically governing such use. Buyers represent that they have all necessary expertise in the safety and regulatory ramifications of their applications, and acknowledge and agree that they are solely responsible for all legal, regulatory and safety-related requirements concerning their products and any use of TI products in such safety-critical applications, notwithstanding any applications-related information or support that may be provided by TI. Further, Buyers must fully indemnify TI and its representatives against any damages arising out of the use of TI products in such safety-critical applications.

TI products are neither designed nor intended for use in automotive applications or environments unless the specific TI products are designated by TI as military-grade or "enhanced plastic." Only products designated by TI as military-grade meet military specifications. Buyers acknowledge and agree that any such TI products which TI has not designated as military-grade is solely at the buyer's risk, and that they are solely responsible for compliance with all legal and regulatory requirements in connection with such use.

Following are URLs where you can obtain information on other Texas Instruments products and application solutions:

| Products              | URL                          | Applications                     | URL                               |
|-----------------------|------------------------------|----------------------------------|-----------------------------------|
| Audio                 | www.ti.com/audio             | Communications and Telecom       | www.ti.com/communications         |
| Amplifiers            | amplifier.ti.com             | Computers and Peripherals        | www.ti.com/computers             |
| Data Converters       | dataconverter.ti.com         | Consumer Electronics             | www.ti.com/consumer-apps          |
| DLP® Products         | www.dlp.com                  | Energy and Lighting              | www.ti.com/energy                 |
| DSP                   | dsp.ti.com                   | Industrial                       | www.ti.com/industrial             |
| Clocks and Timers     | www.ti.com/clocks            | Medical                          | www.ti.com/medical                |
| Interface             | interface.ti.com             | Security                         | www.ti.com/security               |
| Logic                 | logic.ti.com                 | Space, Avionics and Defense     | www.ti.com/space-avionics-defense |
| Power Mgmt            | power.ti.com                 | Transportation                   | www.ti.com/automotive             |
| Microcontrollers      | microcontroller.ti.com       | Automotive                       | www.ti.com/video                  |
| RFID                  | www.ti-rfid.com              | Wireless                         | www.ti.com/wireless-apps          |
| RF/IFF and ZigBee® Solutions | www.ti.com/prf        |                                  |                                   |

## TI E2E Community Home Page
[e2e.ti.com](http://e2e.ti.com)

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265  
Copyright © 2011, Texas Instruments Incorporated
```

---



---

# Can Sp3481 Sp3485 {#can-sp3481_sp3485}

---
# Page 1
---

```markdown
# SP3481/SP3485

## +3.3V Low Power Half-Duplex RS-485 Transceivers with 10Mbps Data Rate

- **RS-485 and RS-422 Transceivers**
- Operates from a single +3.3V supply
- Interoperable with +5.0V logic
- Driver/Receiver Enable
- Low Power Shutdown Mode (SP3481)
- -7V to +12V Common-Mode Input Voltage Range
- Allows up to 32 transceivers on the serial bus
- Compatibility with the industry standard 75176 pinout
- Driver Output Short-Circuit Protection

## DESCRIPTION

The **SP3481** and **SP3485** are a family of +3.3V low power half-duplex transceivers that meet the specifications of the RS-485 and RS-422 serial protocols. These devices are pin-to-pin compatible with the Sipex SP481, SP483, and SP485 devices as well as popular industry standards. The SP3481 and SP3485 feature Sipex's BiCMOS process, allowing low power operation without sacrificing performance. The SP3481 and SP3485 meet the electrical specifications of RS-485 and RS-422 serial protocols up to 10Mbps under load. The SP3481 is equipped with a low power Shutdown mode.

## PIN CONFIGURATION

```
   SP3481 and SP3485
   -------------------
   RO  1  | R
   RE  2  | 
   DE  3  | D
   DI  4  |
          8  Vcc
          7  B
          6  A
          5  GND
```

## SPECIFICATIONS

- **Supply Voltage (Vcc)**: +3.3V
- **Data Rate**: Up to 10Mbps
- **Common-Mode Input Voltage Range**: -7V to +12V
- **Shutdown Mode**: Available in SP3481

---

*© Copyright 2002 Sipex Corporation*
```

---
# Page 2
---

```markdown
# ABSOLUTE MAXIMUM RATINGS

These are stress ratings only and functional operation of the device at these ratings or any other above those indicated in the operation sections of the specifications below is not implied. Exposure to absolute maximum rating conditions for extended periods of time may affect reliability.

- **V_CC**: +6.0V
- **Input Voltages**
  - Logic: -0.3V to +6.0V
  - Drivers: -0.3V to +6.0V
  - Receivers: -0.3V to +6.0V
- **Output Voltages**
  - Drivers: -15V
  - Receivers: -0.3V to +6.0V
- **Storage Temperature**: -65°C to +150°C
- **Power Dissipation per Package**
  - 8-pin NSOIC (derate 6.90mW/°C above +70°C): 600mW
  - 8-pin PDIP (derate 11.8mW/°C above +70°C): 100mW

---

# SPECIFICATIONS

**T_AMB = T_MAX and V_CC = +3.3V ± 5% unless otherwise noted.**

## PARAMETERS

| **PARAMETERS**                             | **MIN.** | **TYP.** | **MAX.** | **UNITS** | **CONDITIONS**                                   |
|--------------------------------------------|----------|----------|----------|-----------|--------------------------------------------------|
| **SP3481/SP3485 DRIVER**                   |          |          |          |           |                                                  |
| DC Characteristics                         |          |          |          |           |                                                  |
| Differential Output Voltage                | GND     | 2        |          | Volts     | V_CC Unloaded; R = ∞; Figure 1                    |
| Differential Output Voltage                |          | 1.5      |          | Volts     | V_CC with load; R = 50Ω; (RS-422); Figure 1      |
| Differential Output Voltage                |          | 0.2      |          | Volts     | V_CC = 27Ω or R = 50Ω; Figure 1                  |
| Input High Voltage                         | 2.0      |          |          | Volts     | Applies to DE, DI, RE                             |
| Input Low Voltage                          | 0.8      | ±10      |          | µA       | Applies to DE, DI, RE                             |
| Driver Short-Circuit Current               |          | ±250     |          | mA       | V_OUT = HIGH                                     |
|                                            |          | ±250     |          | mA       | V_OUT = LOW                                      |

## AC Characteristics

| **PARAMETERS**                             | **MIN.** | **TYP.** | **MAX.** | **UNITS** | **CONDITIONS**                                   |
|--------------------------------------------|----------|----------|----------|-----------|--------------------------------------------------|
| Maximum Data Rate                          | 10       |          |          | Mbps      | RE = V_CC; DE = V_CC                             |
| Driver Input to Output, t_PLH              | 20       | 40       | 60       | ns        | Figures 2 and 8                                  |
| Driver Input to Output, t_PHL              | 20       | 40       | 60       | ns        | Figures 2 and 8                                  |
| Differential Driver Skew                   | 2        | 10       |          | ns        | t_P1 - t_P2; Figures 2 and 9                     |
| Driver Rise or Fall Time                   | 5        | 20       |          | ns        | From 10% to 90%; Figures 3 and 9                  |
| Driver Enable to Output High               | 52       | 120      |          | ns        | Figures 4 and 10                                 |
| Driver Enable to Output Low                | 60       | 120      |          | ns        | Figures 5 and 10                                 |
| Driver Disable Time from High              | 40       | 120      |          | ns        | Figures 5 and 10                                 |
| Driver Disable Time from Low               | 60       | 120      |          | ns        | Figures 4 and 10                                 |

## SP3481/SP3485 RECEIVER

### DC Characteristics

| **PARAMETERS**                             | **MIN.** | **TYP.** | **MAX.** | **UNITS** | **CONDITIONS**                                   |
|--------------------------------------------|----------|----------|----------|-----------|--------------------------------------------------|
| Differential Input Threshold                | -0.2     | +0.2     |          | Volts     | -7V ≤ V_CM ≤ +12V                                |
| Input Hysteresis                           |          | 20       |          | mV        | V_CM = 0V                                       |
| Output Voltage High                        | 0.4      |          |          | Volts     | V_ID = +200mV, -1.5mA                           |
| Output Voltage Low                         |          |          | 0.4      | Volts     | V_ID = -200mV, 2.5mA                            |
| Three-State (High Impedance)              |          |          |          |           |                                                  |
| Output Current                             | 12       | 15       | ±1       | µA        | 0V ≤ V_S ≤ V_CC; RE = V_CC                      |
| Input Resistance                           |          | 1.0      |          | kΩ        | -7V ≤ V_S ≤ +12V                                |
| Input Current (A, B); V_IN = 12V         | -0.8     |          |          | mA        | DE = 0V; V_CC = 0V or 3.6V, V_IN = 12V         |
| Input Current (A, B); V_IN = -7V         | 7        | 60       |          | mA        | DE = 0V; V_CC = 0V or 3.6V, V_IN = -7V         |

---

*10/15/02 SP3481/3485 Low Power Half-Duplex RS485 Transceivers © Copyright 2000 Sipex Corporation*
```

---
# Page 3
---

```markdown
# SPECIFICATIONS (continued)

T_AMB = T_AMB0, T_AW0, and V_CC = +3.3V ± 5% unless otherwise noted.

## PARAMETERS

### SP3481/SP3485 RECEIVER

#### AC Characteristics

| Parameter                          | MIN | TYP | MAX | UNITS | CONDITIONS                              |
|------------------------------------|-----|-----|-----|-------|-----------------------------------------|
| Maximum Data Rate                  | 10  | 40  | 70  | Mbps  | RE = 0V, DE = 0V                        |
| Receiver Input to Output, t_PLH    | 40  | 70  | 100 | ns    | Figures 6 and 11                        |
| Receiver Input to Output, t_PHL    | 40  | 70  | 100 | ns    | T_AMB = +25°C, V_CC = +3.3V, Figures 6 and 11 |
| Differential Receiver Skew         | 4   |     |     | ns    | t_SKEW = t_RPLH - t_RPHL, Figures 6 and 11 |
| Receiver Enable to Output Low      | 35  | 60  |     | ns    | Figures 7 and 12; S1 closed, S2 open   |
| Receiver Enable to Output High     | 35  | 60  |     | ns    | Figures 7 and 12; S2 closed, S1 open   |
| Receiver Disable from Low          | 35  | 60  |     | ns    | Figures 7 and 12; S2 closed, S1 open   |
| Receiver Disable from High         | 35  | 60  |     | ns    | Figures 7 and 12; S2 closed, S1 open   |

### SP3481 Shutdown Timing

| Parameter                          | MIN | TYP | MAX | UNITS | CONDITIONS                              |
|------------------------------------|-----|-----|-----|-------|-----------------------------------------|
| Time to Shutdown                   | 50  | 75  | 200 | ns    | RE = 3.3V, DE = 0V                      |
| Driver Enable from Shutdown to Output High | 65  | 150 | 200 | ns    | Figures 4 and 10                        |
| Driver Enable from Shutdown to Output Low  | 65  | 150 | 200 | ns    | Figures 5 and 10                        |
| Receiver Enable from Shutdown to Output High | 50  | 200 |     | ns    | Figures 7 and 12; S2 closed, S1 open   |
| Receiver Enable from Shutdown to Output Low  | 50  | 200 |     | ns    | Figures 7 and 12; S1 closed, S2 open   |

### POWER REQUIREMENTS

| Parameter                          | MIN  | TYP  | MAX  | UNITS | CONDITIONS                              |
|------------------------------------|------|------|------|-------|-----------------------------------------|
| Supply Current SP3481/3485 No Load | 1000 | 2000 | 1500 | µA    | RE = 0V, DI = 0V or V_CC; DE = V_CC; RE = 0V, DI = 0V or V_CC; DE = 0V |
| SP3481 Shutdown Mode               | 10   |      |      | µA    | DE = 0V, RE = V_CC                     |

© Copyright 2002 Sipex Corporation
```


---
# Page 4
---

```markdown
# SP3481/SP3485 Low Power Half-Duplex RS485 Transceivers

## Pinout (Top View)

```
        RO  1  VCC
        RE  2  B
        DE  3  A
        DI  4  GND
```

## PIN FUNCTION

- **Pin 1** - RO – Receiver Output.
- **Pin 2** - RE – Receiver Output Enable Active LOW.
- **Pin 3** - DE – Driver Output Enable Active HIGH.
- **Pin 4** - DI – Driver Input.
- **Pin 5** - GND – Ground Connection.
- **Pin 6** - A – Driver Output/Receiver Input Non-inverting.
- **Pin 7** - B – Driver Output/Receiver Input Inverting.
- **Pin 8** - VCC

## DESCRIPTION

The **SP3481** and **SP3485** are 2 members in the family of +3.3V low power half-duplex transceivers that meet the specifications of the RS-485 and RS-422 serial protocols. These devices are pin-to-pin compatible with the Sipex SP481, SP483, and SP485 devices as well as popular industry standards. The **SP3481** and **SP3485** feature Sipex's BiCMOS process allowing low power operation without sacrificing performance.

## Drivers

The driver outputs of the **SP3481** and **SP3485** are differential outputs meeting the RS-485 and RS-422 standards. The typical voltage output swing with no load will be 0 Volts to +3.3 Volts. With a load of 54Ω across the differential outputs, the drivers maintain greater than 1.5V voltage levels. The drivers of the **SP3481** and **SP3485** have an enable control line which is active HIGH. A logic HIGH on DE (pin 3) will enable the differential driver outputs. A logic LOW on DE (pin 3) will tri-state the driver outputs.

The transceivers in the **SP3481** and **SP3485** operate up to 10Mbps. The 250mA I_SC maximum limit on the driver output allows the **SP3481** and **SP3485** to withstand an infinite short circuit over the -7.0V to +12.0V common mode range without catastrophic damage to the IC.

## Receivers

The **SP3481** and **SP3485** receivers have differential inputs with an input sensitivity as low as ±200mV. Input impedance of the receivers is typically 15kΩ (12kΩ minimum). A wide common mode range of -7V to +12V allows for large ground potential differences between systems. The receivers of the **SP3481** and **SP3485** have a tri-state enable control pin. A logic LOW on RE (pin 2) will enable the receiver; a logic HIGH on RE (pin 2) will disable the receiver.

The receivers of the **SP3481** and **SP3485** operate up to 10Mbps. The receiver for each of the three devices is equipped with fail-safe. Fail-safe guarantees that the receiver output will be in a HIGH state when it is left unconnected.

## Shutdown Mode for the SP3481

The **SP3481** is equipped with a Shutdown mode. To enable the Shutdown state, both the driver and receiver must be disabled simultaneously. A logic LOW on DE (pin 3) and a logic HIGH on RE (pin 2) will put the **SP3481** into Shutdown mode. In Shutdown, supply current will drop to typical 1µA, 10µA maximum.
```

---
# Page 5
---

```markdown
# SP3481/3485 Low Power Half-Duplex RS485 Transceivers

## Figure 1. Driver DC Test Load Circuit
```
```
          VDD
           |
           R
           |
           D
           |
          VCC
```

## Figure 2. Driver Propagation Delay Test Circuit
```
          VOM
           |
           Rl = 27Ω
           |
           OUT
           |
           S1
           |
          VCC
```

## Figure 3. Driver Differential Output Delay and Transition Time Circuit
```
          VCC
           |
           D
           |
          OUT
           |
          Rl = 602Ω
           |
          C1 = 15pF (NOTE 2)
```

## Figure 4. Driver Enable and Disable Timing Circuit, Output HIGH
```
          VOM = (VCC + VDD) / 2 = 1.5V
           |
           D
           |
          OUT
           |
           S1
           |
          Rl = 110Ω
```

## Figure 5. Driver Enable and Disable Timing Circuit, Output LOW
```
          0V or 3V
           |
           S1
           |
          OUT
           |
          Rl = 110Ω
```

## Figure 6. Receiver Propagation Delay Test Circuit
```
          VOM = VCC / 2
           |
           OUT
           |
           R
```

## Figure 7. Receiver Enable and Disable Timing Circuit
```
          V0
           |
           S3
           |
          VCC
           |
           S1
           |
          Rl
           |
          C1 = 0.1µF (NOTE 5)
```

## Table 1. Transmit Function Truth Table

| RE | DE | DI | LINE CONDITION | B | A |
|----|----|----|----------------|---|---|
| X  | 1  | 1  | No Fault       | 0 | 1 |
| X  | 1  | 0  | No Fault       | 1 | 0 |
| X  | 0  | X  | Z              | Z | Z |

## Table 2. Receive Function Truth Table

| RE | DE | A - B | R |
|----|----|--------|---|
| 0  | 0  | +0.2V  | 1 |
| 0  | 0  | -0.2V  | 0 |
| 0  | 0  | Inputs Open | 1 |
| 1  | 0  | X      | Z |
```


---
# Page 6
---

```markdown
# Driver and Receiver Waveforms

## Figure 8: Driver Propagation Delay Waveforms

- **Input Voltage Levels:**
  - High: 3V
  - Low: 0V
  - Intermediate: 1.5V

- **Output Voltage Levels:**
  - Y Output: \( V_{OM} \)
  - Z Output: \( V_{OM} \)
  - \( V_{OM} = \frac{V_{OH} + V_{OL}}{2} - 1.5V \)

## Figure 9: Driver Differential Output Delay and Transition Time Waveforms

- **Input Voltage Levels:**
  - High: 3V
  - Low: 0V
  - Intermediate: 1.5V

- **Output Voltage Levels:**
  - \( V_{OUT} \)
  - Transition times: \( t_{DO} \) and \( t_{TO} \)

## Figure 10: Driver Enable and Disable Timing Waveforms

- **Input Voltage Levels:**
  - High: 3V
  - Low: 0V
  - Intermediate: 1.5V

- **Output Voltage Levels:**
  - High: \( V_{OH} \)
  - Low: \( V_{OL} \)
  - Transition times: \( t_{EN} \) and \( t_{DIS} \)

## Figure 11: Receiver Propagation Delay Waveforms

- **Input Voltage Levels:**
  - High: 3V
  - Low: 0V
  - Intermediate: 1.5V

- **Output Voltage Levels:**
  - \( V_{OM} = \frac{V_{CC}}{2} \)

## Figure 12: Receiver Enable and Disable Waveforms

- **Input Voltage Levels:**
  - High: 3V
  - Low: 0V
  - Intermediate: 1.5V

- **Output Voltage Levels:**
  - High: \( V_{OH} \)
  - Low: \( V_{OL} \)

## Notes

1. The input pulse is supplied by a generator with the following characteristics:
   - PRR = 250KHz, 50% duty cycle, \( t < 6.6 \, ns \), \( Z_0 = 50 \, \Omega \).
   
2. \( C_L \) includes probe and stray capacitance.
```


---
# Page 7
---

```markdown
# PACKAGE: PLASTIC DUAL-IN-LINE (NARROW)

## Dimensions (Inches)
| 8-PIN | Minimum/Maximum (mm) |
|-------|----------------------|
| A2    | 0.115/0.195 (2.921/4.953) |
| B     | 0.014/0.022 (0.356/0.559) |
| B1    | 0.045/0.070 (1.143/1.778) |
| C     | 0.008/0.014 (0.203/0.356) |
| D     | 0.017/0.160 (0.355/0.400) |
| E     | 0.300/0.325 (7.620/8.255) |
| E1    | 0.240/0.280 (6.096/7.112) |
| L     | 0.115/0.150 (2.921/3.810) |
| Ø     | 0°/15° (0°/15°) |

## Package Dimensions
- **D1** = 0.005" min. (0.127 min.)
- **A1** = 0.015" min. (0.381 min.)
- **A** = 0.210" max. (5.334 max.)
- **A2** = 0.210" max. (5.334 max.)
- **e** = 0.100 BSC (2.540 BSC)

### Alternate End Pins (Both Ends)

## Notes
- All dimensions are in inches unless otherwise specified.
- BSC indicates "Basic Dimension" for reference.
```


---
# Page 8
---

```markdown
# PACKAGE: PLASTIC SMALL OUTLINE (SOIC) (NARROW)

## Dimensions

### 8-Pin Package

| Dimension (Inches) | Minimum/Maximum (mm) |
|---------------------|----------------------|
| A                   | 0.053 / 0.069        |
|                     | (1.346 / 1.748)      |
| A1                  | 0.004 / 0.010        |
|                     | (0.102 / 0.249)      |
| B                   | 0.014 / 0.019        |
|                     | (0.350 / 0.49)       |
| D                   | 0.189 / 0.197        |
|                     | (4.80 / 5.00)        |
| E                   | 0.150 / 0.157        |
|                     | (3.802 / 3.988)      |
| e                   | 0.050 BSC            |
|                     | (1.270 BSC)          |
| H                   | 0.222 / 0.244        |
|                     | (5.801 / 6.198)      |
| h                   | 0.010 / 0.020        |
|                     | (0.254 / 0.498)      |
| L                   | 0.016 / 0.050        |
|                     | (0.406 / 1.270)      |
| Ø                   | 0° / 8°              |
|                     | (0° / 8°)            |

### Diagram Description

- The diagram shows a plastic small outline integrated circuit (SOIC) package with 8 pins.
- The package is viewed from the top and side, illustrating dimensions such as height (h), width (D), and length (L).
- The angle of the package is indicated as 45°.

---

*10/15/02 SP3481/3485 Low Power Half-Duplex RS485 Transceivers © Copyright 2000 Sipex Corporation*
```

---
# Page 9
---

```markdown
# ORDERING INFORMATION

| Model     | Temperature Range | Package            |
|-----------|-------------------|--------------------|
| SP3481CN  | 0°C to +70°C      | 8-pin Narrow SOIC   |
| SP3481CP  | 0°C to +70°C      | 8-pin Plastic DIP   |
| SP3481EN  | -40°C to +85°C    | 8-pin Narrow SOIC   |
| SP3481EP  | -40°C to +85°C    | 8-pin Plastic DIP   |
| SP3485CN  | 0°C to +70°C      | 8-pin Narrow SOIC   |
| SP3485CP  | 0°C to +70°C      | 8-pin Plastic DIP   |
| SP3485EN  | -40°C to +85°C    | 8-pin Narrow SOIC   |
| SP3485EP  | -40°C to +85°C    | 8-pin Plastic DIP   |

Please consult the factory for pricing and availability on a Tape-On-Reel option.

Available in lead-free packaging. To order, add "-L" suffix to the part number. Example: SP3481CN = standard; SP3481CN-L = lead free.

---

## Sipex Corporation

**Headquarters and Sales Office**  
233 South Hillview Drive  
Milpitas, CA 95035  
TEL: (408) 934-7500  
FAX: (408) 935-7600  

**Sales Office**  
22 Linell Circle  
Billerica, MA 01821  
TEL: (978) 667-8700  
FAX: (978) 670-9001  
e-mail: sales@sipex.com  

---

Sipex Corporation reserves the right to make changes to any products described herein. Sipex does not assume any liability arising out of the application or use of any product or circuit described herein; neither does it convey any license under its patent rights nor the rights of others.

*Date: 10/15/02*  
*Document: SP3481/3485 Low Power Half-Duplex RS485 Transceivers*  
*© Copyright 2002 Sipex Corporation*
```

---



---

## Master Document Metadata

- **Generated:** 2025-07-15 19:52:20
- **Source Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Documents Included:** 7
- **Individual Files:** CAN-MAX485, CAN-RS485-CAN-HAT-B-schematic, CAN-RS485-CAN-HAT-user-manual-en, CAN-RS485-CAN-Shield-Schematic, CAN-RS485-CAN-Shield-User-Manual, CAN-SN65HVD230, CAN-SP3481_SP3485
