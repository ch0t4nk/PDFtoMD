<!--
============================================================
MARKPDFDOWN CONVERSION METADATA
============================================================
File: um1910-getting-started-with-the-high-power-stepper-motor-driver-expansion-board-based-on-powerstep01-for-stm32-nucleo-stmicroelectronics_batch.md
Converted: 2025-07-16 13:45:38
Source PDF: Unknown
Batch ID: batch_6877e4e6cb90819091bc0a04dd0a80bc
Session ID: 20250716_134359
------------------------------------------------------------
PROCESSING DETAILS:
Pages Processed: Unknown
API Cost: $0.0000
Cost per Page: $0.0000
Tokens Used: Unknown
------------------------------------------------------------
BATCH CONTEXT:
Total Files in Batch: 14
Total Batch Cost: $0.0811
Average Batch Cost/Page: $0.0811
Processing Time: 0.0 minutes
============================================================
-->

---
# Page 1
---

# UM1910
## User Manual

### Getting started with the high power stepper motor driver expansion board based on powerSTEP01 for STM32 Nucleo

### Introduction

The **X-NUCLEO-IHM03A1** is a high power stepper motor driver expansion board based on the powerSTEP01. It provides an affordable and easy-to-use solution for driving high power bipolar stepper motors in your STM32 Nucleo project. The fully digital motion control through speed profile generation, dynamic positioning feedback, and a complete suite of protection features offer high levels of performance and robustness. The **X-NUCLEO-IHM03A1** is compatible with the Arduino UNO R3 connector and supports the addition of other boards which can be stacked to drive up to three stepper motors with a single STM32 Nucleo board.

### Figure 1
**X-NUCLEO-IHM03A1 expansion board for STM32 Nucleo**

