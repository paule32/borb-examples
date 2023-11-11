from decimal import Decimal

from borb.pdf import Document
from borb.pdf import FlexibleColumnWidthTable
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

    # create an OrderedList
    list: OrderedList = (
        OrderedList()
        .add(Paragraph("Item 1"))
        .add(Paragraph("Item 2"))
        .add(Paragraph("Item 4"))
    )

    # create a FlexibleColumnWidthTable
    table: FlexibleColumnWidthTable = (
        FlexibleColumnWidthTable(number_of_columns=3, number_of_rows=2)
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum"))
        .add(list)
        .add(Paragraph("Sit"))
        .add(Paragraph("Amet"))
        .add(Paragraph("Nunc"))
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    )

    layout.add(table)

    # store
    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()
