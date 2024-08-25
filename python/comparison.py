def extract_button_attributes(figma_button_data):
  button_data = None

  # Iterate through the children to find the button element
  for child in figma_button_data["children"]:
      if child["type"] == "TEXT":
          button_data = child
          break

  if button_data:
    # Extract button attributes
    button_color = button_data["fills"][0]["color"]
    button_text = button_data["characters"]
    # ... other attributes as needed

    return button_color, button_text
  else:
    print("Button element not found in the Figma data.")
    return None, None


def compare_buttons(figma_button_data, website_button):
    # Extract button attributes using the new function
    figma_button_color, figma_button_text = extract_button_attributes(figma_button_data)

    # Check if button data was extracted successfully
    if figma_button_color is not None and figma_button_text is not None:
        # Extract button attributes from the website
        website_button_color = website_button.value_of_css("background-color")
        website_button_text = website_button.text

        # Compare attributes
        if figma_button_color != website_button_color or figma_button_text != website_button_text:
            # Highlight the discrepancy on the website
            website_button.value_of_css("border", "2px solid red")
            # Add other highlighting or reporting mechanisms as needed
    else:
        print("Could not extract button attributes from Figma data.")
