from io import TextIOWrapper


def parse_seeds(raw_str: str) -> list[int]:
    return [int(x) for x in raw_str.split(": ")[1].split()]


SEED_TO_SOIL = "seed-to-soil"
SOIL_TO_FERTALIZER = "soil-to-fertilizer"
FERTALIZER_TO_WATER = "fertilizer-to-water"
WATER_TO_LIGHT = "water-to-light"
LIGHT_TO_TEMPERATURE = "light-to-temperature"
TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity"
HUMIDITY_TO_LOCATION = "humidity-to-location"


def search_maps(mappings: dict[str, list[int]], start_seed: int) -> int:
    cur_val = start_seed
    for mapping in mappings.values():
        cur_val = mapping[cur_val] if cur_val in mapping else cur_val
    return cur_val


with open("data.txt") as file:
    mappings: dict[str, list[int]] = {
        SEED_TO_SOIL: [],
        SOIL_TO_FERTALIZER: [],
        FERTALIZER_TO_WATER: [],
        WATER_TO_LIGHT: [],
        LIGHT_TO_TEMPERATURE: [],
        TEMPERATURE_TO_HUMIDITY: [],
        HUMIDITY_TO_LOCATION: [],
    }

    raw_seed_data = file.readline()

    seeds = parse_seeds(raw_seed_data)

    for mapping in mappings:
        cur_line = file.readline().strip()
        while cur_line and mapping not in cur_line:
            cur_line = file.readline().strip()

        cur_line = file.readline().strip()
        cur_line = file.readline().strip()

        while cur_line:
            dst, src, rnge = [int(x) for x in cur_line.split()]

            mappings[mapping] = [dst, src, rnge]

            cur_line = file.readline().strip()

    min_loc = min([search_maps(mappings, seed) for seed in seeds])
    print(min_loc)
