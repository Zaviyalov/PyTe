import requests
import pytest
from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVATE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_generation(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("deleted_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_deleted(deleted_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[deleted_key]
    print(object_to_send)


def test_update_inner(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator("localize",
                                                                 PlayerLocalization("fr_FR").set_number()).build()
    print(object_to_send)
