import matplotlib.pyplot as plt
import numpy as np
from scapy.all import *
import pandas as pd
import os

def plot_packet_length_time(df):
    """
    Plot the packet length as a function of time.

    Parameters:
    df (pd.DataFrame): Input dataframe containing 'Time' and 'Length' columns.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(df['Time'], df['Length'], width=0.8)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length')
    plt.title('Packet Length as a Function of Time')
    plt.grid(True)
    return plt



def plot_pdf_exponential_distribution(df):
    """
    Plot the probability density function of inter-packet delays.

    Parameters:
    df (pd.DataFrame): Input dataframe containing 'Time' column.
    """
    delay = np.diff(df['Time'])
    delay = np.append(delay, 0)

    pdf, bin_edges = np.histogram(delay, bins=20, density=True)
    plt.figure(figsize=(10, 6))
    plt.hist(delay, density=True)

    mean_delay = np.mean(delay)
    lambda_fit = 1 / mean_delay
    x_fit = np.linspace(0, np.max(delay), 1000)
    y_fit = lambda_fit * np.exp(-lambda_fit * x_fit)

    plt.plot(x_fit, y_fit, color='orange', linewidth=2)
    plt.xlabel('Inter-Packet Delay (seconds)')
    plt.ylabel('PDF')
    plt.title('Probability Density Function of Inter-Packet Delays')
    plt.xticks(np.arange(0, np.max(delay) + 1, 1))
    return plt

def make_ccdf(filter, threshold=0.7):
    """
    Calculate the Complementary Cumulative Distribution Function (CCDF) for given data.

    Parameters:
    filter (np.array): Input data for which CCDF is calculated.
    threshold (float, optional): Threshold for CCDF calculation.

    Returns:
    np.array: Normalized data array, CCDF values.
    """
    sort_array = np.sort(filter)
    normalized_array = sort_array / max(sort_array)
    ccdf = 1 - (np.arange(1, len(sort_array) + 1) / len(sort_array))
    return normalized_array, ccdf


def plot_ccdf(dframes, classification):
    """
    Plot the CCDF of packets size distribution for different datasets.

    Parameters:
    dframes (list of pd.DataFrame): List of dataframes containing 'Length' column.
    classification (list of str): Labels for different datasets.
    """
    output_path = 'C:/Users/USER/Desktop/Networking Project/Wet part/Plots/CCDF/ccdf output.png'
    plt.figure(figsize=(10, 6))

    for df, type in zip(dframes, classification):
        normalized_array, ccdf = make_ccdf(df['Length'])
        plt.plot(normalized_array, ccdf, label=type)

    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Normalized Message Sizes')
    plt.ylabel('CCDF')
    plt.title('CCDF of Packets Size Distribution')
    plt.legend(loc="lower left")
    plt.savefig(output_path)


def files_handler():
    files = os.listdir("Exel files")
    csv_files = []
    for file in files:
        file_path = os.path.join("Exel files", file)
        file_name_without_extension = os.path.splitext(file)[0]
        csv_files.append((file_path, file_name_without_extension))

    return csv_files


def packet_length_handler(dfs):
    output_path = 'C:/Users/USER/Desktop/Networking Project/Wet part/Plots/PacketLength/'
    for name in dfs:
        pltToSave = plot_packet_length_time(dfs[name])
        pltToSave.savefig(output_path + name)


def pdf_exponential_distribution_handler(dfs):
    output_path = 'C:/Users/USER/Desktop/Networking Project/Wet part/Plots/PDF/'
    for name in dfs:
        pltToSave = plot_pdf_exponential_distribution(dfs[name])
        pltToSave.savefig(output_path + name)


def main():
    csv_files = files_handler()
    dfs = {}
    for file_path, data_type in csv_files:
        dfs[data_type] = pd.read_csv(file_path)
    packet_length_handler(dfs)
    pdf_exponential_distribution_handler(dfs)

    dataset_labels = ['Text Group', 'Images Group', 'Audio Group', 'Video Group']
    plot_ccdf(list(dfs.values()), dataset_labels)
    print('Files generated successfully')




if __name__ == "__main__":
    main()
