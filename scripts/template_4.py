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


def create_invoice_template_4(
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
            "light": "#EFF6FF",
        },
        {
            "primary": "#16A34A",
            "secondary": "#14B8A6",
            "accent": "#EAB308",
            "light": "#F0FDF4",
        },
        {
            "primary": "#DC2626",
            "secondary": "#F97316",
            "accent": "#F59E0B",
            "light": "#FEF2F2",
        },
        {
            "primary": "#7C3AED",
            "secondary": "#DB2777",
            "accent": "#F59E0B",
            "light": "#F5F3FF",
        },
        {
            "primary": "#0891B2",
            "secondary": "#2563EB",
            "accent": "#8B5CF6",
            "light": "#ECFEFF",
        },
        {
            "primary": "#DB2777",
            "secondary": "#9333EA",
            "accent": "#F97316",
            "light": "#FDF2F8",
        },
    ]

    palette = random.choice(palettes)

    primary_color = palette["primary"]
    secondary_color = palette["secondary"]
    accent_color = palette["accent"]
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
        42,
    )

    huge_font = ImageFont.truetype(
        "./fonts/Roboto-Bold.ttf",
        56,
    )

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
    # LEFT COLOR SIDEBAR
    # =========================================================

    sidebar_width = 125

    draw.rectangle(
        (
            0,
            0,
            sidebar_width,
            height,
        ),
        fill=primary_color,
    )

    block_height = height // 5

    colors = [
        primary_color,
        secondary_color,
        accent_color,
        "#8B5CF6",
        "#14B8A6",
    ]

    random.shuffle(colors)

    for i, color in enumerate(colors):
        draw.rectangle(
            (
                0,
                i * block_height,
                sidebar_width,
                (i + 1) * block_height,
            ),
            fill=color,
        )

    # =========================================================
    # VERTICAL INVOICE TEXT
    # =========================================================

    letters = "INVOICE"

    for i, letter in enumerate(letters):
        draw.text(
            (
                34,
                90 + i * 65,
            ),
            letter,
            font=huge_font,
            fill="white",
        )

    # =========================================================
    # CONTENT AREA
    # =========================================================

    left = sidebar_width + 40
    right = width - 40
    content_width = right - left

    y = 55

    # =========================================================
    # TOP HEADER
    # =========================================================

    draw.text(
        (
            left,
            y,
        ),
        "INVOICE",
        font=title_font,
        fill=text_color,
    )

    draw.text(
        (
            left,
            y + 52,
        ),
        "Professional billing statement",
        font=small_font,
        fill=secondary_text,
    )

    # Color decoration

    draw.rectangle(
        (
            left,
            y + 83,
            left + 80,
            y + 89,
        ),
        fill=primary_color,
    )

    draw.rectangle(
        (
            left + 85,
            y + 83,
            left + 125,
            y + 89,
        ),
        fill=secondary_color,
    )

    draw.rectangle(
        (
            left + 130,
            y + 83,
            left + 150,
            y + 89,
        ),
        fill=accent_color,
    )

    # =========================================================
    # INVOICE METADATA
    # =========================================================

    meta_width = 270
    meta_x = right - meta_width
    meta_y = 50

    draw.text(
        (
            meta_x,
            meta_y,
        ),
        "INVOICE NUMBER",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            meta_x,
            meta_y + 22,
        ),
        invoice_no,
        font=bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            meta_x,
            meta_y + 58,
        ),
        "ISSUE DATE",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            meta_x,
            meta_y + 80,
        ),
        invoice_date,
        font=small_font,
        fill=text_color,
    )

    # =========================================================
    # BILL TO
    # =========================================================

    y = 170

    bill_width = int(content_width * 0.58)

    draw.rectangle(
        (
            left,
            y,
            left + bill_width,
            y + 145,
        ),
        fill=light_color,
    )

    draw.rectangle(
        (
            left,
            y,
            left + 7,
            y + 145,
        ),
        fill=primary_color,
    )

    draw.text(
        (
            left + 22,
            y + 18,
        ),
        "BILL TO",
        font=small_bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            left + 22,
            y + 48,
        ),
        bill_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            left + 22,
            y + 77,
        ),
        bill_to["address"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            left + 22,
            y + 99,
        ),
        bill_to["city"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            left + 22,
            y + 121,
        ),
        bill_to["phone"],
        font=small_font,
        fill=secondary_text,
    )

    # =========================================================
    # FROM
    # =========================================================

    from_x = left + bill_width + 20
    from_width = right - from_x

    draw.text(
        (
            from_x,
            y,
        ),
        "FROM",
        font=small_bold_font,
        fill=secondary_color,
    )

    draw.text(
        (
            from_x,
            y + 27,
        ),
        from_to["name"],
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            from_x,
            y + 57,
        ),
        from_to["address"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            from_x,
            y + 79,
        ),
        from_to["city"],
        font=small_font,
        fill=secondary_text,
    )

    draw.text(
        (
            from_x,
            y + 101,
        ),
        from_to["phone"],
        font=small_font,
        fill=secondary_text,
    )

    # =========================================================
    # TABLE
    # =========================================================

    y = 355

    draw.text(
        (
            left,
            y,
        ),
        "SERVICES",
        font=bold_font,
        fill=text_color,
    )

    y += 40

    description_x = left
    qty_x = left + 310
    price_x = left + 390
    total_x = left + 520

    # Header line

    draw.line(
        (
            left,
            y,
            right,
            y,
        ),
        fill=primary_color,
        width=3,
    )

    y += 15

    draw.text(
        (
            description_x,
            y,
        ),
        "DESCRIPTION",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            qty_x,
            y,
        ),
        "QTY",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            price_x,
            y,
        ),
        "PRICE",
        font=small_bold_font,
        fill=secondary_text,
    )

    draw.text(
        (
            total_x,
            y,
        ),
        "TOTAL",
        font=small_bold_font,
        fill=secondary_text,
    )

    y += 38

    # =========================================================
    # TABLE ROWS
    # =========================================================

    indicator_colors = [
        primary_color,
        secondary_color,
        accent_color,
    ]

    for index, item in enumerate(items):

        # Alternating row background

        if index % 2 == 0:
            draw.rectangle(
                (
                    left - 10,
                    y - 8,
                    right + 10,
                    y + 35,
                ),
                fill="#FAFAFA",
            )

        # Colored indicator

        indicator_color = indicator_colors[
            index % len(indicator_colors)
        ]

        draw.rectangle(
            (
                left,
                y + 2,
                left + 5,
                y + 27,
            ),
            fill=indicator_color,
        )

        draw.text(
            (
                description_x + 15,
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

        y += 48

        draw.line(
            (
                left,
                y - 8,
                right,
                y - 8,
            ),
            fill=line_color,
            width=1,
        )

    # =========================================================
    # SUBTOTAL
    # =========================================================

    y += 20

    subtotal_width = 280
    subtotal_x = right - subtotal_width

    draw.text(
        (
            subtotal_x,
            y,
        ),
        "SUBTOTAL",
        font=bold_font,
        fill=text_color,
    )

    draw.text(
        (
            subtotal_x + 135,
            y,
        ),
        f"{subtotal:,.2f}",
        font=bold_font,
        fill=primary_color,
    )

    draw.line(
        (
            subtotal_x,
            y + 35,
            right,
            y + 35,
        ),
        fill=primary_color,
        width=2,
    )

    y += 80

    # =========================================================
    # LOWER SECTION
    # =========================================================

    lower_gap = 30

    lower_width = (
        content_width - lower_gap
    ) // 2

    # =========================================================
    # NOTE CARD
    # =========================================================

    note_x = left

    draw.rounded_rectangle(
        (
            note_x,
            y,
            note_x + lower_width,
            y + 155,
        ),
        radius=12,
        fill="#FAFAFA",
        outline=line_color,
        width=1,
    )

    draw.rectangle(
        (
            note_x,
            y,
            note_x + lower_width,
            y + 7,
        ),
        fill=accent_color,
    )

    draw.text(
        (
            note_x + 18,
            y + 22,
        ),
        "NOTE",
        font=bold_font,
        fill=primary_color,
    )

    draw.text(
        (
            note_x + 18,
            y + 58,
        ),
        note,
        font=small_font,
        fill=secondary_text,
    )

    # =========================================================
    # PAYMENT CARD
    # =========================================================

    payment_x = (
        left
        + lower_width
        + lower_gap
    )

    draw.rounded_rectangle(
        (
            payment_x,
            y,
            right,
            y + 155,
        ),
        radius=12,
        fill=light_color,
        outline=primary_color,
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

    footer_y = height - 65

    draw.line(
        (
            left,
            footer_y,
            right,
            footer_y,
        ),
        fill=line_color,
        width=1,
    )

    draw.text(
        (
            left,
            footer_y + 18,
        ),
        "Thank you for your business.",
        font=small_font,
        fill=secondary_text,
    )

    # Footer color decorations

    draw.rectangle(
        (
            right - 100,
            footer_y + 16,
            right - 70,
            footer_y + 31,
        ),
        fill=primary_color,
    )

    draw.rectangle(
        (
            right - 65,
            footer_y + 16,
            right - 45,
            footer_y + 31,
        ),
        fill=secondary_color,
    )

    draw.rectangle(
        (
            right - 40,
            footer_y + 16,
            right - 20,
            footer_y + 31,
        ),
        fill=accent_color,
    )

    return image


# =============================================================
# EXAMPLE
# =============================================================

def example_template_4():
    invoice = create_invoice_template_4(
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