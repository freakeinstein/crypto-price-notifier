#!/usr/bin/python

import sys, getopt
import coingecko
import time

def main(arg_in):
    if len(arg_in) > 1:
        timeout, coins_list = arg_in[0], arg_in[1:]

        if not timeout.isdigit():
            timeout = 60
        else:
            timeout = int(timeout)

        if len(coins_list) > 0:
            print("Program will check CoinGecko for price every "+ str(timeout) +" seconds for the following coins:", coins_list)
            gecko_ = coingecko.gecko(coins_list)

            while (True):
                try:
                    print("\n\n")
                    price, change = gecko_.generate_reports()
                    print("Raw data: ", price, change)
                    print("\n\n")
                except Exception as e:
                    print("=== Something went wrong about: "+str(e)+" ===")
                time.sleep(timeout)
    else:
        print("Run the script as: python server.py <timeout> <coin1> <coin2> ...")


if __name__ == "__main__":
   main(sys.argv[1:])