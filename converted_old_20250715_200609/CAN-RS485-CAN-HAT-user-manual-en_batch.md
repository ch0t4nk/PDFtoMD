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

## Processing Metadata

- **Document:** CAN-RS485-CAN-HAT-user-manual-en
- **Total Pages:** 24
- **Processing Method:** OpenAI Batch API
- **Model:** gpt-4o-mini
- **Batch ID:** batch_6876e59c6e908190b68f3f13dda5e3e1
- **Processed:** 2025-07-15 20:02:23

### 📊 Processing Statistics

- **Total Tokens Used:** 892,923
- **Prompt Tokens:** 886,752
- **Completion Tokens:** 6,171
- **Total Processing Cost:** $0.1367
- **Average Tokens per Page:** 37205
- **Average Cost per Page:** $0.0057

### 💰 Cost Breakdown

- **Input Processing:** $0.1330 (vision + text)
- **Output Generation:** $0.0037 (markdown text)
- **Batch API Discount:** 50% off regular pricing
- **Estimated Regular Cost:** $0.2734

### ⚡ Efficiency Metrics

- **Tokens per Dollar:** 6531254
- **Pages per Dollar:** 175.5
- **Processing Method:** Batch API (cost-optimized)
