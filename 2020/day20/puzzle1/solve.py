with open("./input") as input_file:
    raw_input = input_file.read() + "\n"

raw_tiles = raw_input.split('Tile')[1:]
raw_tiles = [tile.split(":\n") for tile in raw_tiles]
tiles = {int(key.strip()): tuple(map(tuple, value.split("\n")[0:-2]))
         for key, value in raw_tiles}

WIDTH = len(tuple(tiles.values())[0])
HEIGHT = len(tuple(tiles.values())[0][0])

for key, tile in tiles.items():
    print("🆚", key)
    assert len(tile) == WIDTH
    for i, row in enumerate(tile):
        print("🌲", i)
        assert len(row) == WIDTH


def xflip(value):
    return tuple(
        tuple(reversed(row))
        for row in value
    )


def yflip(value):
    return tuple(map(tuple, reversed(value)))


def rot90(value):
    return tuple(
        tuple(
            value[WIDTH - j - 1][i]
            for j in range(WIDTH)
        )
        for i in range(WIDTH)
    )


def generate_variants(value):
    for i in range(4):
        yield value
        yield xflip(value)
        yield yflip(value)
        value = rot90(value)


tile_variants = {
    key: dict(enumerate(set(generate_variants(value)))) for key, value in tiles.items()
}


def get_edges(value):
    return {
        "top": value[0],
        "bottom": value[-1],
        "left": tuple(value[i][0] for i in range(WIDTH)),
        "right": tuple(value[i][-1] for i in range(WIDTH))
    }


tile_variant_edges = {
    key: {
        key_: get_edges(value_)
        for key_, value_ in value.items()
    }
    for key, value in tile_variants.items()


}

possible_matches = (
    ("top", "bottom"),
    ("left", "right"),
    ("bottom", "top"),
    ("right", "left"),
)


def get_tiles_with_matching_edges(to_match_variant, banned_tiles):
    matches = set()
    for key, value in tile_variant_edges.items():
        if key in banned_tiles:
            continue

        for variant_id, variant in value.items():
            for a, b in possible_matches:
                if to_match_variant[a] == variant[b]:
                    matches.add((a, (key, variant_id)))

    return matches


matching_edges_for_each_variant = {
    key: {
        key_: get_tiles_with_matching_edges(value_, [key_])
        for key_, value_ in value.items()
    }
    for key, value in tile_variant_edges.items()
}

print(matching_edges_for_each_variant)

print("🥊" * 10)


def iterate_variants():
    for key, value in matching_edges_for_each_variant.items():
        for key_, _ in value.items():
            yield key, key_


matched_edges_of_variant = tuple(
    ((tileid, varianid), set(
        x[0] for x in matching_edges_for_each_variant[tileid][varianid]
    ))
    for tileid, varianid in iterate_variants()
)

# print(matched_edges_of_variant)

corner_candidates = sorted(
    matched_edges_of_variant, key=lambda x: len(x[1])
)
print(corner_candidates)

# print(list(
# (key, key_) for key, key_ in iterate_variants() if set(x[0] for x in matching_edges_for_each_variant[key][key_]) == set(["bottom", "right"])
# ))
