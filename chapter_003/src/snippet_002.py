from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import OrderedList
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import SingleColumnLayout


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add OrderedList of 3 Paragraph objects
    layout.add(
        OrderedList()
        .add(Paragraph("Lorem", font_color=HexColor("45CB85")))
        .add(Paragraph("Ipsum", font_color=HexColor("E08DAC")))
        .add(Paragraph("Dolor", font_color=HexColor("6A7FDB")))
    )

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
