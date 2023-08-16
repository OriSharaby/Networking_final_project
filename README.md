# Packet Analysis and Visualization Tool

Welcome to the WhatsApp Web Packet Analysis project repository! 
This repository contains code and resources for analyzing packets from WhatsApp web group messages. 
The project involves sniffing packets, identifying message-related packets, and generating helpful plots to facilitate packet identification. 
The analysis is conducted in two distinct parts: one involving packet filtering, and the other simulating real-world noise with Spotify music playing in the background.

## Introduction

This Python script utilizes various libraries such as Matplotlib, NumPy, and Scapy to perform analysis and visualization on network packet data stored in CSV files. The script carries out the following tasks:

Plot Packet Length over Time: It creates a bar graph that displays the packet length as it changes over time.

Plot Delay Probability Density Function (PDF): This section computes the inter-packet delays, estimates parameters for an exponential distribution that fits the data, and then plots both the PDF of the delays and the fitted exponential distribution.

Calculate and Plot Complementary Cumulative Distribution Function (CCDF): The script calculates and plots the CCDF for different datasets' packet size distributions, using logarithmic scales for both axes.

Processing CSV Files: The script reads CSV files from a specified directory, storing the data in pandas DataFrames.

Plotting Packet Length and Delay PDF for Each Dataset: It iterates through the collected DataFrames and generates separate plots for packet length over time and delay PDF for each dataset, saving them as images.

Clearing Previous Plot Files: Before generating new plots, the script clears existing plot files from the designated directory.

Main Function: The main function orchestrates these steps, ensuring that plots are generated for various aspects of the packet data. It also prints a success message after generating the required files.

The script is essentially designed to analyze network packet data, generate insightful visualizations, and manage the overall process in a structured manner.


## Project Structure

The project directory contains the following folders:

- `res`: Contains output plots organized into subfolders.
    - `IMD`: Inter Message Delays plots.
    - `PDF`: Probability Density Function plots.
    - `CCDF`: Complementary Cumulative Distribution Function plots.
- `resources`: Contains two types of resources folders.
    - `pcap files`: Contains pcap recordings obtained from Wireshark.
    - `csv files`: Contains CSV files containing packet data.
- `src`: Contains the main Python script.
    - `final_packet_analyzer.py`: The main Python file that runs the program.


## Install

1. Install the required libraries using the following command:

```bash
pip install matplotlib numpy scapy pandas
```
## Get started

1. **Prepare CSV Files**: Place all your CSV files containing packet data in the `csv files` folder. You can obtain these CSV files by converting pcap recordings into CSV format using Wireshark or other similar tools.

2. **Run the Script**: Open a terminal or command prompt and navigate to the project directory. Run the Python script `final_packet_analyzer.py` using the following command:

    ```bash
    python final_packet_analyzer.py
    ```

   This will execute the script and generate various plots based on the provided CSV files.

3. **Review Plots**: After running the script, the generated plots will be saved in the `res` subfolders. You can explore the plots to gain insights into the packet data's characteristics.

## How to Use
Export the software recordings to csv files, there are two classifications of recordings: clean recordings, recordings with background noise
* clean recordings
    *  filter the recordings with filter ip.src ==157.240.195.56 && tls
    * Name the file "WhatsApp_(The type of messages).csv"

* recordings with background noise
    * Filter the recordings with a tls || filter quic || udp || tcp
    * Name the file "Spotify_WhatsApp_(The type of messages).csv"
  
Save the csv files in the 'csv files' subfolder which is in the 'resources' folder

## Notes

- Ensure your CSV files adhere to the necessary structure, including columns like 'Time', 'Length', and others as specified in the script.
- You can obtain these CSV files by using Wireshark; simply export the data as CSV instead of PCAP.

## Script Details

The `final_packet_analyzer.py` script performs the following tasks:

- Reads CSV files from the `csv files` folder.
- Generates packet length over time plots and saves them in the `IMD` subfolder.
- Generates probability density function plots for inter-packet delays and saves them in the `PDF` subfolder.
- Calculates and plots the complementary cumulative distribution function (CCDF) for packet sizes and saves it in the `CCDF` subfolder.
- Clears any existing plot files in the `res` folder before generating new plots.


## Contact

* Ori Sharaby
