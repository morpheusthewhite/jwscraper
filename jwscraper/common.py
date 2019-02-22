from requests import get


class NoVideoAvailableException(Exception):
    pass


def save_video_at(url: str, filename: str=None):
    """
    Saves the video in the given url
    """
    r = get(url)

    if filename is None:
        filename = r.url.split("/")[-1]
    
    with open(filename, "wb") as out_file:
        out_file.write(r.content)

    return