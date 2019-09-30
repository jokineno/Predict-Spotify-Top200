import os
import spotipy
import spotipy.util as util
import pandas as pd


def load_environment():
    from dotenv import load_dotenv
    load_dotenv()
    username = os.getenv("USR")
    client_id = os.getenv("ID")
    client_secret = os.getenv("SECRET")
    redirect_uri = os.getenv("URI")
    return username, client_id, client_secret, redirect_uri


def get_audio_features(infile, outfile, username, client_id, client_secret, redirect_uri):
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

    # Erase catche and prompt for user permission
    try:
        token = util.prompt_for_user_token(username,
                                           scope,
                                           client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirect_uri)
    except Exception:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)

    # Create spotify object
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()

    displayName = user['display_name']

    print(">>> Hello", displayName)

    data = pd.read_csv(infile)
    track_features = sp.audio_features(data.id[0])
    track_df = pd.DataFrame(track_features)
    df = pd.DataFrame(columns=track_df.columns)

    n = 0
    for id in data.id:
        try:
            features = sp.audio_features(id)
        except Exception:
            continue
        n += 1
        print(n)
        feature_df = pd.DataFrame(features)
        df = df.append(feature_df)

    index_length = df.shape[0]
    index_set = list(range(index_length))
    df = df.set_index(pd.Index(index_set))

    final_df = data.join(df, lsuffix='_caller', rsuffix='_other')
    final_df.to_csv(outfile)

    print("DATA JOINING COMPLETED")
    print("File saved as:", outfile)


def main():
    username, client_id, client_secret, redirect_uri = load_environment()
    infile = "data/top_200_weekly.csv"
    outfile = "data/top_200_features.csv"
    get_audio_features(infile, outfile, username, client_id, client_secret, redirect_uri)


if __name__ == "__main__":
    main()
