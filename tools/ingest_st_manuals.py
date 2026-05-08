from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from pypdf import PdfReader
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency: pypdf. Run this script with the bundled Codex Python runtime or install pypdf."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "materials" / "extracted" / "st_manuals"
MANIFEST = ROOT / "materials" / "source_manifest.json"
INDEX = ROOT / "references" / "st_manuals_index.md"
LEGACY_IDS = {"st_an5306_dual_motor_stm32g4"}

MANUALS = [
    {
        "id": "st_an4144_stm32f0_foc_mcsdk",
        "title": "AN4144 - Field-oriented control using STM32F0 and ST Motor Control SDK",
        "role": "FOC and MCSDK background reference",
        "source_path": r"F:\嵌赛\1手册\an4144-fieldoriented-control-using-the-stm32f0-and-the-stmicroelectronics-motor-control-sdk-stmicroelectronics.pdf",
        "notes": "Legacy STM32F0 FOC application note. Useful for MCSDK/FOC concepts, not for STM32G474-specific peripherals.",
    },
    {
        "id": "st_an5306_opamp_stm32g4",
        "title": "AN5306 - Operational Amplifier (OPAMP) usage in STM32G4 Series",
        "role": "STM32G4 OPAMP/current-sense reference",
        "source_path": r"F:\嵌赛\1手册\an5306-dual-motor-control-using-the-stm32g4-stmicroelectronics.pdf",
        "notes": "The local file name mentions dual motor control, but the extracted PDF title is AN5306 OPAMP usage in STM32G4 Series. Use it for OPAMP/PGA/current-sense analog front-end concepts.",
    },
    {
        "id": "st_an5397_sensorless_pmsm_foc",
        "title": "AN5397 - Sensorless PMSM FOC controller",
        "role": "Sensorless FOC algorithm reference",
        "source_path": r"F:\嵌赛\1手册\an5397-sensorless-pmsm-foc-controller-stmicroelectronics.pdf",
        "notes": "High-value sensorless FOC reference. Use for observer/startup concepts before changing project parameters.",
    },
    {
        "id": "st_nucleo_g474re_brief",
        "title": "NUCLEO-G474RE board brief",
        "role": "Board quick reference",
        "source_path": r"F:\嵌赛\1手册\nucleo-g474re.pdf",
        "notes": "Quick board reference for NUCLEO-G474RE. Use with UM2505 for connectors, jumpers, and ST-LINK details.",
    },
    {
        "id": "st_rm0440_stm32g4_reference_manual",
        "title": "RM0440 - STM32G4 Series reference manual",
        "role": "Authoritative STM32G4 peripheral reference",
        "source_path": r"F:\嵌赛\1手册\rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf",
        "notes": "Highest priority for STM32G4 peripheral behavior: TIM1/TIM8, ADC, DMA, DMAMUX, OPAMP, COMP, CORDIC, FMAC, RCC, GPIO, USART.",
    },
    {
        "id": "st_stm32g474re_datasheet",
        "title": "STM32G474RE datasheet",
        "role": "Authoritative MCU electrical and feature reference",
        "source_path": r"F:\嵌赛\1手册\stm32g474re.pdf",
        "notes": "Highest priority for STM32G474RE package, pinout, memory, alternate functions, and electrical limits.",
    },
    {
        "id": "st_um2505_nucleo64_mb1367",
        "title": "UM2505 - STM32 Nucleo-64 boards MB1367 user manual",
        "role": "NUCLEO-G474RE board user manual",
        "source_path": r"F:\嵌赛\1手册\um2505-stm32-nucleo64-boards-mb1367-stmicroelectronics.pdf",
        "notes": "Board-level reference for NUCLEO-64 MB1367: connectors, solder bridges, power, ST-LINK, Arduino and morpho headers.",
    },
    {
        "id": "st_um3027_motor_control_sdk",
        "title": "UM3027 - STM32 Motor Control SDK user manual",
        "role": "MCSDK workflow reference",
        "source_path": r"F:\嵌赛\1手册\um3027-stm32-motor-control-sdk-stmicroelectronics.pdf",
        "notes": "High-value MCSDK reference for Workbench, Motor Profiler, generated project structure, run-time control, and tuning workflow.",
    },
]


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def extract_pdf(manual: dict[str, str], generated_at: str) -> dict[str, object]:
    source = Path(manual["source_path"])
    if not source.exists():
        raise FileNotFoundError(source)

    reader = PdfReader(str(source))
    page_count = len(reader.pages)
    parts = [
        f"# {manual['title']}",
        "",
        f"Source path: {source}",
        f"Role: {manual['role']}",
        f"Pages: {page_count}",
        f"Extracted at: {generated_at}",
        "",
        "Extraction note: text was extracted with pypdf for local retrieval. Use the original PDF for figures, tables, electrical limits, and final page citations.",
        "",
    ]

    for index, page in enumerate(reader.pages, start=1):
        try:
            text = clean_text(page.extract_text() or "")
        except Exception as exc:  # pragma: no cover - defensive for malformed PDF pages
            text = f"[text extraction failed on page {index}: {exc}]"
        if text:
            parts.extend([f"\n\n--- Page {index} ---\n", text])

    output = OUT_DIR / f"{manual['id']}.txt"
    output.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")
    characters = len(output.read_text(encoding="utf-8", errors="ignore"))
    return {
        "id": manual["id"],
        "title": manual["title"],
        "role": manual["role"],
        "kind": "pdf",
        "source_path": str(source),
        "extracted_file": str(output),
        "pages": page_count,
        "characters": characters,
        "notes": manual["notes"],
    }


