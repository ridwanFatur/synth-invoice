from PIL import Image, ImageChops, ImageDraw, ImageFont

def create_invoice_template_1(
    bill_to,
    invoice_date,
    invoice_no,
    from_to,
    items,
    subtotal,
    note,
    payment_information,
):
    width = 800
    height = 1200

    background_color = "white"
    text_color = "black"
    secondary_color = "#666666"
    line_color = "#CCCCCC"

    regular_font = ImageFont.truetype(
        "./fonts/Roboto-Regular.ttf",
        18,
    )
    bold_font = ImageFont.truetype(
        "./fonts/Roboto-Bold.ttf",
        18,
    )
    small_font = ImageFont.truetype(
        "./fonts/Roboto-Regular.ttf",
        14,
    )
    small_bold_font = ImageFont.truetype(
        "./fonts/Roboto-Bold.ttf",
        14,
    )
    title_font = ImageFont.truetype(
        "./fonts/Roboto-Bold.ttf",
        32,
    )

    image = Image.new(
        "RGB",
        (width, height),
        background_color,
    )
    draw = ImageDraw.Draw(image)

    margin = 50
    content_width = width - (margin * 2)

    def draw_label_value(
        x,
        y,
        label,
        value,
        label_width=100,
    ):
        draw.text(
            (x, y),
            label,
            font=small_bold_font,
            fill=text_color,
        )
        draw.text(
            (x + label_width, y),
            value,
            font=small_font,
            fill=text_color,
        )

    def draw_section_title(x, y, title):
        draw.text(
            (x, y),
            title,
            font=bold_font,
            fill=text_color,
        )

    y = 45

    draw.text(
        (margin, y),
        "INVOICE",
        font=title_font,
        fill=text_color,
    )

    invoice_info_x = 520

    draw_label_value(
        invoice_info_x,
        y,
        "Invoice No.",
        invoice_no,
        label_width=80,
    )
    draw_label_value(
        invoice_info_x,
        y + 28,
        "Date",
        invoice_date,
        label_width=80,
    )

    y += 80

    draw.line(
        (margin, y, width - margin, y),
        fill=line_color,
        width=2,
    )

    y += 30

    column_gap = 40
    column_width = (content_width - column_gap) // 2

    from_x = margin
    bill_to_x = margin + column_width + column_gap

    draw_section_title(
        from_x,
        y,
        "FROM",
    )
    draw_section_title(
        bill_to_x,
        y,
        "BILL TO",
    )

    y += 32

    draw.text(
        (from_x, y),
        from_to["name"],
        font=bold_font,
        fill=text_color,
    )
    draw.text(
        (from_x, y + 28),
        from_to["address"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (from_x, y + 50),
        from_to["city"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (from_x, y + 72),
        from_to["phone"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (from_x, y + 94),
        from_to["email"],
        font=small_font,
        fill=secondary_color,
    )

    draw.text(
        (bill_to_x, y),
        bill_to["name"],
        font=bold_font,
        fill=text_color,
    )
    draw.text(
        (bill_to_x, y + 28),
        bill_to["address"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (bill_to_x, y + 50),
        bill_to["city"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (bill_to_x, y + 72),
        bill_to["phone"],
        font=small_font,
        fill=secondary_color,
    )
    draw.text(
        (bill_to_x, y + 94),
        bill_to["email"],
        font=small_font,
        fill=secondary_color,
    )

    y += 145

    table_x = margin
    table_width = content_width

    col_description = 340
    col_qty = 80
    col_price = 130
    col_total = 150

    header_height = 40
    row_height = 42

    draw.rectangle(
        (
            table_x,
            y,
            table_x + table_width,
            y + header_height,
        ),
        fill="#EEEEEE",
    )

    draw.text(
        (table_x + 10, y + 11),
        "DESCRIPTION",
        font=small_bold_font,
        fill=text_color,
    )
    draw.text(
        (
            table_x + col_description + 10,
            y + 11,
        ),
        "QTY",
        font=small_bold_font,
        fill=text_color,
    )
    draw.text(
        (
            table_x + col_description + col_qty + 10,
            y + 11,
        ),
        "PRICE",
        font=small_bold_font,
        fill=text_color,
    )
    draw.text(
        (
            table_x + col_description + col_qty + col_price + 10,
            y + 11,
        ),
        "TOTAL",
        font=small_bold_font,
        fill=text_color,
    )

    y += header_height

    for item in items:
        draw.line(
            (
                table_x,
                y,
                table_x + table_width,
                y,
            ),
            fill=line_color,
            width=1,
        )

        draw.text(
            (table_x + 10, y + 12),
            item["description"],
            font=small_font,
            fill=text_color,
        )
        draw.text(
            (
                table_x + col_description + 10,
                y + 12,
            ),
            str(item["qty"]),
            font=small_font,
            fill=text_color,
        )
        draw.text(
            (
                table_x + col_description + col_qty + 10,
                y + 12,
            ),
            f"{item['price']:,.2f}",
            font=small_font,
            fill=text_color,
        )
        draw.text(
            (
                table_x + col_description + col_qty + col_price + 10,
                y + 12,
            ),
            f"{item['total']:,.2f}",
            font=small_font,
            fill=text_color,
        )

        y += row_height

    draw.line(
        (
            table_x,
            y,
            table_x + table_width,
            y,
        ),
        fill=line_color,
        width=1,
    )

    y += 25

    subtotal_x = 560

    draw.text(
        (subtotal_x, y),
        "SUBTOTAL",
        font=bold_font,
        fill=text_color,
    )
    draw.text(
        (subtotal_x + 120, y),
        f"{subtotal:,.2f}",
        font=bold_font,
        fill=text_color,
    )

    y += 50

    draw.line(
        (
            subtotal_x,
            y,
            width - margin,
            y,
        ),
        fill=text_color,
        width=2,
    )

    y += 30

    draw_section_title(
        margin,
        y,
        "NOTE",
    )

    y += 30

    draw.text(
        (margin, y),
        note,
        font=small_font,
        fill=secondary_color,
    )

    y += 60

    draw_section_title(
        margin,
        y,
        "PAYMENT INFORMATION",
    )

    y += 35

    draw_label_value(
        margin,
        y,
        "Bank",
        payment_information["bank"],
    )
    draw_label_value(
        margin,
        y + 25,
        "Account",
        payment_information["account_name"],
    )
    draw_label_value(
        margin,
        y + 50,
        "Account No.",
        payment_information["account_number"],
    )
    draw_label_value(
        margin,
        y + 75,
        "Email",
        payment_information["email"],
    )

    draw.line(
        (
            margin,
            height - 70,
            width - margin,
            height - 70,
        ),
        fill=line_color,
        width=1,
    )

    footer_text = "Thank you for your business."

    draw.text(
        (margin, height - 50),
        footer_text,
        font=small_font,
        fill=secondary_color,
    )

    return image

def example_template_1():
    invoice = create_invoice_template_1(
        bill_to={
            "name": "PT Maju Jaya",
            "address": "Jl. Merdeka No. 123",
            "city": "Bandung, Indonesia",
            "phone": "+62 812-3456-7890",
            "email": "finance@majujaya.com",
        },
        invoice_date="29 September 2026",
        invoice_no="INV-2026-00921",
        from_to={
            "name": "PT Digital Nusantara",
            "address": "Jl. Asia Afrika No. 10",
            "city": "Bandung, Indonesia",
            "phone": "+62 811-2222-3333",
            "email": "billing@digitalnusantara.com",
        },
        items=[
            {
                "description": "Software Development",
                "qty": 10,
                "price": 150_000,
                "total": 1_500_000,
            },
            {
                "description": "Cloud Infrastructure",
                "qty": 1,
                "price": 750_000,
                "total": 750_000,
            },
            {
                "description": "Technical Support",
                "qty": 5,
                "price": 100_000,
                "total": 500_000,
            },
        ],
        subtotal=2_750_000,
        note="Payment is due within 30 days from the invoice date.",
        payment_information={
            "bank": "Bank Mandiri",
            "account_name": "PT Digital Nusantara",
            "account_number": "1234567890",
            "email": "billing@digitalnusantara.com",
        },
    )   
    return invoice 