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


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR"),
    ('ru', "RU")
])
def test_update_inner(get_player_generator,localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ["localize", localizations], PlayerLocalization(loc).set_number(15).build()).build()
    print(object_to_send)
