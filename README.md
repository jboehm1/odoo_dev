# Odoo Dev – Test and Static Map Modules

This repository contains sample Odoo 16 modules for basic app demonstrations and advanced address management using Google Maps.

## Included Modules

### 1. Simple App

> A demo module showing the minimal structure of an Odoo add-on: manifest, Python model, XML view.

- **Goal:** Provide a starting point for developing and testing Odoo modules.
- **Key files:** 
    - `__init__.py`
    - `__manifest__.py`
    - `models/`

### 2. Address Map Static

> This module enables you to **display a static Google Map** (Static Maps API) directly on a contact (res.partner) form, based on the stored address or GPS coordinates.

**Features:**
- Adds a "Map" tab or field to the contact form.
- Dynamically generates a Google Maps image using the contact’s address.
- Module can be configured from the Odoo backend Settings.

#### Settings

A custom option is added to the Odoo Settings menu:
- **Show map on contact form**
    - Enables/disables the map display on each partner record.
    - Can be managed from “Settings” > “Technical Settings” > “Address Map Static”.

Includes a field for your **Google Maps API Key**:
- Lets you use the Google Maps Static service securely, according to your project’s API key and quotas.

Key files:
- `res_config_settings_view.xml` (settings view)
- `models/res_config_settings.py` (configuration storage)

#### Code Structure

- `address_map/__init__.py`: module initializer
- `address_map/__manifest__.py`: Odoo manifest
- `address_map/models/`: Python models (contacts, config)
- `address_map/views/`: XML views (contact, settings)

## Installation

1. **Clone the repository**
