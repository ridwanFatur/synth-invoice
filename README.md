# Synthetic Invoice Dataset

A synthetic invoice image dataset designed for training and evaluating document AI, OCR, and invoice information extraction models.

The dataset contains invoice images generated programmatically using Python and [Pillow](https://python-pillow.org/). Each invoice is created from randomly generated structured data and rendered using one of five invoice templates. The generated documents are then augmented with paper texture, stains, noise, deformation, and perspective effects to simulate real-world scanned or photographed invoices.

The dataset is available on Hugging Face:

**Hugging Face Dataset:** https://huggingface.co/datasets/ridwanFatur98/synth-invoice

## Dataset Generation

The invoices are generated using the Python notebook `generate.ipynb` and supporting scripts under `scripts/`.

The generation pipeline consists of the following stages:

1. Generate random invoice data.
2. Select one of five invoice templates.
3. Render the structured data into an invoice image.
4. Apply paper texture and wrinkles.
5. Add stains, speckles, and image grain.
6. Apply rotation, bending, and perspective deformation.
7. Save the generated image together with its structured metadata.

### Generated Invoice Data

Each invoice contains the following information:

* Bill-to company

  * Company name
  * Address
  * City
  * Phone number
  * Email address
* Invoice date
* Invoice number
* Issuing company

  * Company name
  * Address
  * City
  * Phone number
  * Email address
* Invoice items

  * Description
  * Quantity
  * Unit price
  * Total
* Subtotal
* Payment note
* Payment information

  * Bank
  * Account name
  * Account number
  * Email address

The generated content uses Indonesian-oriented company names, addresses, cities, banks, phone numbers, and business information.

## Invoice Templates

Five different invoice layouts are used during generation:

* Template 1
* Template 2
* Template 3
* Template 4
* Template 5

Each template uses the same underlying invoice schema but has a different visual layout. This provides layout diversity for document understanding models.

## Image Augmentation

To make the synthetic documents more representative of real-world documents, generated invoices are augmented with several effects.

### Paper Texture

Random paper wrinkles and shading are applied to simulate physical paper.

### Noise and Stains

The images can contain:

* Random stains
* Small speckles
* Image grain
* Variable opacity
* Variable stain sizes

### Paper Deformation

The document can also be randomly transformed using:

* Rotation
* Bending
* Horizontal deformation
* Perspective distortion

These augmentations are intended to simulate invoices captured by cameras or scanned under imperfect conditions.

## Example

An example generated invoice is included in the repository under `misc/example/`.

![Example invoice](misc/example/example.png)

The example demonstrates the type of invoice images contained in the dataset, including the document layout, tabular line items, payment information, and synthetic paper imperfections.

## Dataset Structure

The source project is organized as follows:

```
.
├── README.md
├── generate.ipynb
├── _clean_hf.ipynb
├── dataset/
├── fonts/
│   ├── OpenSans-Bold.ttf
│   ├── OpenSans-Regular.ttf
│   ├── Roboto-Bold.ttf
│   └── Roboto-Regular.ttf
├── misc/
│   └── example/
└── scripts/
    ├── template_1.py
    ├── template_2.py
    ├── template_3.py
    ├── template_4.py
    ├── template_5.py
    ├── texture_1.py
    ├── noise_1.py
    ├── warp_1.py
    └── utils.py
```

The generated dataset uploaded to Hugging Face can be loaded directly using the `datasets` library.

## Loading the Dataset

Install the Hugging Face Datasets library:

```
pip install datasets
```

Then load the dataset:

```
from datasets import load_dataset

ds = load_dataset("ridwanFatur98/synth-invoice")
```

The dataset provides the generated training and test splits.

For example:

```
train_dataset = ds["train"]
test_dataset = ds["test"]
```

## Example Metadata

A generated invoice is associated with structured data similar to:

```
{
    "bill_to": {
        "name": "CV Nusantara Sejahtera",
        "address": "Gang Laswi No. 0",
        "city": "Subulussalam, Indonesia",
        "phone": "+62 886-4121-4341",
        "email": "finance@cvnusantarasejahtera.com"
    },
    "invoice_date": "23 March 2025",
    "invoice_no": "INV-2025-91329",
    "from_to": {
        "name": "CV Sinar Digital",
        "address": "Gg. BKR No. 136",
        "city": "Banjarmasin, Indonesia",
        "phone": "+62 839-1050-2328",
        "email": "billing@cvsinardigital.com"
    },
    "items": [
        {
            "description": "Technical Support",
            "qty": 10,
            "price": 4250000,
            "total": 42500000
        },
        {
            "description": "Software Testing",
            "qty": 2,
            "price": 4650000,
            "total": 9300000
        }
    ],
    "subtotal": 51800000,
    "note": "Please include the invoice number with your payment.",
    "payment_information": {
        "bank": "Bank Permata",
        "account_name": "CV Sinar Digital",
        "account_number": "6224843555",
        "email": "billing@cvsinardigital.com"
    }
}
```

## Intended Use

This dataset can be used for experiments involving:

* OCR
* Document understanding
* Invoice information extraction
* Document image classification
* Key-value extraction
* Table and line-item extraction
* Image-to-JSON models
* Encoder-decoder document models
* Synthetic data augmentation

It was specifically created as a synthetic dataset for experimenting with invoice document understanding models.

## Limitations

This is a fully synthetic dataset. The invoice content, companies, addresses, contact information, transaction data, and document layouts are generated programmatically and do not represent real business transactions.

Although image augmentations are used to introduce realistic imperfections, the generated images may not fully capture the visual diversity and complexity of real-world invoices.

For best results, models trained on this dataset should ideally be evaluated or fine-tuned with real invoice documents as well.

## License

Please refer to the dataset repository on Hugging Face for the applicable dataset license and usage terms.

## Repository

Hugging Face:

https://huggingface.co/datasets/ridwanFatur98/synth-invoice
