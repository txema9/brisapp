from backend.services.enrichment.generic_dataset_enricher import (
    enrich_dataset
)


enrich_dataset(

    input_filename="salud.json",

    output_filename="salud_geocoded.json"
)