import coingecko
import time

gecko_ = coingecko.gecko(["bitcoin", "ethereum", "chainlink", "ocean-protocol"])

while (True):
    print(gecko_.generate_reports())
    time.sleep(60)