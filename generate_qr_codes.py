"""
Generate QR codes for PayPal and Venmo donation links with Gillsystems logo overlay.
Requires: qrcode, pillow (PIL)
"""
import qrcode
from PIL import Image
import io
import base64
import os

# Logo image data (base64 encoded from attachment)
LOGO_BASE64 = """
iVBORw0KGgoAAAANSUhEUgAAA5QAAADICAYAAACkH0vhAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSogMAjABBgAYAAQAABQBBQACBQAA... [truncated for brevity]
"""

# Donation URLs
PAYPAL_URL = "https://paypal.me/gillsystems"
VENMO_URL = "https://venmo.com/Stephen-Gill-007"

def create_qr_with_logo(url, output_filename, logo_path=None):
    """Generate a QR code with an optional logo overlay."""
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction allows logo overlay
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # If logo provided, overlay it
    if logo_path:
        try:
            logo = Image.open(logo_path)
            
            # Calculate logo size (should be about 1/5 of QR code size)
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 5
            
            # Resize logo maintaining aspect ratio
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Create a white background for the logo (for better visibility)
            logo_bg_size = int(logo_size * 1.2)
            logo_bg = Image.new('RGB', (logo_bg_size, logo_bg_size), 'white')
            
            # Calculate position to center logo background
            logo_bg_pos = (
                (qr_width - logo_bg_size) // 2,
                (qr_height - logo_bg_size) // 2
            )
            
            # Paste logo background
            qr_img.paste(logo_bg, logo_bg_pos)
            
            # Calculate position to center logo
            logo_pos = (
                (qr_width - logo.width) // 2,
                (qr_height - logo.height) // 2
            )
            
            # Paste logo (with alpha channel if available)
            if logo.mode == 'RGBA':
                qr_img.paste(logo, logo_pos, logo)
            else:
                qr_img.paste(logo, logo_pos)
                
        except Exception as e:
            print(f"Warning: Could not overlay logo - {e}")
    
    # Save QR code
    qr_img.save(output_filename, 'PNG')
    print(f"✓ Generated: {output_filename}")

def main():
    # Check if logo file exists
    logo_file = "gillsystems_logo.png"
    
    # Try to decode and save the logo first
    print("Creating Gillsystems logo file...")
    # For now, we'll create QR codes without logo and let user add the logo file
    # Since the base64 data would be too large for this script
    
    print("\nGenerating QR codes...")
    print("Note: Please save your logo as 'gillsystems_logo.png' in the repo folder")
    print("      Then run this script again to embed the logo.\n")
    
    # Generate QR codes
    try:
        create_qr_with_logo(PAYPAL_URL, "qr-paypal.png", logo_file if os.path.exists(logo_file) else None)
        create_qr_with_logo(VENMO_URL, "qr-venmo.png", logo_file if os.path.exists(logo_file) else None)
        print("\n✓ QR codes generated successfully!")
        print(f"  - qr-paypal.png (PayPal: {PAYPAL_URL})")
        print(f"  - qr-venmo.png (Venmo: {VENMO_URL})")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


    # --- Composite logo + QR + icons for README bottom ---
    def composite_logo_with_qrs_and_icons():
        base_logo = Image.open("Gill Systems Logo.png").convert("RGBA")
        qr_paypal = Image.open("qr-paypal.png").convert("RGBA")
        qr_venmo = Image.open("qr-venmo.png").convert("RGBA")
        icon_paypal = Image.open("paypal_icon.png").convert("RGBA")
        icon_venmo = Image.open("venmo_icon.png").convert("RGBA")

        # Resize QR codes and icons for overlay
        qr_size = int(base_logo.height * 0.45)
        icon_size = int(qr_size * 0.28)
        qr_paypal = qr_paypal.resize((qr_size, qr_size), Image.LANCZOS)
        qr_venmo = qr_venmo.resize((qr_size, qr_size), Image.LANCZOS)
        icon_paypal = icon_paypal.resize((icon_size, icon_size), Image.LANCZOS)
        icon_venmo = icon_venmo.resize((icon_size, icon_size), Image.LANCZOS)

        # Position: top right, above the text area
        margin = int(base_logo.height * 0.04)
        qr1_x = base_logo.width - qr_size*2 - margin*2
        qr2_x = base_logo.width - qr_size - margin
        qr_y = margin

        # Paste QR codes
        logo_with_qrs = base_logo.copy()
        logo_with_qrs.paste(qr_paypal, (qr1_x, qr_y), qr_paypal)
        logo_with_qrs.paste(qr_venmo, (qr2_x, qr_y), qr_venmo)

        # Paste icons below each QR
        icon_y = qr_y + qr_size + margin//2
        logo_with_qrs.paste(icon_paypal, (qr1_x + (qr_size-icon_size)//2, icon_y), icon_paypal)
        logo_with_qrs.paste(icon_venmo, (qr2_x + (qr_size-icon_size)//2, icon_y), icon_venmo)

        # Save composite
        logo_with_qrs.save("readme_donation_bottom_Gillsystems_Logo.png")
        print("Saved: readme_donation_bottom_Gillsystems_Logo.png")

    if __name__ == "__main__":
        import sys
        main()
        composite_logo_with_qrs_and_icons()