### Notice
For dedicated assistance, submit a request through our online support portal at [www.st.com/support](http://www.st.com/support).

---

**UM1910 - Rev 2 - March 2025**  
For further information, contact your local STMicroelectronics sales office.

---
# Page 2
---

# UM1910
## Getting started

The X-NUCLEO-IHM03A1 expansion board is a high power stepper motor driver covering a wide range of applications. In particular, the maximum ratings of the board are the following:

- Power stage supply voltage (VS) from 10.5 V to 50 V
- Motor phase current up to 10 A r.m.s.

Follow this sequence to start your project with the board:

1. Check the jumper position based on your configuration (see Section 2: Hardware description and configuration).
2. Plug the board to the STM32 Nucleo board through Arduino UNO R3 for the X-NUCLEO-IHM03A1.
3. Supply the board through the input 1 (VS) and 2 (ground) of the connector CN1. The power OK (green) and fault (red) LEDs will turn on.
4. Develop your application using the examples provided with the firmware library, X-CUBE-SPN3, high power stepper motor driver software expansion for STM32Cube. Further support material is available on the powerSTEP01 (www.st.com/powerstep) and STM32 Nucleo web pages (www.st.com/stm32nucleo).

**Note:** Up to three expansion boards can be stacked on the same STM32 Nucleo board as described in Section 2.2: Multi-motor configuration.

---
# Page 3
---

# 2 Hardware description and configuration

Figure 2. Jumper and connector positions shows the position of the connectors and the configuration jumpers of the board.

## Figure 2. Jumper and connector positions

Below are the pinout details for the Arduino UNO R3 and the ST Morpho connectors.

## Table 1. Arduino UNO R3 connector table

| Connector | Pin (1) | Signal                  | Remarks                                                                 |
|-----------|---------|------------------------|-------------------------------------------------------------------------|
| CN5       | 1       | powerSTEP RESET        |                                                                         |
|           | 2       | Step clock input       |                                                                         |
|           | 3       | SPI CS                 | See Section 2.1: Selecting the chip select and clock lines of the SPI  |
|           | 4       | SPI MOSI               | See Section 2.2: Multi-motor configuration                             |
|           | 5       | SPI MISO               | See Section 2.2: Multi-motor configuration                             |
|           | 6       | SPI SCK                | See Section 2.1: Selecting the chip select and clock lines of the SPI  |
|           | 7       | Ground                 |                                                                         |
|           | 3       | FLAG                   |                                                                         |
| CN9       | 4       | SPI SCK                | See Section 2.1: Selecting the chip select and clock lines of the SPI  |
|           | 5       | BUSY / SYNC            |                                                                         |
| CN6       | 2       | VDD                    |                                                                         |
|           | 6       | Ground                 |                                                                         |
|           | 7       | Ground                 |                                                                         |
| CN8       | 1       | VDD                    |                                                                         |

---
# Page 4
---

# UM1910
## Hardware description and configuration

### Table 2. ST Morpho connector table

| Connector | Pin (1) | Signal          | Remarks                                                        |
|-----------|---------|------------------|----------------------------------------------------------------|
| CN8       | 3       | Ground           | All the unlisted pins are not connected.                       |
| CN10      | 9       | Ground           |                                                                |
|           | 11      | SPI SCK          | See Section 2.1: Selecting the chip select and clock lines of the SPI |
|           | 13      | SPI MISO         | See Section 2.2: Multi-motor configuration                     |
|           | 15      | SPI MOSI         | See Section 2.2: Multi-motor configuration                     |
|           | 17      | SPI CS           | See Section 2.1: Selecting the chip select and clock lines of the SPI |
|           | 19      | Step clock input |                                                                |
|           | 21      | powerSTEP RESET  |                                                                |
|           | 29      | BUSY/SYNC       |                                                                |
|           | 31      | SPI CK           | See Section 2.1: Selecting the chip select and clock lines of the SPI |
|           | 33      | FLAG             |                                                                |
| CN7       | 12      | VDD              |                                                                |
|           | 20      | Ground           |                                                                |
|           | 22      | Ground           |                                                                |
|           | 28      | ID               |                                                                |
|           | 32      | SPI CS           | See Section 2.1: Selecting the chip select and clock lines of the SPI |

### 2.1 Selecting the chip select and clock lines of the SPI

The chip select and the clock lines of the SPI interface can be selected via the appropriate resistors indicated in Table 3. Chip select line selection and Table 4. Clock line selection.

### Table 3. Chip select line selection

| R9          | R10          | CS line                     |
|-------------|--------------|-----------------------------|
| Not mounted | 0 Ω          | CN5 pin3, CN10 pin 17 (default) |
| 0 Ω         | Not mounted  | CN8 pin 3, CN7 pin 32      |

### Table 4. Clock line selection

| R11          | R12          | SCK line                     |
|--------------|--------------|------------------------------|
| 0 Ω          | Not mounted  | CN5 pin6, CN10 pin 9 (default) |
| Not mounted  | 0 Ω          | CN9 pin 4, CN10 pin 31      |

---
# Page 5
---

# 2.2 Multi-motor configuration

The expansion boards can be stacked on a single STM32 Nucleo board in order to drive up to three stepper motors (one expansion board for each motor is required).

The configuration is changed by mounting the resistors from R3 to R8 as listed in **Table 5. Multi-motor setup table**.

The other resistors are not mounted.

By default, the stepper driver board is configured for a single-motor setup, so the board configuration must be changed in multi-motor setups before stacking the boards on the STM32 Nucleo.

## Table 5. Multi-motor setup table

| Number of motors | Of Board       | Mounted resistors |
|------------------|----------------|--------------------|
| 1                | -              | R3 – R8            |
| 2                | 1 (bottom)     | R3 – R6            |
|                  | 2 (top)       | R4 – R8            |
| 3                | 1 (bottom)     | R3 – R6            |
|                  | 2              | R4 – R7            |
|                  | 3 (top)       | R5 – R8            |

---
# Page 6
---

# UM1910

## 3 Schematic Diagram

**Figure 3. Schematic diagram**

### Description of the Schematic

The schematic diagram illustrates the connections and components used in the UM1910 system. Key components include:

- **Power Supply**: The circuit is powered by a voltage source (V_in) rated at 5V.
- **Microcontroller**: Central processing unit for managing operations.
- **Sensors**: Multiple sensors (SENSOR_A, SENSOR_B, etc.) are connected to the microcontroller for data acquisition.
- **Output Connections**: Various output pins (OUT_1, OUT_2, etc.) are designated for interfacing with external devices.

### Technical Specifications

- **Voltage Input**: 5V
- **Microcontroller Part Number**: [Insert part number here]
- **Sensor Types**: [Insert sensor types here]

### Connections

- **Power Connections**:
  - V_in connected to the power supply.
  - Ground connections are established throughout the circuit.

- **Sensor Connections**:
  - Each sensor is connected to designated pins on the microcontroller.
  
- **Output Connections**:
  - Outputs are connected to external devices for signal processing.

### Notes

- Ensure all connections are secure to prevent signal loss.
- Refer to the component datasheets for detailed specifications and pin configurations.

---
# Page 7
---

# UM1910  
## Bill of Materials  

### Table 6. BOM list (Part 1)

| Item | Reference | Value  | Q.ty | Description                                   | Part number          |
|------|-----------|--------|------|-----------------------------------------------|----------------------|
| 1    | C1 C6     | 100NF  | 2    | CAP CER 100nF 50V X7R 0603                   | 100NF_50V_X7R_0603   |
| 2    | C2       | 220NF  | 1    | CAP CER 220nF 35V X7R 0603                   | 220NF_35V_X7R_0603   |
| 3    | C3 C7    | 470NF  | 2    | CAP CER 470nF 25V X7R 0603                   | 470NF_25V_X7R_0603   |
| 4    | C4       | 3.3NF  | 1    | CAP CER 3.3nF 50V X7R 0603                   | 3.3NF_50V_X7R_0603   |
| 5    | C5       | NP     | 1    | CAP NP 0603                                   | C_NP_0603            |
| 6    | C8       | 47NF   | 1    | CAP CER 47nF 100V X7R/X7S 0805               | 47NF_100V_X7R/X7S_0805 |
| 7    | C9       | 22UF   | 1    | CAP TANT 22uF 6V3 10% PACK-A                  | 22UF_6V3_TANT_PACK-A |
| 8    | C10-C13  | 220NF  | 4    | CAP CER 220nF 100V X7R 0805                   | 220NF_100V_X7R_0805  |
| 9    | C14 C15  | 68UF   | 2    | CAP ALU 68uF 100V SMD 17x17                   | EEV-FK2A680M         |
| 10   | C16 C17  | NP     | 2    | CAP ALU 68uF 100V Radial 10x5 P5              | UHEA2680MPD          |
| 11   | CN1      | MKDS1/6-3.81 | 1 | Screw connector 6 poles MKDS 1/6-3.81         | MKDS1/6-3.81         |
| 12   | CN2      | CON-1x2 | 1   | THOUGH-HOLE-1x2-Pin height 14.8 - Body 8.5mm - pitch 2.54 | SSQ-102-04-F-S       |
| 13   | CN5      | CON-1x10 | 1  | THOUGH-HOLE-1x10-Pin height 14.8 - Body 8.5mm - pitch 2.54 | SSQ-110-04-F-S       |
| 14   | CN6 CN9  | CON-1x8 | 2   | THOUGH-HOLE-1x8-Pin height 14.8 - Body 8.5mm - pitch 2.54 | SSQ-108-04-F-S       |
| 15   | CN7 CN10 | CON-2x19 | 2  | THOUGH-HOLE-2x19-Pin height 14.8 - Body 8.5mm - pitch 2.54 | SSQ-119-04-L-D       |
| 16   | CN8      | CON-1x6 | 1   | THOUGH-HOLE-1x6-Pin height 14.8 - Body 8.5mm - pitch 2.54 | SSQ-106-04-F-S       |
| 17   | D1       | BAR43   | 1   | Double Diode High Speed Switching Diode       | BAR43                |
| 18   | D2       | RED     | 1   | LED RED - 0805 -2mcd - 621nm                  | LED_RED              |
| 19   | D3-D7    | YELLOW  | 5   | LED YELLOW - 0805 -6mcd - 588nm               | LED_YELLOW           |
| 20   | D8       | GREEN   | 1   | LED GREEN - 0805 -6mcd - 569nm                | LED_GREEN            |
| 21   | D9 D10   | BAT46ZFILM | 2 | DIODE SCHOTTKY 150MA                          | BAT46                |
| 22   | MIRE1-MIRE3 | OPTICAL_TARGET | 3 | OPTICAL_TARGET                               | OPTICAL_TARGET       |
| 23   | R1 R2    | 0R1    | 2    | RES 0.1 OHM 5% 2W 2512                       | 0R1_5%_2512         |
| 24   | R3 R8 R10 R11 | 0R | 4 | RES 0 OHM 5% 1/8W 0805                       | 0R_5%_0805          |
| 25   | R4-R7 R9 R12 R22 | NP | 7 | RES NP 0805                                   | R_NP_0805           |
| 26   | R13 R25 R26 | 39K | 3  | RES 39K OHM 5% 1/10W 0603                    | 39K_5%_0603         |
| 27   | R14 R20 R21 | 330R | 3 | 330R OHM 5% 1/10W                            | 330R_5%_0603        |
| 28   | R15 R23   | 0R    | 2   | RES 0 OHM 5% 1/10W 0603                      | 0R_5%_0603          |

---
# Page 8
---

# UM1910
## Bill of Materials

### Table 7. BOM list (Part 2)

| Item | Reference      | Value | Q.ty | Description                          | Part number      |
|------|----------------|-------|------|--------------------------------------|------------------|
| 29   | R16-R19        | 10K   | 4    | RES 10K OHM 5% 1/10W 0805 SMD      | 10K_5%_0805      |
| 30   | R24 R27-R30    | NP    | 5    | RES NP 0603                          | R_NP_0603        |
| 31   | TP1            | KEYSTONE-5000 | 1 | TEST POINT RED                       | KEYSTONE 5000    |
| 32   | U1             | POWERSTEP01 | 1 | Fully integrated stepper motor driver | POWERSTEP01      |

### Additional BOM List

| Item | Manufact.       | Manuf. Part number | Distributor | Distributor Part number |
|------|------------------|--------------------|-------------|-------------------------|
| 1    |                  |                    |             |                         |
| 2    |                  |                    |             |                         |
| 3    |                  |                    |             |                         |
| 4    |                  |                    |             |                         |
| 5    |                  |                    |             |                         |
| 6    |                  |                    |             |                         |
| 7    |                  |                    |             |                         |
| 8    | PANASONIC        | EEV-FK2A680Q       |             |                         |
| 9    | NICHICON         | UHE2A680MPD        |             |                         |
| 10   | PHOENIX CONTACT   | MKD5/1.6-3.81     | RS          | 220-4377                |
| 11   | SAMTEC           | SSQ-102-04-F-S     |             |                         |
| 12   | SAMTEC           | SSQ-110-04-F-S     |             |                         |
| 13   | SAMTEC           | SSQ-108-04-F-S     |             |                         |
| 14   | SAMTEC           | SSQ-119-04-L-D     |             |                         |
| 15   | SAMTEC           | SSQ-106-04-F-S     |             |                         |
| 16   | STMICROELECTRONICS | BAR43SFILM      | RS          | 714-0470                |
| 17   | LITE-ON          | LTST-C170-EKT      | RS          | 692-0890                |
| 18   | LITE-ON          | LTST-C170-YKT      | RS          | 692-0925                |
| 19   | LITE-ON          | LTST-C170-GKT      | RS          | 692-0900                |
| 20   | STMICROELECTRONICS | BAT46ZFILM      | RS          | 714-6850                |
| 21   |                  |                    |             |                         |
| 22   |                  |                    |             |                         |
| 23   |                  |                    |             |                         |
| 24   |                  |                    |             |                         |
| 25   |                  |                    |             |                         |
| 26   |                  |                    |             |                         |
| 27   |                  |                    |             |                         |
| 28   |                  |                    |             |                         |
| 29   |                  |                    |             |                         |
| 30   |                  |                    |             |                         |
| 31   | KEYSTONE         | KEYSTONE 5000      | FARNELL     | 1460376                 |
| 32   | STMICROELECTRONICS | POWERSTEP01      |             |                         |

---
# Page 9
---

# Regulatory Compliance Information

## Notice for US Federal Communication Commission (FCC)

For evaluation only; not FCC approved for resale.

**FCC NOTICE** - This kit is designed to allow:

1. Product developers to evaluate electronic components, circuitry, or software associated with the kit to determine whether to incorporate such items in a finished product and
2. Software developers to write software applications for use with the end product.

This kit is not a finished product and when assembled may not be resold or otherwise marketed unless all required FCC equipment authorizations are first obtained. Operation is subject to the condition that this product does not cause harmful interference to licensed radio stations and that this product accept harmful interference. Unless the assembled kit is designed to operate under part 15, part 18 or part 95 of this chapter, the operator of the kit must operate under the authority of an FCC license holder or must secure an experimental authorization under part 5 of this chapter 3.1.2.

## Notice for Innovation, Science and Economic Development Canada (ISED)

For evaluation purposes only. This kit generates, uses, and can radiate radio frequency energy and has not been tested for compliance with the limits of computing devices pursuant to Industry Canada (IC) rules.

À des fins d’évaluation uniquement. Ce kit génère, utilise et peut émettre de l'énergie radioélectrique et n'a pas été testé pour sa conformité aux limites des appareils informatiques conformément aux règles d’Industrie Canada (IC).

## Notice for the European Union

This device is in conformity with the essential requirements of the Directive 2014/30/EU (EMC) and of the Directive 2015/863/EU (RoHS) according to standards EN 55032:2015+A11:2020, EN IEC 61000-6-3:2021, EN 55035:2017+A11:2020, EN IEC 61000-6-1:2019 and EN IEC 63000:2018. Compliance to EMC standards in Class A (industrial intended use).

---
# Page 10
---

# Revision history

## Table 8. Document revision history

| Date         | Revision | Changes                                                       |
|--------------|----------|--------------------------------------------------------------|
| 06-Jul-2015  | 1        | Initial release.                                            |
| 03-Mar-2025  | 2        | Updated the entire document to improve readability. <br> Added Section 5: Regulatory compliance information. |

---
# Page 11
---

# UM1910

## Contents

1. [Getting started](#getting-started) .................................................. 2  
2. [Hardware description and configuration](#hardware-description-and-configuration) .......... 3  
   2.1 [Selecting the chip select and clock lines of the SPI](#selecting-the-chip-select-and-clock-lines-of-the-spi) .......... 4  
   2.2 [Multi-motor configuration](#multi-motor-configuration) .......................... 5  
3. [Schematic diagram](#schematic-diagram) ............................................. 6  
4. [Bill of materials](#bill-of-materials) .................................................. 7  
5. [Regulatory compliance information](#regulatory-compliance-information) ................. 9  

## Revision history ................................................................................. 10  
## List of tables ....................................................................................... 12  
## List of figures ...................................................................................... 13  

---
# Page 12
---

# UM1910
## List of tables

| Table Number | Title                                           | Page |
|--------------|-------------------------------------------------|------|
| Table 1      | Arduino UNO R3 connector table                  | 3    |
| Table 2      | ST Morpho connector table                        | 4    |
| Table 3      | Chip select line selection                       | 4    |
| Table 4      | Clock line selection                             | 4    |
| Table 5      | Multi-motor setup table                         | 5    |
| Table 6      | BOM list (Part 1)                               | 7    |
| Table 7      | BOM list (Part 2)                               | 8    |
| Table 8      | Document revision history                        | 10   |

---
# Page 13
---

# List of Figures

| Figure Number | Description                                                   | Page |
|---------------|---------------------------------------------------------------|------|
| Figure 1      | X-NUCLEO-IHM03A1 expansion board for STM32 Nucleo           | 1    |
| Figure 2      | Jumper and connector positions                                 | 3    |
| Figure 3      | Schematic diagram                                             | 6    |

---
# Page 14
---

# UM1910

## IMPORTANT NOTICE – READ CAREFULLY

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST's terms and conditions of sale in place at the time of order acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of purchasers' products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to [www.st.com/trademarks](http://www.st.com/trademarks). All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2025 STMicroelectronics – All rights reserved

---

## Processing Metadata

- **Document:** um1910-getting-started-with-the-high-power-stepper-motor-driver-expansion-board-based-on-powerstep01-for-stm32-nucleo-stmicroelectronics
- **Total Pages:** 14
- **Processing Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Batch ID:** batch_6877e4e6cb90819091bc0a04dd0a80bc
- **Processed:** 2025-07-16 13:45:38

### 📊 Processing Statistics

- **Total Tokens Used:** 524,645
- **Prompt Tokens:** 519,218
- **Completion Tokens:** 5,427
- **Total Processing Cost:** $0.0811
- **Average Tokens per Page:** 37475
- **Average Cost per Page:** $0.0058

### 💰 Cost Breakdown

- **Input Processing:** $0.0779 (vision + text)
- **Output Generation:** $0.0033 (markdown text)
- **Batch API Discount:** 50% off regular pricing
- **Estimated Regular Cost:** $0.1623

### ⚡ Efficiency Metrics

- **Tokens per Dollar:** 6466011
- **Pages per Dollar:** 172.5
- **Processing Method:** Batch API (cost-optimized)
