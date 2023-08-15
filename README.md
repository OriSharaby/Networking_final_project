# Packet Analysis and Visualization Tool

This tool is designed to analyze packet capture (pcap) recordings using Python and generate various plots for visualizing packet data and statistics. The tool makes use of the `matplotlib`, `numpy`, `scapy`, and `pandas` libraries for data manipulation and visualization.

## Project Structure

The project directory contains the following folders:

- `pcap files`: Contains pcap recordings obtained from Wireshark.
- `csv files`: Contains CSV files containing packet data.
- `Plots`: Contains output plots organized into subfolders.
    - `IMD`: Inter Message Delays plots.
    - `PDF`: Probability Density Function plots.
    - `CCDF`: Complementary Cumulative Distribution Function plots.

## Usage

1. Install the required libraries using the following command:

```bash
pip install matplotlib numpy scapy pandas
