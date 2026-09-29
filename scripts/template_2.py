from PIL import Image, ImageDraw, ImageFont


def create_invoice_template_2(
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
    header_color = "#222222"
    light_color = "#F3F3F3"

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
        38,
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
        label_width=90,
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

    def draw_party_box(
        x,
        y,
        box_width,
        title,
        data,
    ):
        box_height = 165

        draw.rectangle(
            (
                x,
                y,
                x + box_width,
                y + box_height,
            ),
            fill=light_color,
            outline=line_color,
            width=1,
        )

        draw.text(
            (x + 18, y + 15),
            title,
            font=small_bold_font,
            fill=text_color,
        )

        draw.line(
            (
                x + 18,
                y + 42,
                x + box_width - 18,
                y + 42,
            ),
            fill=line_color,
            width=1,
        )

        draw.text(
            (x + 18, y + 57),
            data["name"],
            font=bold_font,
            fill=text_color,
        )

        draw.text(
            (x + 18, y + 86),
            data["address"],
            font=small_font,
            fill=secondary_color,
        )

        draw.text(
            (x + 18, y + 108),
            data["city"],
            font=small_font,
            fill=secondary_color,
        )

        draw.text(
            (x + 18, y + 130),
            data["phone"],
            font=small_font,
            fill=secondary_color,
        )

        draw.text(
            (
                x + box_width // 2,
                y + 130,
            ),
            data["email"],
            font=small_font,
            fill=secondary_color,
        )

        return box_height

    # =========================================================
    # HEADER
    # =========================================================

    y = 45

    draw.text(
        (margin, y),
        "INVOICE",
        font=title_font,
        fill=text_color,
    )

    draw.text(
        (margin, y + 48),
        "Professional services invoice",
        font=small_font,
        fill=secondary_color,
    )

    # Invoice metadata box
    info_width = 300
    info_height = 85
    info_x = width - margin - info_width
    info_y = 38

    draw.rectangle(
        (
            info_x,
            info_y,
            info_x + info_width,
            info_y + info_height,
        ),
        fill=light_color,
        outline=line_color,
        width=1,
    )

    draw.text(
        (info_x + 15, info_y + 13),
        "INVOICE NO.",
        font=small_bold_font,
        fill=secondary_color,
    )

    draw.text(
        (info_x + 130, info_y + 13),
        invoice_no,
        font=small_bold_font,
        fill=text_color,
    )

    draw.text(
        (info_x + 15, info_y + 47),
        "DATE",
        font=small_bold_font,
        fill=secondary_color,
    )

    draw.text(
        (info_x + 130, info_y + 47),
        invoice_date,
        font=small_font,
        fill=text_color,
    )

    y = 150

    draw.line(
        (
            margin,
            y,
            width - margin,
            y,
        ),
        fill=text_color,
        width=2,
    )

    y += 30

    # =========================================================
    # FROM / BILL TO
    # =========================================================

    gap = 25
    box_width = (content_width - gap) // 2

    draw_party_box(
        margin,
        y,
        box_width,
        "FROM",
        from_to,
    )

    draw_party_box(
        margin + box_width + gap,
        y,
        box_width,
        "BILL TO",
        bill_to,
    )

    y += 195

    # =========================================================
    # ITEMS TABLE
    # =========================================================

    table_x = margin
    table_width = content_width

    col_description = 330
    col_qty = 80
    col_price = 150
    col_total = (
        table_width
        - col_description
        - col_qty
        - col_price
    )

    header_height = 45
    row_height = 48

    # Table header
    draw.rectangle(
        (
            table_x,
            y,
            table_x + table_width,
            y + header_height,
        ),
        fill=header_color,
    )

    draw.text(
        (table_x + 12, y + 13),
        "DESCRIPTION",
        font=small_bold_font,
        fill="white",
    )

    draw.text(
        (
            table_x + col_description + 10,
            y + 13,
        ),
        "QTY",
        font=small_bold_font,
        fill="white",
    )

    draw.text(
        (
            table_x
            + col_description
            + col_qty
            + 10,
            y + 13,
        ),
        "PRICE",
        font=small_bold_font,
        fill="white",
    )

    draw.text(
        (
            table_x
            + col_description
            + col_qty
            + col_price
            + 10,
            y + 13,
        ),
        "TOTAL",
        font=small_bold_font,
        fill="white",
    )

    y += header_height

    # Table rows
    for index, item in enumerate(items):
        if index % 2 == 0:
            draw.rectangle(
                (
                    table_x,
                    y,
                    table_x + table_width,
                    y + row_height,
                ),
                fill="#FAFAFA",
            )

        draw.text(
            (
                table_x + 12,
                y + 14,
            ),
            item["description"],
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                table_x
                + col_description
                + 10,
                y + 14,
            ),
            str(item["qty"]),
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                table_x
                + col_description
                + col_qty
                + 10,
                y + 14,
            ),
            f"{item['price']:,.2f}",
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                table_x
                + col_description
                + col_qty
                + col_price
                + 10,
                y + 14,
            ),
            f"{item['total']:,.2f}",
            font=small_font,
            fill=text_color,
        )

        draw.line(
            (
                table_x,
                y + row_height,
                table_x + table_width,
                y + row_height,
            ),
            fill=line_color,
            width=1,
        )

        y += row_height

    # =========================================================
    # TOTAL
    # =========================================================

    y += 25

    summary_width = 300
    summary_x = width - margin - summary_width

    draw.rectangle(
        (
            summary_x,
            y,
            width - margin,
            y + 65,
        ),
        fill=light_color,
        outline=line_color,
        width=1,
    )

    draw.text(
        (
            summary_x + 18,
            y + 21,
        ),
        "SUBTOTAL",
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            summary_x + 145,
            y + 21,
        ),
        f"{subtotal:,.2f}",
        font=bold_font,
        fill=text_color,
    )

    y += 100

    # =========================================================
    # NOTE + PAYMENT INFORMATION
    # =========================================================

    bottom_gap = 30
    bottom_width = (
        content_width - bottom_gap
    ) // 2

    # NOTE
    note_x = margin

    draw.text(
        (note_x, y),
        "NOTE",
        font=bold_font,
        fill=text_color,
    )

    draw.line(
        (
            note_x,
            y + 30,
            note_x + bottom_width,
            y + 30,
        ),
        fill=line_color,
        width=1,
    )

    draw.text(
        (
            note_x,
            y + 45,
        ),
        note,
        font=small_font,
        fill=secondary_color,
    )

    # PAYMENT INFORMATION
    payment_x = (
        margin
        + bottom_width
        + bottom_gap
    )

    draw.text(
        (payment_x, y),
        "PAYMENT INFORMATION",
        font=bold_font,
        fill=text_color,
    )

    draw.line(
        (
            payment_x,
            y + 30,
            width - margin,
            y + 30,
        ),
        fill=line_color,
        width=1,
    )

    draw_label_value(
        payment_x,
        y + 45,
        "Bank",
        payment_information["bank"],
        label_width=80,
    )

    draw_label_value(
        payment_x,
        y + 70,
        "Account",
        payment_information["account_name"],
        label_width=80,
    )

    draw_label_value(
        payment_x,
        y + 95,
        "Account No.",
        payment_information["account_number"],
        label_width=80,
    )

    draw_label_value(
        payment_x,
        y + 120,
        "Email",
        payment_information["email"],
        label_width=80,
    )

    # =========================================================
    # FOOTER
    # =========================================================

    footer_y = height - 65

    draw.line(
        (
            margin,
            footer_y,
            width - margin,
            footer_y,
        ),
        fill=line_color,
        width=1,
    )

    draw.text(
        (
            margin,
            footer_y + 15,
        ),
        "Thank you for your business.",
        font=small_font,
        fill=secondary_color,
    )

    return image

def example_template_2():
    invoice = create_invoice_template_2(
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