#!/usr/bin/python

import sys, getopt
import coingecko
import time

def main(args_in):
    if len(args_in) > 0:
        gecko_ = coingecko.gecko(args_in)

        while (True):
            try:
                price, change = gecko_.generate_reports()
                print("Raw data: ", price, change)
            except Exception as e:
                print("=== Something went wrong about: "+str(e)+" ===")
            time.sleep(60)
    else:
        print("No coins are provided. Run the script as: python server.py <coin1> <coin2> ...")


if __name__ == "__main__":
   main(sys.argv[1:])