from backend.domain.models.zone import Zone


def get_zones():

    return [

        Zone(
            id=1,
            name="El Sardinero",
            latitude=43.47234934934887,
            longitude=-3.7826310695260883,
            radius=500,
            marker="🌊"
        ),

        Zone(
            id=2,
            name="Valdenoja",
            latitude=43.48256515385705,
            longitude=-3.793652450228221,
            radius=500,
            marker="🏡"
        ),

        Zone(
            id=3,
            name="Centro - Ayuntamiento",
            latitude=43.46237104044435,
            longitude=-3.810014266281815,
            radius=450,
            marker="🚨"
        ),

        Zone(
            id=4,
            name="Castilla-Hermida",
            latitude=43.45512685721038,
            longitude=-3.8193966314831678,
            radius=450,
            marker="⚓"
        ),

        Zone(
            id=5,
            name="Barrio Pesquero",
            latitude=43.45119335572701,
            longitude=-3.8208146583245783,
            radius=350,
            marker="🐟"
        ),

        Zone(
            id=6,
            name="General Dávila",
            latitude=43.46134772819438,
            longitude=-3.8303346119838824,
            radius=550,
            marker="☀️"
        ),

        Zone(
            id=7,
            name="Cazoña – Alisal",
            latitude=43.4581,
            longitude=-3.8414,
            radius=600,
            marker="🚶"
        ),

        Zone(
            id=8,
            name="Monte – Cueto",
            latitude=43.486202253800826,
            longitude=-3.7979554087551213,
            radius=650,
            marker="🌲"
        ),

        Zone(
            id=9,
            name="Calle Alta",
            latitude=43.45898116801386,
            longitude=-3.818183363527089,
            radius=450,
            marker="🚌"
        ),

        Zone(
            id=10,
            name="Cañadío-Puertochico",
            latitude=43.46351972663305,
            longitude=-3.8013836039426367,
            radius=400,
            marker="🍷"
        ),

        Zone(
            id=11,
            name="Plaza Porticada - Plaza de Pombo",
            latitude=43.4621172173889,
            longitude=-3.8062012039427358,
            radius=350,
            marker="🍽️"
        ),

        Zone(
            id=12,
            name="Calderón - Mercado de la Esperanza",
            latitude=43.462859302598325,
            longitude=-3.8099811835254593,
            radius=350,
            marker="🎭"
        ),

        Zone(
            id=13,
            name="Vargas - San Fernando - Burgos",
            latitude=43.4627,
            longitude=-3.8196,
            radius=450,
            marker="🍺"
        ),

        Zone(
            id=14,
            name="Río de la Pila - Hernán Cortés",
            latitude=43.4668,
            longitude=-3.8049,
            radius=350,
            marker="🎵"
        ),

        Zone(
            id=15,
            name="Península de la Magdalena",
            latitude=43.469355406273436,
            longitude=-3.767564435338004,
            radius=700,
            marker="🏰"
        ),

        Zone(
            id=16,
            name="Playa de Mataleñas - Faro Cabo Mayor",
            latitude=43.486043368198565,
            longitude=-3.787880946665848,
            radius=750,
            marker="🏖️"
        ),

        Zone(
            id=17,
            name="Centro Botín - Jardines de Pereda",
            latitude=43.4621,
            longitude=-3.7987,
            radius=400,
            marker="🎨"
        )
    ]