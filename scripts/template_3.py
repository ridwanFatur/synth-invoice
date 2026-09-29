import random

from PIL import Image, ImageDraw, ImageFont


def create_invoice_template_3(
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

    # =========================================================
    # RANDOM COLORS
    # =========================================================

    color_palettes = [
        {
            "primary": "#2563EB",      # blue
            "secondary": "#60A5FA",
            "light": "#EFF6FF",
            "accent": "#DBEAFE",
        },
        {
            "primary": "#16A34A",      # green
            "secondary": "#4ADE80",
            "light": "#F0FDF4",
            "accent": "#DCFCE7",
        },
        {
            "primary": "#DC2626",      # red
            "secondary": "#F87171",
            "light": "#FEF2F2",
            "accent": "#FEE2E2",
        },
        {
            "primary": "#7C3AED",      # purple
            "secondary": "#A78BFA",
            "light": "#F5F3FF",
            "accent": "#EDE9FE",
        },
        {
            "primary": "#EA580C",      # orange
            "secondary": "#FB923C",
            "light": "#FFF7ED",
            "accent": "#FFEDD5",
        },
        {
            "primary": "#0891B2",      # cyan
            "secondary": "#22D3EE",
            "light": "#ECFEFF",
            "accent": "#CFFAFE",
        },
        {
            "primary": "#DB2777",      # pink
            "secondary": "#F472B6",
            "light": "#FDF2F8",
            "accent": "#FCE7F3",
        },
    ]

    palette = random.choice(color_palettes)

    primary_color = palette["primary"]
    secondary_color = palette["secondary"]
    light_color = palette["light"]
    accent_color = palette["accent"]

    background_color = "white"
    text_color = "#222222"
    secondary_text_color = "#666666"
    line_color = "#DDDDDD"

    # =========================================================
    # FONTS
    # =========================================================

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
        40,
    )

    # =========================================================
    # IMAGE
    # =========================================================

    image = Image.new(
        "RGB",
        (width, height),
        background_color,
    )

    draw = ImageDraw.Draw(image)

    margin = 50
    content_width = width - margin * 2

    # =========================================================
    # HELPER
    # =========================================================

    def draw_label_value(
        x,
        y,
        label,
        value,
        label_width=90,
        value_color=text_color,
    ):
        draw.text(
            (x, y),
            label,
            font=small_bold_font,
            fill=secondary_text_color,
        )

        draw.text(
            (x + label_width, y),
            value,
            font=small_font,
            fill=value_color,
        )

    # =========================================================
    # TOP COLOR BAR
    # =========================================================

    draw.rectangle(
        (
            0,
            0,
            width,
            18,
        ),
        fill=primary_color,
    )

    # Small colorful blocks
    block_width = width // 5

    random_colors = [
        primary_color,
        secondary_color,
        "#F59E0B",
        "#10B981",
        "#8B5CF6",
    ]

    random.shuffle(random_colors)

    for index, color in enumerate(random_colors):
        draw.rectangle(
            (
                index * block_width,
                0,
                (index + 1) * block_width,
                18,
            ),
            fill=color,
        )

    # =========================================================
    # HEADER
    # =========================================================

    y = 50

    draw.text(
        (margin, y),
        "INVOICE",
        font=title_font,
        fill=primary_color,
    )

    draw.text(
        (margin, y + 52),
        "Thank you for choosing our services.",
        font=small_font,
        fill=secondary_text_color,
    )

    # Invoice number
    invoice_box_x = 500
    invoice_box_y = 50
    invoice_box_width = 250
    invoice_box_height = 125

    draw.rounded_rectangle(
        (
            invoice_box_x,
            invoice_box_y,
            invoice_box_x + invoice_box_width,
            invoice_box_y + invoice_box_height,
        ),
        radius=12,
        fill=light_color,
        outline=accent_color,
        width=2,
    )

    draw.text(
        (
            invoice_box_x + 20,
            invoice_box_y + 15,
        ),
        "INVOICE",
        font=small_bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            invoice_box_x + 20,
            invoice_box_y + 42,
        ),
        invoice_no,
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            invoice_box_x + 20,
            invoice_box_y + 78,
        ),
        "DATE",
        font=small_bold_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            invoice_box_x + 80,
            invoice_box_y + 78,
        ),
        invoice_date,
        font=small_font,
        fill=text_color,
    )

    y = 205

    # =========================================================
    # FROM / BILL TO
    # =========================================================

    column_gap = 25
    column_width = (
        content_width - column_gap
    ) // 2

    from_x = margin
    bill_to_x = margin + column_width + column_gap

    # FROM colored header
    draw.rectangle(
        (
            from_x,
            y,
            from_x + column_width,
            y + 40,
        ),
        fill=primary_color,
    )

    draw.text(
        (
            from_x + 15,
            y + 11,
        ),
        "FROM",
        font=small_bold_font,
        fill="white",
    )

    # BILL TO colored header
    draw.rectangle(
        (
            bill_to_x,
            y,
            bill_to_x + column_width,
            y + 40,
        ),
        fill=secondary_color,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 11,
        ),
        "BILL TO",
        font=small_bold_font,
        fill="white",
    )

    y += 40

    party_box_height = 145

    # FROM box
    draw.rectangle(
        (
            from_x,
            y,
            from_x + column_width,
            y + party_box_height,
        ),
        fill=light_color,
        outline=accent_color,
        width=1,
    )

    draw.text(
        (
            from_x + 15,
            y + 15,
        ),
        from_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            from_x + 15,
            y + 45,
        ),
        from_to["address"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            from_x + 15,
            y + 68,
        ),
        from_to["city"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            from_x + 15,
            y + 91,
        ),
        from_to["phone"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            from_x + 15,
            y + 114,
        ),
        from_to["email"],
        font=small_font,
        fill=secondary_text_color,
    )

    # BILL TO box
    draw.rectangle(
        (
            bill_to_x,
            y,
            bill_to_x + column_width,
            y + party_box_height,
        ),
        fill="#FAFAFA",
        outline=line_color,
        width=1,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 15,
        ),
        bill_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 45,
        ),
        bill_to["address"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 68,
        ),
        bill_to["city"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 91,
        ),
        bill_to["phone"],
        font=small_font,
        fill=secondary_text_color,
    )

    draw.text(
        (
            bill_to_x + 15,
            y + 114,
        ),
        bill_to["email"],
        font=small_font,
        fill=secondary_text_color,
    )

    y += party_box_height + 35

    # =========================================================
    # ITEMS TITLE
    # =========================================================

    draw.text(
        (margin, y),
        "ITEM DETAILS",
        font=bold_font,
        fill=text_color,
    )

    # Decorative colored line
    draw.rectangle(
        (
            margin + 145,
            y + 8,
            margin + 260,
            y + 13,
        ),
        fill=primary_color,
    )

    draw.rectangle(
        (
            margin + 265,
            y + 8,
            margin + 300,
            y + 13,
        ),
        fill="#F59E0B",
    )

    y += 38

    # =========================================================
    # TABLE
    # =========================================================

    table_x = margin
    table_width = content_width

    col_description = 320
    col_qty = 80
    col_price = 150
    col_total = (
        table_width
        - col_description
        - col_qty
        - col_price
    )

    header_height = 42
    row_height = 48

    # Header
    draw.rounded_rectangle(
        (
            table_x,
            y,
            table_x + table_width,
            y + header_height,
        ),
        radius=7,
        fill=primary_color,
    )

    draw.text(
        (
            table_x + 12,
            y + 12,
        ),
        "DESCRIPTION",
        font=small_bold_font,
        fill="white",
    )

    draw.text(
        (
            table_x + col_description + 10,
            y + 12,
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
            y + 12,
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
            y + 12,
        ),
        "TOTAL",
        font=small_bold_font,
        fill="white",
    )

    y += header_height

    # Rows
    row_colors = [
        "white",
        light_color,
        "#FAFAFA",
    ]

    for index, item in enumerate(items):
        row_color = row_colors[index % len(row_colors)]

        draw.rectangle(
            (
                table_x,
                y,
                table_x + table_width,
                y + row_height,
            ),
            fill=row_color,
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
                table_x + col_description + 10,
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
            font=small_bold_font,
            fill=primary_color,
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
    # TOTAL SECTION
    # =========================================================

    y += 25

    total_width = 330
    total_x = width - margin - total_width

    draw.rounded_rectangle(
        (
            total_x,
            y,
            width - margin,
            y + 75,
        ),
        radius=10,
        fill=primary_color,
    )

    draw.text(
        (
            total_x + 20,
            y + 24,
        ),
        "SUBTOTAL",
        font=bold_font,
        fill="white",
    )

    draw.text(
        (
            total_x + 165,
            y + 24,
        ),
        f"{subtotal:,.2f}",
        font=bold_font,
        fill="white",
    )

    y += 110

    # =========================================================
    # NOTE
    # =========================================================

    note_width = 330

    draw.text(
        (
            margin,
            y,
        ),
        "NOTE",
        font=bold_font,
        fill=primary_color,
    )

    draw.rectangle(
        (
            margin,
            y + 30,
            margin + 5,
            y + 100,
        ),
        fill=secondary_color,
    )

    draw.text(
        (
            margin + 18,
            y + 38,
        ),
        note,
        font=small_font,
        fill=secondary_text_color,
    )

    # =========================================================
    # PAYMENT INFORMATION
    # =========================================================

    payment_x = 430

    draw.text(
        (
            payment_x,
            y,
        ),
        "PAYMENT INFORMATION",
        font=bold_font,
        fill=primary_color,
    )

    draw_label_value(
        payment_x,
        y + 35,
        "Bank",
        payment_information["bank"],
        label_width=90,
    )

    draw_label_value(
        payment_x,
        y + 60,
        "Account",
        payment_information["account_name"],
        label_width=90,
    )

    draw_label_value(
        payment_x,
        y + 85,
        "Account No.",
        payment_information["account_number"],
        label_width=90,
    )

    draw_label_value(
        payment_x,
        y + 110,
        "Email",
        payment_information["email"],
        label_width=90,
    )

    # =========================================================
    # FOOTER
    # =========================================================

    footer_y = height - 70

    draw.rectangle(
        (
            0,
            footer_y,
            width,
            height,
        ),
        fill=primary_color,
    )

    draw.text(
        (
            margin,
            footer_y + 17,
        ),
        "Thank you for your business.",
        font=small_font,
        fill="white",
    )

    draw.text(
        (
            width - margin - 150,
            footer_y + 17,
        ),
        "PAYMENT RECEIPT",
        font=small_bold_font,
        fill="white",
    )

    return image

def example_template_3():
    invoice = create_invoice_template_3(
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