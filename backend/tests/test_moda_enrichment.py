from backend.services.enrichment.generic_dataset_enricher import (
    enrich_dataset
)


enrich_dataset(

    input_filename="moda-complementos.json",

    output_filename="moda_geocoded.json"
)