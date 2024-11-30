from pypdf import PdfReader, PdfWriter
import argparse


def create_booklet(input_pdf, output_pdf):
    # Load the input PDF
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    # Calculate number of pages needed (must be a multiple of 4 for a booklet)
    if total_pages % 4 != 0:
        raise ValueError(f"Document has {total_pages}, which is not a multiple of 4")

    writer = PdfWriter()

    # Rearrange pages into booklet order
    for i in range(0, total_pages // 2):
        last_index = total_pages - i - 1

        # Pages
        left = reader.pages[i]
        right = reader.pages[last_index]

        # Swap order when needed
        if i % 2 == 0:
            left, right = right, left

        pageWidth = left.mediabox.width

        # Translate right page by left page's width and then merge
        left.merge_translated_page(right, pageWidth, 0, expand=True)

        # Add page to result
        writer.add_page(left)

    # Save the rearranged PDF
    with open(output_pdf, "wb") as output:
        writer.write(output)


# Setup arguments
parser = argparse.ArgumentParser(description="Create booklet from pdf")
parser.add_argument("input", help="Input PDF file")
parser.add_argument("output", help="Output PDF file")

# Parse and run
args = parser.parse_args()
create_booklet(args.input, args.output)
