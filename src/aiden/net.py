import urllib.request
import urllib.error


def has_internet(timeout: float = 3.0) -> bool:
    print("Init Internet connection...")
    try:
        with urllib.request.urlopen(
            "https://connectivitycheck.gstatic.com/generate_204",
            timeout=timeout,
        ) as response:
            print("Connection established")
            print("Going online")
            return response.status == 204
    except (urllib.error.URLError, TimeoutError, OSError):
        return False