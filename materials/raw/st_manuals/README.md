# ST Official PDF Mirror

This folder holds repo-local copies of frequently used ST official PDFs.

Use it together with:

- `manifest.json` for file hashes, official URLs, and refresh status.
- `materials/extracted/st_manuals/` for fast local `rg` searches.
- `references/st_manuals_index.md` for routing: which document to use for which kind of question.

Refresh rule:

1. Check the current ST product/document page online.
2. Download the current PDF into this folder, or copy a verified local cache file here if shell download fails.
3. Re-extract text into `materials/extracted/st_manuals/`.
4. Update `manifest.json`, `references/st_manuals_index.md`, and rebuild `vector_store/`.

Safety rule: extracted text is good for retrieval, but PWM, current-sense, OPAMP, comparator, break-input, and electrical-limit decisions must still be checked against the PDF and then verified by the appropriate no-power or current-limited test stage.
