#!/bin/bash

set -e

DIR="./"

echo "Applying manifests from $DIR"

find "$DIR" -maxdepth 1 -name "*.yaml" | sort | while read -r file; do
  echo "→ Applying $(basename "$file")"
  kubectl apply -f "$file"
done

echo "All manifests applied successfully."
