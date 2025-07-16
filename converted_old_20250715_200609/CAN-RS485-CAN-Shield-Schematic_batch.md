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

## Processing Metadata

- **Document:** CAN-RS485-CAN-Shield-Schematic
- **Total Pages:** 1
- **Processing Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Batch ID:** batch_6876e59c6e908190b68f3f13dda5e3e1
- **Processed:** 2025-07-15 20:02:23

### 📊 Processing Statistics

- **Total Tokens Used:** 37,921
- **Prompt Tokens:** 36,948
- **Completion Tokens:** 973
- **Total Processing Cost:** $0.0061
- **Average Tokens per Page:** 37921
- **Average Cost per Page:** $0.0061

### 💰 Cost Breakdown

- **Input Processing:** $0.0055 (vision + text)
- **Output Generation:** $0.0006 (markdown text)
- **Batch API Discount:** 50% off regular pricing
- **Estimated Regular Cost:** $0.0123

### ⚡ Efficiency Metrics

- **Tokens per Dollar:** 6190173
- **Pages per Dollar:** 163.2
- **Processing Method:** Batch API (cost-optimized)
