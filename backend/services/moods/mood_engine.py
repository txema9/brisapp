def generate_zone_moods(
    zone,
    current_hour
):

    metrics = zone.metrics


    # =========================
    # TIPO DE ZONA
    # =========================

    zone_signals = {

        "🍴 Restauración":
            metrics.food_count,

        "🛍️ Compras":
            metrics.commerce_count,

        "🚶 Paseo":
            metrics.culture_count,

        "🛠️ Industria":
            metrics.health_count
    }


    zone.zone_type = max(
        zone_signals,
        key=zone_signals.get
    )


    # =========================
    # FACTORES TEMPORALES
    # =========================

    nightlife_multiplier = 1

    transport_multiplier = 1


    # NOCHE

    if current_hour >= 21:

        nightlife_multiplier = 2


    # HORA PUNTA

    if (
        7 <= current_hour <= 9
        or
        17 <= current_hour <= 19
    ):

        transport_multiplier = 2


    # =========================
    # TIPO DE OCIO
    # =========================

    social_activity = (

        metrics.food_count * 2

        + (
            metrics.nightlife_count
            * 3
            * nightlife_multiplier
        )

        + metrics.culture_count
    )


    if social_activity >= 40:

        zone.leisure_mood = (
            "🍻 Animado"
        )

    elif social_activity >= 12:

        zone.leisure_mood = (
            "☕ Tranquilo"
        )

    else:

        zone.leisure_mood = (
            "🏠 Residencial"
        )


    # =========================
    # ESTADO URBANO
    # =========================

    movement_activity = (

        (
            metrics.transport_count
            * 3
            * transport_multiplier
        )

        + metrics.commerce_count * 2

        + metrics.food_count
    )


    if movement_activity >= 60:

        zone.traffic_mood = (
            "⛔ Congestionado"
        )

    elif movement_activity >= 20:

        zone.traffic_mood = (
            "🚦 Activo"
        )

    else:

        zone.traffic_mood = (
            "🍃 Fluido"
        )