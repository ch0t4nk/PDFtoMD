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

## Processing Metadata

- **Document:** CAN-SP3481_SP3485
- **Total Pages:** 9
- **Processing Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Batch ID:** batch_6876e59c6e908190b68f3f13dda5e3e1
- **Processed:** 2025-07-15 20:02:23

### 📊 Processing Statistics

- **Total Tokens Used:** 236,231
- **Prompt Tokens:** 230,526
- **Completion Tokens:** 5,705
- **Total Processing Cost:** $0.0380
- **Average Tokens per Page:** 26248
- **Average Cost per Page:** $0.0042

### 💰 Cost Breakdown

- **Input Processing:** $0.0346 (vision + text)
- **Output Generation:** $0.0034 (markdown text)
- **Batch API Discount:** 50% off regular pricing
- **Estimated Regular Cost:** $0.0760

### ⚡ Efficiency Metrics

- **Tokens per Dollar:** 6216294
- **Pages per Dollar:** 236.8
- **Processing Method:** Batch API (cost-optimized)
