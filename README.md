# Packet Analysis and Visualization Tool

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

- `final_packet_analyzer.py`: .
- `pcap files`: Contains pcap recordings obtained from Wireshark.
- `csv files`: Contains CSV files containing packet data.
- `Plots`: Contains output plots organized into subfolders.
    - `IMD`: Inter Message Delays plots.
    - `PDF`: Probability Density Function plots.
    - `CCDF`: Complementary Cumulative Distribution Function plots.
- `final_packet_analyzer.py`: The main Python file that runs the program.
- `Article.pdf`: The paper that the project is based on.
- `Network Project PDF(dry part).pdf`: The dry part that contains answers to questions and a summary of the article.


## Usage

1. Install the required libraries using the following command:

```bash
pip install matplotlib numpy scapy pandas
