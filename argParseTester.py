import argparse


parser = argparse.ArgumentParser()

parser.add_argument("idc")

laeme = parser.parse_args()

print(laeme.idc)