import argparse
from parser import process_file, process_directory

# ----------- CLI Interface -----------

def main():
    parser = argparse.ArgumentParser(description="Obsidian-to-Anki Flashcard Generator")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--dir', help='Path to folder of markdown notes')
    group.add_argument('--note', help='Path to a single markdown note')

    parser.add_argument('--output', default='anki.txt', help='Path to output .txt file (default: anki.txt)')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite output file instead of appending')

    args = parser.parse_args()

    if args.note:
        process_file(args.note, args.output, overwrite=args.overwrite)
    else:
        process_directory(args.dir, args.output, overwrite=args.overwrite)

    print(f"\n✅ Finished! Flashcards written to {args.output}")

if __name__ == "__main__":
    main()