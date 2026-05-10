from services.enrichment.generic_dataset_enricher import (
    enrich_dataset
)


enrich_dataset(

    input_filename="ocio-tiempo-libre.json",

    output_filename="ocio_geocoded.json"
)