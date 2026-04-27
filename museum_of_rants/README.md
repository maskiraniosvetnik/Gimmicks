# Museum of Human Suffering
### Artifact Intake Terminal v1.0

A terminal program that transforms emotional vents and rants into museum exhibit entries, catalogued with curatorial gravitas.

## Structure

```
museum/
├── main.py       # Entry point and main loop
├── logic.py      # Emotion detection and artifact generation
├── display.py    # Terminal rendering and gallery browser
├── archive.py    # JSON persistence (save/load)
└── data.py       # All keyword pools and string lists
```

## Usage

```bash
python main.py
```

- Type your grievance at the prompt
- The system detects your emotional state and generates a museum exhibit
- Save artifacts to browse later via the `gallery` command
- Type `exit`, `quit`, or `q` to leave

## Commands

| Input     | Action                        |
|-----------|-------------------------------|
| (any text)| Generate artifact from input  |
| `gallery` | Browse saved artifacts        |
| `q`       | Quit                          |

## Anomalies

Rare random events that distort the exhibit display:

| Anomaly     | Effect                              |
|-------------|-------------------------------------|
| GLITCH      | Vowels replaced with `#`            |
| REDACTED    | Random words replaced with `███`    |
| ECHO        | Description repeats itself          |
| CORRUPTED   | Description rendered in reverse     |
| FORBIDDEN   | Entire record expunged              |
| UNSTABLE    | Flagged, no further effect          |
| FRAGMENTED  | Flagged, no further effect          |

## Data

All pools are in `data.py` and can be expanded freely:
- `EMOTION_KEYWORDS` — detection triggers per emotion
- `EMOTION_POOLS` — description phrases per emotion
- `ARTIFACT_NOUNS` — title nouns per emotion
- `DRAMATIC_ADJECTIVES` — title prefixes
- `SUBTITLES`, `WING_NAMES`, `CURATOR_NOTES`, `FOOTNOTES`, `SIGNIFICANCE_PHRASES` — exhibit metadata
