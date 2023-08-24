import os

def call_bison(content):
    cmd = f"""                                                                                           tcapelle at Thomas-Capelle-WV3WV6RH3C.local
    curl \
    -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://us-central1-aiplatform.googleapis.com/v1/projects/wandb-growth/locations/us-central1/publishers/google/models/text-bison:predict -d \
    $'{
    "instances": [
        { "prompt": content}
    ],
    "parameters": {
        "temperature": 0.2,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
    }
    }'"""

    return os.system(cmd)
