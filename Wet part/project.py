import matplotlib.pyplot as plt
import numpy as np
from scapy.all import *
import pandas as pd
import os

#Fig.8
def plot_packet_length_time(df):

    plt.figure(figsize=(10, 5))
    plt.bar(df['Time'], df['Length'], width=0.1)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length')
    plt.title('Packet Length as a Function of Time')
    plt.grid(True)
    plt.show()


#Fig.3
def plot_pdf_exponential_distribution(df):

    delay = np.diff(df['Time'])
    delay = np.append(delay, 0)

    df['Delay'] = delay
    print(df.head())
    rng = np.round(delay.max())

    print(delay)

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

    # Adjust x-axis tick labels to display every value separately
    plt.xticks(np.arange(0, np.max(delay) + 1, 1))

    plt.show()

def make_ccdf(filter,threshold=0.7):
    sort_array = np.sort(filter)
    normalized_array =sort_array/max(sort_array)

    #compute CCDF
    ccdf = 1 - (np.arange(1,len(sort_array)+1)/len(sort_array))

    return normalized_array,ccdf


#Fig.4
def plot_ccdf(dframes,classification):
    plt.figure(figsize=(10, 6))

    for df,type in zip(dframes,classification):
        normalized_array, ccdf = make_ccdf(df['Length'])
        plt.plot(normalized_array,ccdf,label = type)

    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Normalized Message Sizes')
    plt.ylabel('CCDF')
    plt.title('CCDF of Packets Size Distribution')
    plt.legend(loc="lower left")
    plt.show()


def main():
    file_path_video = 'C:/Users/USER/Desktop/Networking Project/Exel files/videos.csv'
    df_video = pd.read_csv(file_path_video)
    plot_packet_length_time(df_video)
    plot_pdf_exponential_distribution(df_video)

if __name__ == "__main__":
    main()






