# Interactive YouTube Audio Downloader

A minimal CLI tool to search YouTube tracks by title and download local audio files using `yt-dlp` and `FFmpeg`.

## Features
- **Keyword Search:** Query tracks directly without copying video URLs[cite: 1].
- **Result Selection:** Choose 1 track from top 5 search matches[cite: 1].
- **Audio Output:** Converts stream to `.wav` (default) or `.mp3` format[cite: 1, 2].
- **Local Storage:** Outputs files directly to `./output/`[cite: 2].

## Structure
- `core.py`: Base `yt-dlp` extraction class[cite: 3].
- `youtube.py`: Download & query settings[cite: 2].
- `main.py`: CLI search menu loop[cite: 1].
- `ffmpeg_bin/`: Directory containing your local `ffmpeg` executable[cite: 2].
- `output/`: Folder where downloaded audio is stored[cite: 2].

## Quick Start
1. Install dependency:
   ```bash
   pip install yt-dlp
   ```
2. Run:
   ```bash
   python main.py
   ```
   
# Note
This project was made after i learn basic python from [Dicoding](dicoding.com) with less AI help, nothing special about it.
