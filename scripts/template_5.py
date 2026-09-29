import random

from PIL import Image, ImageDraw, ImageFont


def draw_label_value(
    draw,
    x,
    y,
    label,
    value,
    label_width=70,
    label_font=None,
    value_font=None,
    label_color="#666666",
    value_color="#222222",
):
    draw.text(
        (x, y),
        label,
        font=label_font,
        fill=label_color,
    )

    draw.text(
        (x + label_width, y),
        value,
        font=value_font,
        fill=value_color,
    )


def create_invoice_template_5(
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
    # RANDOM COLOR PALETTE
    # =========================================================

    palettes = [
        {
            "primary": "#2563EB",
            "secondary": "#06B6D4",
            "accent": "#F59E0B",
            "extra": "#8B5CF6",
            "light": "#EFF6FF",
        },
        {
            "primary": "#16A34A",
            "secondary": "#14B8A6",
            "accent": "#EAB308",
            "extra": "#2563EB",
            "light": "#F0FDF4",
        },
        {
            "primary": "#DC2626",
            "secondary": "#F97316",
            "accent": "#F59E0B",
            "extra": "#DB2777",
            "light": "#FEF2F2",
        },
        {
            "primary": "#7C3AED",
            "secondary": "#DB2777",
            "accent": "#F59E0B",
            "extra": "#06B6D4",
            "light": "#F5F3FF",
        },
        {
            "primary": "#0891B2",
            "secondary": "#2563EB",
            "accent": "#8B5CF6",
            "extra": "#F97316",
            "light": "#ECFEFF",
        },
        {
            "primary": "#DB2777",
            "secondary": "#9333EA",
            "accent": "#F97316",
            "extra": "#14B8A6",
            "light": "#FDF2F8",
        },
    ]

    palette = random.choice(palettes)

    primary_color = palette["primary"]
    secondary_color = palette["secondary"]
    accent_color = palette["accent"]
    extra_color = palette["extra"]
    light_color = palette["light"]

    text_color = "#222222"
    secondary_text = "#666666"
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
        44,
    )

    huge_font = ImageFont.truetype(
        "./fonts/Roboto-Bold.ttf",
        60,
    )

    # =========================================================
    # RANDOM LAYOUT SETTINGS
    # =========================================================

    margin_left = random.choice([45, 55, 65])
    margin_right = random.choice([45, 55, 65])

    content_left = margin_left
    content_right = width - margin_right

    # Header height varies slightly
    header_height = random.choice([165, 180, 195])

    # Random accent orientation
    accent_direction = random.choice(
        [
            "top",
            "left",
            "right",
        ]
    )

    # Random table style
    table_style = random.choice(
        [
            "rounded",
            "stripe",
            "solid_header",
        ]
    )

    # Random decorative offset
    decoration_offset = random.randint(-15, 15)

    # =========================================================
    # IMAGE
    # =========================================================

    image = Image.new(
        "RGB",
        (width, height),
        "white",
    )

    draw = ImageDraw.Draw(image)

    # =========================================================
    # LARGE COLOR HEADER
    # =========================================================

    draw.rounded_rectangle(
        (
            25,
            25,
            width - 25,
            header_height,
        ),
        radius=22,
        fill=light_color,
    )

    # Large colored shape
    if accent_direction == "top":
        draw.rectangle(
            (
                25,
                25,
                width - 25,
                40,
            ),
            fill=primary_color,
        )

    elif accent_direction == "left":
        draw.rectangle(
            (
                25,
                25,
                40,
                header_height,
            ),
            fill=primary_color,
        )

    else:
        draw.rectangle(
            (
                width - 40,
                25,
                width - 25,
                header_height,
            ),
            fill=primary_color,
        )

    # =========================================================
    # HEADER DECORATION
    # =========================================================

    circle_size = random.choice([75, 90, 105])

    circle_x = width - 135 + decoration_offset
    circle_y = 45 + random.randint(-5, 15)

    draw.ellipse(
        (
            circle_x,
            circle_y,
            circle_x + circle_size,
            circle_y + circle_size,
        ),
        fill=secondary_color,
    )

    draw.ellipse(
        (
            circle_x + 25,
            circle_y + 25,
            circle_x + circle_size + 25,
            circle_y + circle_size + 25,
        ),
        fill=accent_color,
    )

    # =========================================================
    # HEADER TITLE
    # =========================================================

    title_x = content_left + random.choice([0, 5, 15])
    title_y = 58 + random.randint(-5, 10)

    draw.text(
        (
            title_x,
            title_y,
        ),
        "INVOICE",
        font=title_font,
        fill=text_color,
    )

    draw.text(
        (
            title_x,
            title_y + 55,
        ),
        "Professional billing statement",
        font=small_font,
        fill=secondary_text,
    )

    # Color bars
    bar_y = title_y + 88

    bar_lengths = [
        random.randint(45, 80),
        random.randint(30, 60),
        random.randint(20, 45),
        random.randint(25, 55),
    ]

    bar_colors = [
        primary_color,
        secondary_color,
        accent_color,
        extra_color,
    ]

    current_x = title_x

    for length, color in zip(bar_lengths, bar_colors):
        draw.rounded_rectangle(
            (
                current_x,
                bar_y,
                current_x + length,
                bar_y + 7,
            ),
            radius=3,
            fill=color,
        )

        current_x += length + 8

    # =========================================================
    # INVOICE META BADGE
    # =========================================================

    meta_width = 220
    meta_height = 78

    meta_x = width - margin_right - meta_width
    meta_y = header_height - meta_height - 18

    draw.rounded_rectangle(
        (
            meta_x,
            meta_y,
            meta_x + meta_width,
            meta_y + meta_height,
        ),
        radius=12,
        fill="white",
        outline=primary_color,
        width=2,
    )

    draw.text(
        (
            meta_x + 15,
            meta_y + 10,
        ),
        "INVOICE NO.",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            meta_x + 15,
            meta_y + 34,
        ),
        invoice_no,
        font=bold_font,
        fill=primary_color,
    )

    # =========================================================
    # BILL TO / FROM
    # =========================================================

    y = header_height + 35

    section_gap = random.choice([20, 25, 35])

    section_width = (
        content_right
        - content_left
        - section_gap
    ) // 2

    bill_x = content_left
    from_x = (
        content_left
        + section_width
        + section_gap
    )

    card_height = random.choice([145, 155, 165])

    # ---------------------------------------------------------
    # BILL TO CARD
    # ---------------------------------------------------------

    draw.rounded_rectangle(
        (
            bill_x,
            y,
            bill_x + section_width,
            y + card_height,
        ),
        radius=15,
        fill="white",
        outline=line_color,
        width=1,
    )

    # Random colored side
    bill_side = random.choice(
        [
            "left",
            "top",
        ]
    )

    if bill_side == "left":
        draw.rounded_rectangle(
            (
                bill_x,
                y,
                bill_x + 8,
                y + card_height,
            ),
            radius=4,
            fill=primary_color,
        )
    else:
        draw.rectangle(
            (
                bill_x,
                y,
                bill_x + section_width,
                y + 7,
            ),
            fill=primary_color,
        )

    draw.text(
        (
            bill_x + 20,
            y + 18,
        ),
        "BILL TO",
        font=small_bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            bill_x + 20,
            y + 47,
        ),
        bill_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            bill_x + 20,
            y + 77,
        ),
        bill_to["address"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            bill_x + 20,
            y + 99,
        ),
        bill_to["city"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            bill_x + 20,
            y + 121,
        ),
        bill_to["phone"],
        font=small_font,
        fill=secondary_text,
    )

    # ---------------------------------------------------------
    # FROM CARD
    # ---------------------------------------------------------

    draw.rounded_rectangle(
        (
            from_x,
            y,
            from_x + section_width,
            y + card_height,
        ),
        radius=15,
        fill=light_color,
        outline=secondary_color,
        width=1,
    )

    draw.text(
        (
            from_x + 20,
            y + 18,
        ),
        "FROM",
        font=small_bold_font,
        fill=secondary_color,
    )

    draw.text(
        (
            from_x + 20,
            y + 47,
        ),
        from_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            from_x + 20,
            y + 77,
        ),
        from_to["address"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            from_x + 20,
            y + 99,
        ),
        from_to["city"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            from_x + 20,
            y + 121,
        ),
        from_to["phone"],
        font=small_font,
        fill=secondary_text,
    )

    # =========================================================
    # ISSUE DATE
    # =========================================================

    date_y = y + card_height + 18

    draw.text(
        (
            content_left,
            date_y,
        ),
        "ISSUE DATE",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            content_left + 85,
            date_y,
        ),
        invoice_date,
        font=small_font,
        fill=text_color,
    )

    # Small decorative line
    draw.line(
        (
            content_right - 160,
            date_y + 10,
            content_right,
            date_y + 10,
        ),
        fill=accent_color,
        width=3,
    )

    # =========================================================
    # TABLE
    # =========================================================

    y = date_y + 42

    draw.text(
        (
            content_left,
            y,
        ),
        "ITEM DETAILS",
        font=bold_font,
        fill=text_color,
    )

    y += 35

    description_x = content_left + 15
    qty_x = content_left + 325
    price_x = content_left + 410
    total_x = content_left + 535

    table_top = y

    # ---------------------------------------------------------
    # TABLE HEADER
    # ---------------------------------------------------------

    if table_style == "solid_header":

        draw.rounded_rectangle(
            (
                content_left,
                y,
                content_right,
                y + 42,
            ),
            radius=8,
            fill=primary_color,
        )

        header_color = "white"

    elif table_style == "rounded":

        draw.rounded_rectangle(
            (
                content_left,
                y,
                content_right,
                y + 42,
            ),
            radius=8,
            outline=primary_color,
            width=2,
            fill=light_color,
        )

        header_color = primary_color

    else:

        draw.rectangle(
            (
                content_left,
                y,
                content_right,
                y + 42,
            ),
            fill=light_color,
        )

        header_color = primary_color

    draw.text(
        (
            description_x,
            y + 12,
        ),
        "DESCRIPTION",
        font=small_bold_font,
        fill=header_color,
    )

    draw.text(
        (
            qty_x,
            y + 12,
        ),
        "QTY",
        font=small_bold_font,
        fill=header_color,
    )

    draw.text(
        (
            price_x,
            y + 12,
        ),
        "PRICE",
        font=small_bold_font,
        fill=header_color,
    )

    draw.text(
        (
            total_x,
            y + 12,
        ),
        "TOTAL",
        font=small_bold_font,
        fill=header_color,
    )

    y += 58

    # =========================================================
    # TABLE ROWS
    # =========================================================

    indicator_colors = [
        primary_color,
        secondary_color,
        accent_color,
        extra_color,
    ]

    for index, item in enumerate(items):

        row_height = 48

        # Random row style
        if index % 2 == 0:

            row_fill = random.choice(
                [
                    "#FAFAFA",
                    light_color,
                    "#F8FAFC",
                ]
            )

            draw.rounded_rectangle(
                (
                    content_left,
                    y - 7,
                    content_right,
                    y + row_height - 4,
                ),
                radius=6,
                fill=row_fill,
            )

        # Color marker
        marker_color = indicator_colors[
            index % len(indicator_colors)
        ]

        marker_width = random.choice([5, 7, 9])

        draw.rounded_rectangle(
            (
                content_left,
                y + 5,
                content_left + marker_width,
                y + 29,
            ),
            radius=3,
            fill=marker_color,
        )

        draw.text(
            (
                description_x + 5,
                y,
            ),
            item["description"],
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                qty_x,
                y,
            ),
            str(item["qty"]),
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                price_x,
                y,
            ),
            f"{item['price']:,.2f}",
            font=small_font,
            fill=text_color,
        )

        draw.text(
            (
                total_x,
                y,
            ),
            f"{item['total']:,.2f}",
            font=small_bold_font,
            fill=primary_color,
        )

        y += row_height

        draw.line(
            (
                content_left,
                y - 7,
                content_right,
                y - 7,
            ),
            fill=line_color,
            width=1,
        )

    # =========================================================
    # TOTAL BOX
    # =========================================================

    y += 18

    total_width = 285
    total_height = 75

    total_x = content_right - total_width

    draw.rounded_rectangle(
        (
            total_x,
            y,
            content_right,
            y + total_height,
        ),
        radius=14,
        fill=primary_color,
    )

    draw.text(
        (
            total_x + 20,
            y + 18,
        ),
        "SUBTOTAL",
        font=small_bold_font,
        fill="white",
    )

    draw.text(
        (
            total_x + 20,
            y + 41,
        ),
        "Amount due",
        font=small_font,
        fill="#E5E7EB",
    )

    draw.text(
        (
            content_right - 125,
            y + 25,
        ),
        f"{subtotal:,.2f}",
        font=bold_font,
        fill="white",
    )

    # =========================================================
    # LOWER SECTION
    # =========================================================

    y += total_height + 35

    lower_gap = random.choice([20, 30, 40])

    lower_width = (
        content_right
        - content_left
        - lower_gap
    ) // 2

    lower_height = 165

    # Randomly swap NOTE / PAYMENT positions
    swap_cards = random.choice([True, False])

    if not swap_cards:

        note_x = content_left
        payment_x = (
            content_left
            + lower_width
            + lower_gap
        )

    else:

        payment_x = content_left
        note_x = (
            content_left
            + lower_width
            + lower_gap
        )

    # =========================================================
    # NOTE CARD
    # =========================================================

    draw.rounded_rectangle(
        (
            note_x,
            y,
            note_x + lower_width,
            y + lower_height,
        ),
        radius=14,
        fill="#FAFAFA",
        outline=line_color,
        width=1,
    )

    note_color = random.choice(
        [
            accent_color,
            secondary_color,
            extra_color,
        ]
    )

    draw.rectangle(
        (
            note_x,
            y,
            note_x + lower_width,
            y + 8,
        ),
        fill=note_color,
    )

    draw.text(
        (
            note_x + 18,
            y + 25,
        ),
        "NOTE",
        font=bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            note_x + 18,
            y + 62,
        ),
        note,
        font=small_font,
        fill=secondary_text,
    )

    # =========================================================
    # PAYMENT CARD
    # =========================================================

    draw.rounded_rectangle(
        (
            payment_x,
            y,
            payment_x + lower_width,
            y + lower_height,
        ),
        radius=14,
        fill=light_color,
        outline=secondary_color,
        width=1,
    )

    draw.text(
        (
            payment_x + 18,
            y + 22,
        ),
        "PAYMENT INFORMATION",
        font=bold_font,
        fill=primary_color,
    )

    draw_label_value(
        draw,
        payment_x + 18,
        y + 58,
        "Bank",
        payment_information["bank"],
        label_width=70,
        label_font=small_font,
        value_font=small_font,
        label_color=secondary_text,
        value_color=text_color,
    )

    draw_label_value(
        draw,
        payment_x + 18,
        y + 82,
        "Account",
        payment_information["account_name"],
        label_width=70,
        label_font=small_font,
        value_font=small_font,
        label_color=secondary_text,
        value_color=text_color,
    )

    draw_label_value(
        draw,
        payment_x + 18,
        y + 106,
        "No.",
        payment_information["account_number"],
        label_width=70,
        label_font=small_font,
        value_font=small_font,
        label_color=secondary_text,
        value_color=text_color,
    )

    draw_label_value(
        draw,
        payment_x + 18,
        y + 130,
        "Email",
        payment_information["email"],
        label_width=70,
        label_font=small_font,
        value_font=small_font,
        label_color=secondary_text,
        value_color=text_color,
    )

    # =========================================================
    # FOOTER
    # =========================================================

    footer_y = height - 55

    footer_variant = random.choice(
        [
            "line",
            "blocks",
            "minimal",
        ]
    )

    if footer_variant == "line":

        draw.line(
            (
                content_left,
                footer_y,
                content_right,
                footer_y,
            ),
            fill=line_color,
            width=1,
        )

        draw.text(
            (
                content_left,
                footer_y + 15,
            ),
            "Thank you for your business.",
            font=small_font,
            fill=secondary_text,
        )

    elif footer_variant == "blocks":

        draw.text(
            (
                content_left,
                footer_y + 8,
            ),
            "Thank you for your business.",
            font=small_font,
            fill=secondary_text,
        )

        block_x = content_right - 125

        footer_colors = [
            primary_color,
            secondary_color,
            accent_color,
            extra_color,
        ]

        random.shuffle(footer_colors)

        for i, color in enumerate(footer_colors):

            block_width = random.choice([18, 22, 28])

            draw.rectangle(
                (
                    block_x,
                    footer_y + 7,
                    block_x + block_width,
                    footer_y + 23,
                ),
                fill=color,
            )

            block_x += block_width + 5

    else:

        draw.text(
            (
                content_left,
                footer_y + 8,
            ),
            "Thank you for your business.",
            font=small_font,
            fill=secondary_text,
        )

        draw.line(
            (
                content_right - 90,
                footer_y + 18,
                content_right,
                footer_y + 18,
            ),
            fill=primary_color,
            width=3,
        )

    return image


# =============================================================
# EXAMPLE
# =============================================================

def example_template_5():
    invoice = create_invoice_template_5(
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

