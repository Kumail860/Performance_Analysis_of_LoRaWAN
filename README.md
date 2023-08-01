# Performance_Analysis_of_LoRaWAN
This work is a description of the experiment conducted to understand the reception
of LoRa in closed environments, such as a building.
The experiment was carried out on 04/05/2023, in the NW1 building of University of
Bremen. The data’s primary goal is to provide researchers with the understanding of
factors such as distance, obstacles, interference with other wireless devices that
dictates LoRa’s performance.
The experiment setup phase was fairly simple, 4 gateways/receivers were deployed
in different locations in the NW1 building.
The NW1 building consists of different blocks and multiple floors. From each location
we sent exactly 4 packets.
Timestamps were noted for the sent packets.
We transmitted data through the various blocks and floors in order to compare the
different RSSI (Received Signal Strength Indicator) and see how they vary
accordingly.
The time stamps and respectives RSSI are stored in an excel file.
The data files are named in the format HHMM_Date_Month and saved as an Excel
Worksheet, (.xlsx).
The Excel file consists of the following fields/ columns:
● Packet_id: tells the packet number that was sent through the LoRa device.
This column represents a unique identifier for each packet of data. It helps to
distinguish one packet from another.
● Date: This column indicates the date on which the experiment was conducted
in the format [Year, Month, Date].
● Time: This column shows the time when a certain packet was sent. It uses the
format [Hour, Minute, Second].
● GW1 - GW4: The columns D to G comprises of different gateways/receivers.
Their values indicate the signal strength from different gateways. For some
instances, a data packet has been received by several gateways. For others
the packet was not received by any gateway, hence indicated by a dash or (-).
● Loc: The column H indicates the location/block in the NW1 building from
where the packet was sent.
● Floors: This column indicates the floor associated with the recorded data.
To filter our data of redundant information (extra packets sent), we have highlighted
rows that were identified as accidental transmissions and having the lowest RSSI.
The following rows were highlighted and thus can be deleted.
In the file 1230_4_5 the rows 62, 69, 75, 96, 114, 167, 180.
