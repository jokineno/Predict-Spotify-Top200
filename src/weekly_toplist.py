from fycharts import SpotifyCharts


def get_weekly_toplist(outfile):
    api = SpotifyCharts.SpotifyCharts()
    api.top200Weekly(output_file=outfile, start="2017-06-09", region="global")


def main():
    get_weekly_toplist("data/top_200_weekly.csv")


if __name__ == "__main__":
    main()
