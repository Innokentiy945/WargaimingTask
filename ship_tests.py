def test_option_a(ship, ship_component, original_value, current_value):
    weapons_allowed = []
    for i in range(1, 21):
        weapons_allowed.append(f"Weapon-{i}")

    hulls_allowed = []
    for i in range(1, 6):
        hulls_allowed.append(f"Hull-{i}")

    engines_allowed = []
    for i in range(1, 7):
        engines_allowed.append(f"Engine-{i}")

    if original_value == current_value:
        assert False, (
            f"{ship} {ship_component} value did not change.\n"
            f"Expected:\n  {original_value}\n"
            f"But was:\n  {current_value}"
        )

    allowed = None
    if ship_component == "weapon":
        allowed = weapons_allowed
    elif ship_component == "hull":
        allowed = hulls_allowed
    elif ship_component == "engine":
        allowed = engines_allowed

    if allowed is not None and current_value not in allowed:
        assert False, (
            f"{ship} {ship_component} changed to an invalid value.\n"
            f"Expected:\n  {allowed}\n"
            f"But was:\n  {current_value}"
        )

    print(
        f"{ship} {ship_component} changed.\n"
        f"Original: {original_value}\n"
        f"Current:  {current_value}"
    )