def update_manifest(entries: list[dict[str, object]], generated_at: str) -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    sources = data.get("sources", [])
    entry_ids = {entry["id"] for entry in entries} | LEGACY_IDS
    sources = [source for source in sources if source.get("id") not in entry_ids]
    sources.extend(entries)
    data["generated_at"] = generated_at
    data["workspace"] = str(ROOT.parent)
    data["sources"] = sources
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_index(entries: list[dict[str, object]], generated_at: str) -> None:
    lines = [
        "# ST Official Manuals Index",
        "",
        f"Generated at: {generated_at}",
        "",
        "These are local text extractions of official ST PDF manuals/application notes. Use the `.txt` files for fast local retrieval, but use the original PDFs for figures, tables, exact page citations, and safety-critical electrical values.",
        "",
        "## Added Sources",
        "",
        "| ID | Document | Role | Pages | Extracted text | Original PDF |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for entry in entries:
        source = str(entry["source_path"]).replace("|", "\\|")
        lines.append(
            f"| `{entry['id']}` | {entry['title']} | {entry['role']} | {entry['pages']} | {entry['characters']} chars | `{source}` |"
        )

    lines.extend(
        [
            "",
            "## Retrieval Guidance",
            "",
            "- For STM32G474 peripheral behavior, prefer `st_rm0440_stm32g4_reference_manual`.",
            "- For STM32G474RE pinout, package, alternate functions, and electrical limits, prefer `st_stm32g474re_datasheet`.",
            "- For MCSDK workflow, generated project structure, Motor Profiler, and tuning flow, prefer `st_um3027_motor_control_sdk`.",
            "- For NUCLEO-G474RE board connectors, power, jumpers, and ST-LINK details, prefer `st_um2505_nucleo64_mb1367` plus `st_nucleo_g474re_brief`.",
            "- For STM32G4 OPAMP/PGA/current-sense analog front-end concepts, prefer `st_an5306_opamp_stm32g4`.",
            "- For sensorless FOC concepts, observer/startup flow, and algorithm background, prefer `st_an5397_sensorless_pmsm_foc`.",
            "- Treat `st_an4144_stm32f0_foc_mcsdk` as background only when it conflicts with STM32G4-specific documents.",
            "",
            "## Safety Note",
            "",
            "Do not change PWM, dead-time, over-current, ADC current-sense, OPAMP, comparator, or startup parameters from extracted text alone. Confirm against the original PDF and then validate with current-limited, instrumented tests.",
            "",
        ]
    )
    INDEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    generated_at = datetime.now().replace(microsecond=0).isoformat()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for legacy_id in LEGACY_IDS:
        legacy_file = OUT_DIR / f"{legacy_id}.txt"
        if legacy_file.exists():
            legacy_file.unlink()
    entries = []
    for manual in MANUALS:
        print(f"extracting {manual['id']} ...")
        entries.append(extract_pdf(manual, generated_at))

    update_manifest(entries, generated_at)
    write_index(entries, generated_at)
    print(f"extracted {len(entries)} manuals to {OUT_DIR}")
    print(f"updated {MANIFEST}")
    print(f"wrote {INDEX}")


if __name__ == "__main__":
    main()
