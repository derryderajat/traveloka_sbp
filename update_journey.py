import json
import os

file_path = "/Users/derryderajat/UI/Perkuliahan/Semester 1/Analisis Kebutuhan & Perancangan Sistem Informasi/traveloka_sbp/journey.json"

try:
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        exit(1)

    with open(file_path, 'r') as f:
        data = json.load(f)

    if 'bundles' not in data:
        print("Error: 'bundles' key not found in JSON data")
        exit(1)

    for bundle in data['bundles']:
        if 'price_breakdown' not in bundle:
            original_price = bundle.get('original_price', 0)
            
            # Calculate prices based on proportions: flight=35%, hotel=40%, activity=25%
            flight_price = round(original_price * 0.35)
            hotel_price = round(original_price * 0.40)
            # Ensure they sum up to original_price by calculating activity_price as the remainder
            activity_price = original_price - flight_price - hotel_price
            
            bundle['price_breakdown'] = {
                "flight_price": flight_price,
                "hotel_price": hotel_price,
                "activity_price": activity_price,
                "total_price": original_price
            }

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

    print("Successfully updated journey.json with price_breakdown for each bundle.")

except json.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
