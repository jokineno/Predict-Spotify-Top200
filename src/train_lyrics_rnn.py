from textgenrnn import textgenrnn


def main():
    """
    Outputs textgenrnn_weights.hdf5
    """
    textgen = textgenrnn()
    textgen.train_from_file("data/processedlyrics.txt", num_epochs=4)


if __name__ == "__main__":
    main()
    