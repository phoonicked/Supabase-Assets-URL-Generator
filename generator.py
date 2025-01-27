import json
from supabase import create_client, Client


supabase_url = ''  # Replace with Supabase URL
supabase_key = ''  # Replace with Supabase Service Role key
supabase: Client = create_client(supabase_url, supabase_key)

def generate_public_urls(file_names):
    try:
        # Generate public URLs
        public_urls = []
        for file_name in file_names:
            print(f"Processing file: {file_name}")
            public_url = f"{supabase_url}/storage/v1/object/public/images/{file_name}"
            public_urls.append(public_url)

        # Construct the JSON structure
        json_output = {
            "image": public_urls
        }

        # Save the JSON to a file
        with open('images.json', 'w') as json_file:
            json.dump(json_output, json_file, indent=2)

        print('Public URLs JSON saved to images.json')

    except Exception as e:
        print('An error occurred:', e)

if __name__ == '__main__':
    while True:
        file_names_input = input("Enter the file names separated by commas (e.g., 03.01.05.jpg, 03.01.06.jpg) or press Enter to stop: ")
        if not file_names_input.strip():
            print("No input provided. Exiting...")
            break
        file_names = [file_name.strip() for file_name in file_names_input.split(',')]
        generate_public_urls(file_names)
